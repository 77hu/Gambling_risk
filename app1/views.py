# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from .forms import RegisterForm,LoginForm
# from .test1 import main
# import asyncio
# from .llm_agent import LLM_process
# from django.views.decorators.csrf import csrf_protect
# from .embedding import FaissVectorStore
# #注册
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             messages.success(request,'注册成功！欢迎加入！')
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form':form})
#
# #登录
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request,data=request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user=authenticate(username=username,password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request,f'你已登录:{username}')
#                 return redirect('home')
#             else:
#                 messages.error(request,'用户名或者密码错误')
#         else:
#             messages.error(request, '用户名或者密码错误')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form':form})
#
# def user_logout(request):
#     logout(request)
#     messages.success(request,'你已成功退出')
#     return redirect('login')
#
#
# def dict_to_text(data:dict)->str:
#     # 按需求拼接key和value，用换行、分号等分隔
#     text = f"""URL地址：{data['url']}
#     合法性：{data['url_legitimacy']}
#     涉赌风险：{"是" if data['gambling_risk'] else "否"}
#     核心关键词：{', '.join(data['keywords'])}
#     风险分析：{data['risk_analysis']}"""
#     # print(text)
#     return text
# # 保存向量
# def save_user_vectors(texts):
#     store = FaissVectorStore(dim=768)
#     temp_data=[]
#     for text in texts:
#         temp_data.append(dict_to_text(text))
#     store.save_vectors(texts=texts,)
#
#
#
# @csrf_protect
# def home(request):
#     # print("当前用户:", request.user, "ID:", request.user.id, "是否认证:", request.user.is_authenticated)
#     context = {'results': []}
#
#     if request.method == 'POST':
#         raw_urls = request.POST.get('url', '').strip()
#         if not raw_urls:
#             context['error'] = "请输入至少一个 URL"
#             return render(request, 'home.html', context)
#
#         url_list = [u.strip() for u in raw_urls.splitlines() if u.strip()]
#         if not url_list:
#             context['error'] = "未检测到有效 URL"
#             return render(request, 'home.html', context)
#
#         try:
#             all_results = []
#             for url in url_list:
#                 try:
#                     text = asyncio.run(main(url))
#                     result = LLM_process(text, url)
#                     # 确保 result 是 dict，并包含必要字段
#                     result['url'] = url  # 用于前端显示
#                     all_results.append(result)
#                 except Exception as e:
#                     all_results.append({
#                         'url': url,
#                         'url_legitimacy': '分析失败',
#                         'gambling_risk': False,
#                         'risk_analysis': f'错误: {str(e)}',
#                         'keywords': []
#                     })
#
#             context['results'] = all_results
#             save_user_vectors(texts=all_results,)
#             # print(context)
#
#         except Exception as e:
#             context['error'] = f"系统错误：{str(e)}"
#
#     return render(request, 'home.html', context)
#
# @login_required
# def recommend(request):
#     temp=[]
#     query_text = request.GET.get('q', '').strip()
#     # print(query_text)
#     store = FaissVectorStore(dim=768)
#     # 将查询文本转为向量
#     query_vector = store.text_to_vectors([query_text])[0]  # shape: (768,)
#     # 搜索最相似的 6 条
#     results = store.search(query_vector, k=6)
#     # print(results)
#     for i in results:
#         similarity_data=i['metadata']['text']
#         #similarity_data中有url_legitimacy、gambling_risk，risk_analysis、keywords、url字段
#         temp.append(similarity_data)
#
#     return render(request, 'recommend.html', {'results': temp})
#


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError

from .forms import RegisterForm, LoginForm
from .test1 import main
import asyncio
from .llm_agent import LLM_process
from .models import URLAnalysis

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import traceback


# ======================
# 辅助函数：安全拼接文本
# ======================
def dict_to_text(data: dict) -> str:
    """安全地将分析结果 dict 转为字符串，避免 None/类型错误"""
    try:
        url = str(data.get('url', '') or '').strip()
        legitimacy = str(data.get('url_legitimacy', '') or '').strip()
        gambling_risk = bool(data.get('gambling_risk', False))
        gambling_str = "是" if gambling_risk else "否"

        keywords = data.get('keywords', [])
        if not isinstance(keywords, (list, tuple)):
            keywords = []
        keywords_clean = [str(k).strip() for k in keywords if k and str(k).strip()]
        keywords_str = ", ".join(keywords_clean)

        risk_analysis = str(data.get('risk_analysis', '') or '').strip()

        return f"""URL地址：{url}
合法性：{legitimacy}
涉赌风险：{gambling_str}
核心关键词：{keywords_str}
风险分析：{risk_analysis}""".strip()
    except Exception as e:
        # 出错时返回可读错误信息，确保 raw_text 非空
        return f"[TEXT_GEN_ERROR] 原始数据: {data} | 错误: {e}"


# ======================
# 保存分析结果到数据库
# ======================
def save_user_vectors(texts=None, user=None):
    """将分析结果保存到 MySQL，带防御式处理"""
    if not texts:
        return 0

    objs = []
    for i, data in enumerate(texts):
        try:
            raw_text = dict_to_text(data)
            if not raw_text:
                raw_text = "[EMPTY_RAW_TEXT]"

            obj = URLAnalysis(
                user=user,
                url=str(data.get('url', ''))[:500],
                url_legitimacy=str(data.get('url_legitimacy', ''))[:100],
                gambling_risk=bool(data.get('gambling_risk', False)),
                risk_analysis=str(data.get('risk_analysis', ''))[:1000],
                keywords=data.get('keywords', []),
                raw_text=raw_text,
            )
            objs.append(obj)
        except Exception as e:
            print(f"[构建 URLAnalysis 对象失败 @ {i}]: {e}")
            print("原始 data:", data)
            continue  # 跳过坏数据，不影响其他

    if not objs:
        print("[WARN] 无可保存的有效数据")
        return 0

    try:
        created = URLAnalysis.objects.bulk_create(objs)
        print(f"[INFO] 成功保存 {len(created)} 条分析记录")
        return len(created)
    except IntegrityError as e:
        print("[DB IntegrityError]:", e)
        # 尝试逐条插入（定位问题行）
        count = 0
        for obj in objs:
            try:
                obj.save()
                count += 1
            except Exception as ee:
                print(f"[单条保存失败]: {ee} | URL: {obj.url}")
        print(f"[Fallback] 逐条保存成功 {count}/{len(objs)} 条")
        return count
    except Exception as e:
        print("[保存失败（其他异常）]:", e)
        traceback.print_exc()
        return 0


# ======================
# 视图：注册
# ======================
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, '注册成功！欢迎加入！')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# ======================
# 视图：登录
# ======================
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'你已登录：{username}')
                return redirect('home')
            else:
                messages.error(request, '用户名或密码错误')
        else:
            messages.error(request, '用户名或密码错误')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# ======================
# 视图：退出
# ======================
def user_logout(request):
    logout(request)
    messages.success(request, '你已成功退出')
    return redirect('login')


# ======================
# 视图：首页（URL 分析入口）
# ======================
@login_required  # ✅ 关键：确保 request.user 有效
@csrf_protect
def home(request):
    context = {'results': []}

    if request.method == 'POST':
        raw_urls = request.POST.get('url', '').strip()
        if not raw_urls:
            messages.error(request, "请输入至少一个 URL")
            return render(request, 'home.html', context)

        url_list = [u.strip() for u in raw_urls.splitlines() if u.strip()]
        if not url_list:
            messages.error(request, "未检测到有效 URL")
            return render(request, 'home.html', context)

        print(f"[INFO] 用户 {request.user} 提交 {len(url_list)} 个 URL 分析请求")

        try:
            all_results = []
            for url in url_list:
                try:
                    text = asyncio.run(main(url))
                    result = LLM_process(text, url)
                    result['url'] = url  # 确保有 url 字段
                    all_results.append(result)
                except Exception as e:
                    error_msg = f"分析异常: {type(e).__name__}: {str(e)[:100]}"
                    print(f"[LLM_PROCESS FAIL - {url}]: {error_msg}")
                    all_results.append({
                        'url': url,
                        'url_legitimacy': '分析失败',
                        'gambling_risk': False,
                        'risk_analysis': error_msg,
                        'keywords': []
                    })

            # ✅ 保存前测试 raw_text 生成（防御）
            for i, res in enumerate(all_results):
                try:
                    test = dict_to_text(res)
                    if not test.strip():
                        print(f"[WARN] 第 {i + 1} 条 raw_text 为空: {res.get('url', '')}")
                except Exception as e:
                    print(f"[CRITICAL] dict_to_text 崩溃 @ {i}: {e}")

            # ✅ 保存数据（传入当前登录用户）
            saved_count = save_user_vectors(texts=all_results, user=request.user)
            if saved_count > 0:
                messages.success(request, f"成功分析并保存 {saved_count} 条记录")
            else:
                messages.warning(request, "分析完成，但数据保存失败（请查看日志）")

            context['results'] = all_results

        except Exception as e:
            print("[HOME VIEW OUTER EXCEPTION]:")
            traceback.print_exc()
            messages.error(request, f"系统错误：{str(e)}")

    return render(request, 'home.html', context)


# ======================
# 视图：推荐（TF-IDF + 余弦相似度）
# ======================
@login_required
def recommend(request):
    query_text = request.GET.get('q', '').strip()
    results = []


    print(f"[RECOMMEND] 查询文本: '{query_text}' | 用户: {request.user}")

    # ✅ 获取最近 100 条（非仅 6 条，提升召回）→ 后续 TF-IDF 计算快
    analyses = URLAnalysis.objects.values(
        'id', 'url', 'url_legitimacy', 'gambling_risk',
        'risk_analysis', 'keywords', 'raw_text'
    ).order_by('-created_at')[:100]  # 增加基数，提高 top-k 质量

    analyses_list = list(analyses)
    print(f"[RECOMMEND] 从 DB 加载 {len(analyses_list)} 条记录")

    if query_text and analyses_list:
        try:
            # 提取原始文本
            corpus = [a['raw_text'] for a in analyses_list if a['raw_text'].strip()]
            if not corpus:
                print("[WARN] 所有 raw_text 为空")
                return render(request, 'recommend.html', {'results': []})

            # TF-IDF 向量化
            vectorizer = TfidfVectorizer(
                max_features=5000,
                stop_words='english',
                ngram_range=(1, 2),
                lowercase=True,
                token_pattern=r'(?u)\b\w+\b'  # 默认，支持中文需改，但英文+关键词够用
            )
            tfidf_matrix = vectorizer.fit_transform(corpus)
            query_vec = vectorizer.transform([query_text])

            # 余弦相似度
            similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
            top_k = min(6, len(corpus))
            top_indices = np.argsort(similarities)[::-1][:top_k]

            # 组装结果
            for idx in top_indices:
                score = float(similarities[idx])
                if score < 0.01:  # 过滤极低相似度
                    continue
                item = analyses_list[idx].copy()
                item['similarity_score'] = round(score, 4)
                results.append(item)

            print(f"[RECOMMEND] 返回 {len(results)} 条相似结果")

        except Exception as e:
            print("[TF-IDF 计算异常]:", e)
            traceback.print_exc()
            messages.error(request, f"推荐计算失败：{e}")

    return render(request, 'recommend.html', {'results': results})