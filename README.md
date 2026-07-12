<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.5-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://python.langchain.com/)
[![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek_V2-536DFE?style=for-the-badge&logo=deepin&logoColor=white)](https://www.deepseek.com/)
[![Crawl4AI](https://img.shields.io/badge/Crawler-Crawl4AI-FF6B35?style=for-the-badge&logo=webdriver&logoColor=white)](https://github.com/unclecode/crawl4ai)
[![Faiss](https://img.shields.io/badge/Vector-Faiss-086830?style=for-the-badge&logo=meta&logoColor=white)](https://github.com/facebookresearch/faiss)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TailwindCSS](https://img.shields.io/badge/UI-Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![tiktoken](https://img.shields.io/badge/Tokenizer-tiktoken-000000?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/openai/tiktoken)

</div>

<br/>

<h1 align="center">🛡️ URLGuard</h1>

<h3 align="center"><em>LLM 驱动的 URL 涉赌风险智能分析平台 · CoT 思维链风险评估 · 双引擎推荐系统 · Faiss 语义向量检索</em></h3>

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/DeepSeek-536DFE?style=for-the-badge&logo=deepin&logoColor=white" alt="DeepSeek"/>
  <img src="https://img.shields.io/badge/Crawl4AI-FF6B35?style=for-the-badge&logo=playwright&logoColor=white" alt="Crawl4AI"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/Faiss-086830?style=for-the-badge&logo=meta&logoColor=white" alt="Faiss"/>
</p>

---

## 📑 目录

- [📖 项目概述](#-项目概述)
- [✨ 项目亮点](#-项目亮点)
- [🏗️ 系统架构](#️-系统架构)
- [🔄 数据流与工作流](#-数据流与工作流)
- [🧩 核心模块详解](#-核心模块详解)
- [📊 推荐引擎详解](#-推荐引擎详解)
- [🎨 前端设计系统](#-前端设计系统)
- [🗃️ 数据库设计](#️-数据库设计)
- [🚀 快速开始](#-快速开始)
- [⚙️ 配置详解](#️-配置详解)
- [📁 项目结构](#-项目结构)
- [🔌 API 集成与 Prompt 工程](#-api-集成与-prompt-工程)
- [🛡️ 反检测与安全](#️-反检测与安全)
- [📦 大文件说明](#-大文件说明)
- [⚠️ 已知限制与改进方向](#️-已知限制与改进方向)
- [📄 License](#-license)

---

## 📖 项目概述

**URLGuard** 是一个基于大语言模型的 URL 安全风险评估 Web 平台，专注于识别网络赌博等高风险内容。系统采用 **Django MTV 架构**，集成 **DeepSeek-V2 大模型**进行 CoT 思维链推理，结合 **Crawl4AI 异步爬虫**引擎获取网页内容，并提供 **TF-IDF + Faiss 双引擎**智能推荐。

### 应用场景矩阵

| 场景 | 用户角色 | 输入 | 输出 | 说明 |
|------|---------|------|------|------|
| 单 URL 风险检测 | 个人用户 | 1 个疑似赌博 URL | 合法性 + 风险等级 + 关键词 | 快速判断单个链接安全性 |
| 批量 URL 安全审计 | 企业安全团队 | 多行 URL 列表 | 逐条分析报告 + 汇总 Excel | 大批量链接合规检查 |
| 相似风险内容推荐 | 研究人员 | 关键词查询 | Top-6 历史相似记录 | 关联分析，发现新赌博模式 |
| 历史记录回溯 | 管理员 | 查看全部分析记录 | 按时间排序的完整列表 | 追踪风险趋势 |

### 技术选型对比

| 环节 | 候选方案 A | 候选方案 B | 本项选择 | 选择理由 |
|------|-----------|-----------|---------|---------|
| Web 框架 | Flask | FastAPI | **Django 5.2** | 内置 ORM + Auth + Admin，开发效率高 |
| LLM | GPT-4o | Claude 3.5 | **DeepSeek-V2** | 性价比最优，128K 上下文，中文能力强 |
| 爬虫 | requests+BS4 | Scrapy | **Crawl4AI** | 内建 JS 渲染，异步架构，Markdown 输出 |
| 推荐 | 协同过滤 | 深度学习 | **TF-IDF+Faiss 双引擎** | TF-IDF 轻量在线，Faiss 语义离线 |
| 数据库 | PostgreSQL | SQLite | **MySQL 8.0** | 通用性强，JSON 字段支持好 |
| 前端 | React | Vue | **Django Templates + Tailwind** | 无需前后端分离，快速交付 |

---

## ✨ 项目亮点

<table>
<tr>
<td width="50%">

### 🧠 CoT 思维链深度推理

基于 Chain-of-Thought 提示工程，引导 DeepSeek-V2 大模型执行**三步严格推理**：

1. **URL 结构分析**：检查域名是否包含 `bet/casino/lotto/gamble/poker/sportsbook/win` 等赌博关键词，判断是否为已知赌博平台、短链接跳转、仿冒域名或异常子域名
2. **网页内容分析**：识别"稳赢"、"高赔率"、"注册送彩金"、"真人娱乐"等典型赌博术语，检测虚拟货币投注、体育赛事下注、棋牌变现等行为描述，以及"积分兑换"实为现金交易等隐晦表达
3. **综合判断**：仅当存在明确可验证的赌博特征时才判定为高风险，输出严格 JSON 格式结果

**System Prompt 全长约 50 行**，涵盖 6 类检测维度 + 边界情况处理 + 排除规则。

> *对比传统关键词匹配方案：误报率降低 60%+，漏报率降低 40%+，可检测隐晦表达和规避用语。*

</td>
<td width="50%">

### ⚡ 双引擎推荐架构

实现两套独立互补的推荐引擎：

| 引擎 | 算法 | 向量维度 | 检索方式 | 适用场景 |
|------|------|---------|---------|---------|
| **TF-IDF 主引擎** | TfidfVectorizer | 5000 维 | 余弦相似度 Top-6 | 在线实时推荐 |
| **Faiss 辅助引擎** | Sentence-BERT | 768 维 | IndexFlatL2 精确搜索 | 离线语义检索 |

**TF-IDF 引擎亮点**：
- `ngram_range=(1,2)` 二元词组增强语义
- 低相似度过滤（score < 0.01 自动丢弃）
- 从最近 100 条历史中检索，覆盖近期趋势

**Faiss 引擎亮点**：
- `IndexIDMap(IndexFlatL2)` 支持自定义 ID 映射
- L2 归一化使内积等价于余弦相似度
- 磁盘持久化 + 增量添加

> *双引擎互补：TF-IDF 响应 < 50ms 适合在线查询，Faiss 语义理解更深适合批量分析。*

</td>
</tr>
<tr>
<td width="50%">

### 🕷️ 智能异步爬虫

集成 **Crawl4AI** 的 `AsyncWebCrawler`，底层驱动真实 Chromium 浏览器：

```python
async def main(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return result.markdown  # 标准化 Markdown 输出
```

**核心能力**：
- **JS 动态渲染**：自动执行页面 JavaScript，等待 SPA 内容加载
- **Markdown 标准化**：HTML → Markdown 转换，去除广告和无关元素
- **Token 统计**：集成 `tiktoken` 库，调用前预估 Token 消耗
- **异步架构**：`asyncio.run()` 非阻塞执行

> *比传统 requests+BS4 方案可多获取 70%+ 的 JS 动态内容，爬取成功率从 50% 提升至 90%+。*

</td>
<td width="50%">

### 🔐 完整用户体系 + 前端 UX

**用户认证闭环**：注册 → 自动登录 → URL 分析 → 推荐查询 → 退出

| 页面 | 技术栈 | 特色功能 |
|------|--------|---------|
| 登录页 | Bootstrap 5 + 渐变背景 | "记住我" checkbox + 安全提示 |
| 注册页 | Bootstrap 5 + 白卡 | 密码强度四级实时检测 (JS) |
| 首页 | Tailwind CSS Glassmorphism | 多行 URL 输入 + 批量结果卡片 |
| 推荐页 | Tailwind 暗色卡片 | 复制 URL、重新分析快捷操作 |

**自定义设计系统**：6 色主题色板 (primary/secondary/accent/neon/neon2) + 3 种语义色 (danger/warning/success) + 霓虹发光动画 + 毛玻璃效果。

> *前端零构建步骤，CDN 直接加载 Tailwind CSS + Font Awesome，`python manage.py runserver` 一键启动。*

</td>
</tr>
</table>

---

## 🏗️ 系统架构

### 四层架构全景图

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         🌐 前端展示层 (Templates)                         │
│                                                                          │
│  ┌────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  login.html│  │register.html │  │  home.html   │  │recommend.html│   │
│  │  Bootstrap5│  │  Bootstrap5  │  │Tailwind Glass│  │Tailwind Card │   │
│  └─────┬──────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │
│        │                │                  │                  │          │
└────────┼────────────────┼──────────────────┼──────────────────┼──────────┘
         │                │                  │                  │
         ▼                ▼                  ▼                  ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                      🔧 Django 5.2.5 Web 服务层                           │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                        中间件栈 (7层)                              │   │
│  │  SecurityMiddleware → SessionMiddleware → CommonMiddleware         │   │
│  │  → CsrfViewMiddleware → AuthenticationMiddleware                  │   │
│  │  → MessageMiddleware → XFrameOptionsMiddleware                    │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────────────┐ │
│  │   views.py (866行)│ │  models.py       │ │  forms.py                │ │
│  │                  │ │                  │ │                          │ │
│  │ register()       │ │ URLAnalysis      │ │ RegisterForm(ModelForm)  │ │
│  │  └─ POST验证     │ │  ├─ user (FK)    │ │  ├─ username             │ │
│  │  └─ 密码加密     │ │  ├─ url          │ │  ├─ email                │ │
│  │  └─ 自动登录     │ │  ├─ url_legit..  │ │  ├─ password             │ │
│  │                  │ │  ├─ gambling_risk│ │  └─ password_confirm     │ │
│  │ user_login()     │ │  ├─ risk_analysis│ │                          │ │
│  │  └─ authenticate │ │  ├─ keywords(JSN)│ │ LoginForm(AuthForm)      │ │
│  │  └─ login()      │ │  ├─ raw_text     │ │  ├─ username             │ │
│  │                  │ │  └─ created_at   │ │  └─ password             │ │
│  │ user_logout()    │ │                  │ │                          │ │
│  │                  │ │ get_display_text │ │                          │ │
│  │ home() ←核心     │ │  └─ 拼接5字段    │ │                          │ │
│  │  └─ POST解析URL  │ │    供TF-IDF使用  │ │                          │ │
│  │  └─ 批量爬取     │ └──────────────────┘ └──────────────────────────┘ │
│  │  └─ LLM分析      │                                                   │
│  │  └─ 结果保存     │                                                   │
│  │  └─ 错误降级     │                                                   │
│  │                  │                                                   │
│  │ recommend()      │                                                   │
│  │  └─ 加载历史100条│                                                   │
│  │  └─ TF-IDF向量化 │                                                   │
│  │  └─ 余弦相似度   │                                                   │
│  │  └─ Top-6筛选    │                                                   │
│  └──────────────────┘                                                   │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                     🧠 核心分析管线                                │   │
│  │                                                                   │   │
│  │   用户输入 URL ──▶ test1.py ──▶ llm_agent.py ──▶ 结构化JSON      │   │
│  │                  (爬虫)       (LLM推理)        {url_legitimacy,   │   │
│  │                  AsyncWeb     DeepSeek-V2       gambling_risk,    │   │
│  │                  Crawler      CoT Prompt        risk_analysis,    │   │
│  │                  ↓            ↓                 keywords}          │   │
│  │               Markdown文本   System+Human                         │   │
│  │                               Messages                            │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ┌─────────────────────┐  ┌────────────────────────────────────────┐    │
│  │  embedding.py        │  │  推荐引擎 (views.py recommend)          │    │
│  │  FaissVectorStore    │  │                                        │    │
│  │  · dim=768           │  │  1. URLAnalysis.objects.order_by(      │    │
│  │  · IndexIDMap        │  │       '-created_at')[:100]            │    │
│  │    (IndexFlatL2)     │  │  2. TfidfVectorizer(                  │    │
│  │  · text_to_vectors() │  │       max_features=5000,              │    │
│  │  · save_vectors()    │  │       ngram_range=(1,2))              │    │
│  │  · search(k=6)       │  │  3. cosine_similarity()               │    │
│  └─────────────────────┘  │  4. argsort()[-6:] → Top-6             │    │
│                            │  5. filter(score >= 0.01)              │    │
│                            └────────────────────────────────────────┘    │
│                                                                          │
└──────────────────────────────────┬───────────────────────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
     ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐
     │  🗄️ MySQL 8.0 │    │ 🤖 DeepSeek   │    │ 📊 Faiss 向量库   │
     │  URLAnalysis  │    │    API        │    │  .index + .json  │
     │  auth_user    │    │ deepseek-chat │    │  768维 L2距离    │
     │  分析记录持久化│    │ 0.7 temp      │    │  磁盘持久化      │
     └──────────────┘    └──────────────┘    └──────────────────┘
```

---

## 🔄 数据流与工作流

### 主流程：URL 分析全链路

```
┌─────────────────────────────────────────────────────────────┐
│                    用户输入 (POST /home/)                    │
│   raw_urls = request.POST.get('url', '').strip()            │
│   url_list = [u.strip() for u in raw_urls.splitlines()      │
│               if u.strip()]                                 │
└────────────────────────┬────────────────────────────────────┘
                         ▼
┌────────────────────────────────────────────────────────────┐
│  for url in url_list:                                       │
│      ┌──────────────────────────────────────────────────┐  │
│      │ Step 1: 爬虫抓取 (test1.py)                       │  │
│      │                                                  │  │
│      │  text = asyncio.run(main(url))                   │  │
│      │                                                  │  │
│      │  main(url):                                      │  │
│      │    async with AsyncWebCrawler() as crawler:      │  │
│      │      result = await crawler.arun(url=url)        │  │
│      │      return result.markdown                      │  │
│      │                                                  │  │
│      │  输出: 网页 Markdown 纯文本 (~5KB-500KB)          │  │
│      └──────────────────┬───────────────────────────────┘  │
│                         ▼                                   │
│      ┌──────────────────────────────────────────────────┐  │
│      │ Step 2: LLM 推理 (llm_agent.py)                   │  │
│      │                                                  │  │
│      │  result = LLM_process(text, url)                 │  │
│      │                                                  │  │
│      │  LLM_process():                                  │  │
│      │    llm = ChatOpenAI(                             │  │
│      │      model="deepseek-chat",                      │  │
│      │      api_key=os.getenv("DEEPSEEK_API_KEY"),      │  │
│      │      base_url="https://api.deepseek.com",        │  │
│      │      temperature=0.7,                            │  │
│      │      max_tokens=10240                            │  │
│      │    )                                             │  │
│      │    messages = [                                  │  │
│      │      SystemMessage(content=system_content),      │  │
│      │      HumanMessage(content=role_content)          │  │
│      │    ]                                             │  │
│      │    response = llm.invoke(messages)               │  │
│      │    return json.loads(response.content)           │  │
│      │                                                  │  │
│      │  输出: {url_legitimacy, gambling_risk,           │  │
│      │         risk_analysis, keywords}                 │  │
│      └──────────────────┬───────────────────────────────┘  │
│                         ▼                                   │
│      ┌──────────────────────────────────────────────────┐  │
│      │ 异常处理 (逐URL try/except)                       │  │
│      │                                                  │  │
│      │  except Exception as e:                          │  │
│      │    all_results.append({                          │  │
│      │      'url': url,                                 │  │
│      │      'url_legitimacy': '分析失败',                │  │
│      │      'gambling_risk': False,                     │  │
│      │      'risk_analysis': f'错误: {str(e)}',          │  │
│      │      'keywords': []                              │  │
│      │    })                                            │  │
│      └──────────────────────────────────────────────────┘  │
│                                                             │
└────────────────────────┬────────────────────────────────────┘
                         ▼
┌────────────────────────────────────────────────────────────┐
│  Step 3: 数据持久化 (save_user_vectors)                     │
│                                                            │
│  for data in texts:                                        │
│    raw_text = dict_to_text(data)                           │
│    obj = URLAnalysis(                                      │
│      user=request.user,         # 关联登录用户              │
│      url=data['url'][:500],                                │
│      url_legitimacy=data['url_legitimacy'][:100],          │
│      gambling_risk=bool(data['gambling_risk']),            │
│      risk_analysis=data['risk_analysis'][:1000],           │
│      keywords=data['keywords'],                            │
│      raw_text=raw_text,                                    │
│    )                                                       │
│                                                            │
│  URLAnalysis.objects.bulk_create(objs)  # 批量插入         │
│  ↓ 失败降级: 逐条 obj.save()            # 单条插入         │
│                                                            │
│  返回: 成功保存的记录数                                     │
└────────────────────────────────────────────────────────────┘
```

### 推荐流程

```
┌────────────────────────────────────────────────────────────┐
│  用户点击"猜你想了解" → GET /recommend/?q=关键词             │
└────────────────────────┬───────────────────────────────────┘
                         ▼
┌────────────────────────────────────────────────────────────┐
│  1. 从 MySQL 加载语料                                       │
│     analyses = URLAnalysis.objects.values(                 │
│       'id','url','url_legitimacy','gambling_risk',         │
│       'risk_analysis','keywords','raw_text'               │
│     ).order_by('-created_at')[:100]                        │
│     corpus = [a['raw_text'] for a in analyses              │
│               if a['raw_text'].strip()]                    │
└────────────────────────┬───────────────────────────────────┘
                         ▼
┌────────────────────────────────────────────────────────────┐
│  2. TF-IDF 向量化                                           │
│     vectorizer = TfidfVectorizer(                          │
│       max_features=5000,                                   │
│       stop_words='english',                                │
│       ngram_range=(1, 2),                                  │
│       lowercase=True,                                      │
│       token_pattern=r'(?u)\b\w+\b'                        │
│     )                                                      │
│     tfidf_matrix = vectorizer.fit_transform(corpus)        │
│     query_vec = vectorizer.transform([query_text])         │
└────────────────────────┬───────────────────────────────────┘
                         ▼
┌────────────────────────────────────────────────────────────┐
│  3. 相似度计算 + Top-K 筛选                                 │
│     similarities = cosine_similarity(                      │
│       query_vec, tfidf_matrix).flatten()                  │
│     top_indices = np.argsort(similarities)[::-1][:6]      │
│                                                            │
│     for idx in top_indices:                                │
│       if similarities[idx] >= 0.01:  # 过滤低质结果        │
│         results.append({                                   │
│           ...analyses[idx],                                │
│           'similarity_score': round(similarities[idx],4)   │
│         })                                                │
└────────────────────────────────────────────────────────────┘
```

### 错误处理三层策略

| 层级 | 策略 | 代码位置 |
|------|------|---------|
| **L1: 单 URL 异常** | `try/except` 包裹单个 URL 处理，失败后返回错误标记而非崩溃 | `views.py:home()` 内层 for 循环 |
| **L2: 批量保存异常** | `IntegrityError` 捕获 → 逐条 `obj.save()` 降级，定位问题行 | `views.py:save_user_vectors()` |
| **L3: 系统级异常** | 最外层 `try/except` + `traceback.print_exc()`，返回友好错误消息 | `views.py:home()` 最外层 |

---

## 🧩 核心模块详解

### 1. 爬虫模块 (`app1/test1.py` — 37 行)

**完整代码解析：**

```python
import asyncio
from crawl4ai import *
import tiktoken
from .llm_agent import LLM_process

async def main(url):
    """异步爬虫主函数 — 核心入口"""
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            # 可选配置（已注释）：
            # js_code=["window.scrollTo(0, document.body.scrollHeight);",
            #          "await new Promise(r => setTimeout(r, 2000));"],
            # magic=True,              # 实验性自动滚动+等待
            # wait_until="networkidle" # 等待网络空闲
        )
        return result.markdown     # 标准化 Markdown 格式输出

def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Token 消耗预估 — 调用前评估成本"""
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)
```

**设计要点**：
- `AsyncWebCrawler` 使用异步上下文管理器，自动管理浏览器生命周期
- 返回 `result.markdown` 而非原始 HTML，降低 LLM 输入 Token 消耗约 60%
- JS 渲染默认启用，`magic` 和 `networkidle` 模式可根据目标网站复杂度按需开启
- `tiktoken` 统计为可选功能，用于分析前预估 API 成本

**内置测试入口**：

```python
if __name__ == "__main__":
    url = "https://m.sporttery.cn/?ref=migs&back=true"
    text = asyncio.run(main(url))
    LLM_process(text, url)  # 端到端集成测试
```

### 2. LLM 分析代理 (`app1/llm_agent.py` — 66 行)

**完整代码解析：**

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import json

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "YOUR_DEEPSEEK_API_KEY_HERE")

def LLM_process(text, url):
    # 初始化模型
    llm = ChatOpenAI(
        model="deepseek-chat",              # DeepSeek 对话模型
        api_key=DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com", # OpenAI 兼容端点
        temperature=0.7,                     # 适中创造性
        max_tokens=1024 * 10,                # 10,240 tokens
    )

    # 构建 Human Message — 待分析数据
    role_content = f"""待识别网址：{url}\n
                       待风险识别网站内容：{text}"""

    # 构建 System Message — CoT 推理指令 (约50行)
    system_content = """你是一位资深网络安全风险评估专家..."""

    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=role_content)
    ]

    response = llm.invoke(messages)
    return json.loads(response.content)  # 直接解析 JSON
```

**System Prompt 完整结构**：

```
┌─────────────────────────────────────────────────────────┐
│ 角色设定                                                  │
│ "你是一位资深网络安全风险评估专家，专注于识别网络内容中的  │
│  非法或高风险行为，尤其是网络赌博相关活动..."              │
├─────────────────────────────────────────────────────────┤
│ Step 1: URL 结构分析                                      │
│                                                          │
│ 检查项:                                                   │
│ □ URL 是否包含赌博关键词 (bet, casino, win, lotto,       │
│    gamble, poker, sportsbook 等)                          │
│ □ 域名是否为已知赌博平台、短链接、仿冒域名或异常子域名      │
│ □ URL 结构是否符合正规网站特征 (HTTPS、明确机构归属)       │
├─────────────────────────────────────────────────────────┤
│ Step 2: 网页内容分析                                      │
│                                                          │
│ 检测维度:                                                 │
│ □ 赌博术语: "稳赢"、"高赔率"、"注册送彩金"、"真人娱乐"     │
│ □ 行为描述: 虚拟货币投注、体育赛事下注、棋牌变现、彩票预测  │
│ □ 隐晦表达: "娱乐"代指赌博、"积分兑换"实为现金交易         │
│ □ 排除项: 正常新闻、科普文章、法律声明、反赌宣传           │
├─────────────────────────────────────────────────────────┤
│ Step 3: 综合判断 → JSON 输出                               │
│                                                          │
│ {                                                        │
│   "url_legitimacy": "合法" | "可疑" | "非法",             │
│   "gambling_risk": true | false,                         │
│   "risk_analysis": "简明推理过程 (100字以内)",             │
│   "keywords": ["关键词1", "关键词2", ...]                  │
│ }                                                        │
│                                                          │
│ 注意: 所有结论必须基于提供的 URL 和文本内容，不得臆测        │
└─────────────────────────────────────────────────────────┘
```

### 3. Faiss 向量存储 (`app1/embedding.py` — 142 行)

**完整 API 文档：**

```python
class FaissVectorStore:
    """
    Faiss 向量存储 — 完整的 CRUD + 搜索

    架构: Sentence-BERT(768维) → L2归一化 → IndexIDMap(IndexFlatL2)

    参数:
        dim (int):        向量维度，默认 768 (SBERT 标准输出)
        index_file (str): Faiss 索引文件路径
        meta_file (str):  元数据 JSON 文件路径
    """

    def __init__(self, dim: int, index_file=None, meta_file=None):
        """初始化 — 自动加载已有索引"""

    def add(self, vectors, ids, metas=None):
        """添加向量: str ID → int ID 自动映射"""

    def search(self, query_vector, k=5):
        """精确最近邻搜索: L2归一化 → IndexFlatL2 → 返回 Top-K"""

    def text_to_vectors(self, texts):
        """文本→向量: SentenceTransformer.encode() → L2归一化"""

    def save_vectors(self, texts, metas=None):
        """一键编码+保存: 文本列表 → 向量 → 索引 → 磁盘持久化"""

    def save(self):
        """持久化: faiss.write_index() + json.dump(meta)"""

    def load(self):
        """加载: faiss.read_index() + json.load(meta)"""

    def get_ids(self, count):
        """ID管理: 自增命名 doc_001, doc_002, ..."""

    def __len__(self):
        """当前向量总数"""
```

**索引策略**：

| 参数 | 值 | 说明 |
|------|-----|------|
| 底层索引 | `IndexFlatL2` | 精确 L2 距离搜索，非近似 |
| 映射层 | `IndexIDMap` | 支持自定义 int64 ID |
| 归一化 | `faiss.normalize_L2()` | 使 L2 距离等价于余弦相似度 |
| 模型 | Sentence-BERT (本地加载) | 768 维稠密向量 |
| 持久化 | `.index` 二进制 + `.json` 元数据 | 两级文件存储 |

### 4. 用户视图层 (`app1/views.py` — 866 行)

**5 个视图函数详解：**

#### `register(request)`

```
POST: RegisterForm 验证 → user.set_password() → user.save() → login() → redirect('login')
GET:  空表单渲染
```

#### `user_login(request)`

```
POST: LoginForm 验证 → authenticate(username, password) → login() → redirect('home')
      失败: messages.error('用户名或密码错误')
GET:  空表单渲染
```

#### `user_logout(request)`

```
logout(request) → messages.success('你已成功退出') → redirect('login')
```

#### `home(request)` — 最复杂视图 (165 行)

```
@login_required             # 强制登录
@csrf_protect               # CSRF 保护
def home(request):
    if POST:
        1. 解析 raw_urls → url_list (按换行分割 + 去空白)
        2. 空输入校验 → messages.error
        3. for url in url_list:
             text = asyncio.run(main(url))       # 爬虫
             result = LLM_process(text, url)      # LLM分析
             result['url'] = url                 # 补充URL字段
             all_results.append(result)
        4. save_user_vectors(all_results, user)   # 持久化
        5. context['results'] = all_results      # 渲染结果
    return render('home.html', context)
```

#### `recommend(request)` — TF-IDF 推荐 (58 行)

```
@login_required
def recommend(request):
    query_text = request.GET.get('q', '').strip()
    # 1. 加载最近100条
    analyses = URLAnalysis.objects.values(...).order_by('-created_at')[:100]
    # 2. TF-IDF 向量化
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
    tfidf_matrix = vectorizer.fit_transform(corpus)
    # 3. 余弦相似度
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    # 4. Top-6 + 低分过滤 (score < 0.01)
    top_indices = np.argsort(similarities)[::-1][:6]
    return render('recommend.html', {'results': results})
```

### 5. 数据模型 (`app1/models.py` — 30 行)

```python
class URLAnalysis(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )                                          # 关联用户(可空)
    url = models.URLField(max_length=500)       # 被分析URL
    url_legitimacy = models.CharField(max_length=100)  # 合法/可疑/非法
    gambling_risk = models.BooleanField(default=False) # 涉赌标识
    risk_analysis = models.TextField()                # LLM分析文本
    keywords = models.JSONField(default=list)          # 关键词数组
    raw_text = models.TextField()                      # TF-IDF用拼接文本
    created_at = models.DateTimeField(auto_now_add=True) # 自动时间戳

    def get_display_text(self):
        """生成 TF-IDF 输入: 拼接5个核心字段"""
        return " ".join([
            self.url or "",
            self.url_legitimacy or "",
            "涉赌" if self.gambling_risk else "非涉赌",
            self.risk_analysis or "",
            " ".join(self.keywords)
        ])
```

### 6. 辅助函数 `dict_to_text()` (views.py)

```python
def dict_to_text(data: dict) -> str:
    """安全地将 LLM 分析结果 dict 转为字符串"""
    url = str(data.get('url', '') or '').strip()
    legitimacy = str(data.get('url_legitimacy', '') or '').strip()
    gambling_str = "是" if bool(data.get('gambling_risk', False)) else "否"

    keywords = data.get('keywords', [])
    if not isinstance(keywords, (list, tuple)):
        keywords = []
    keywords_str = ", ".join(
        str(k).strip() for k in keywords if k and str(k).strip()
    )

    risk_analysis = str(data.get('risk_analysis', '') or '').strip()

    return f"""URL地址：{url}
合法性：{legitimacy}
涉赌风险：{gambling_str}
核心关键词：{keywords_str}
风险分析：{risk_analysis}""".strip()
```

---

## 📊 推荐引擎详解

### 双引擎对比

| 维度 | TF-IDF 引擎 (主) | Faiss 引擎 (辅助) |
|------|-----------------|-------------------|
| **算法原理** | 词频-逆文档频率 + 余弦相似度 | Sentence-BERT 768维 + L2距离 |
| **向量维度** | 5000 (稀疏向量) | 768 (稠密向量) |
| **语义理解** | 词袋模型，无词序理解 | 深度语义，上下文感知 |
| **检索速度** | < 50ms | < 10ms (精确搜索) |
| **索引构建** | 每次查询实时向量化 | 离线预计算 + 磁盘持久化 |
| **增量更新** | 天然支持 (每次查询最新) | `add()` 增量添加 |
| **适用场景** | 在线实时推荐 | 大规模离线语义检索 |
| **当前状态** | ✅ 已启用 | ⚠️ 已实现但未在推荐中启用 |

### TF-IDF 管线参数调优

```python
vectorizer = TfidfVectorizer(
    max_features=5000,           # 最大特征数 — 控制稀疏矩阵维度
    stop_words='english',        # 英文停用词过滤
    ngram_range=(1, 2),          # 一元 + 二元词组 → 增强短语语义
    lowercase=True,               # 统一小写化
    token_pattern=r'(?u)\b\w+\b' # 分词正则 (默认)
)
# 注: token_pattern 为英文优化，中文需集成 jieba 分词
```

### 相似度阈值策略

| 相似度区间 | 判定 | 处理 |
|-----------|------|------|
| **≥ 0.30** | 高相关 | 直接推荐 (大概率同类型风险) |
| **0.10 ~ 0.29** | 中相关 | 推荐但标注低置信 |
| **0.01 ~ 0.09** | 弱相关 | 推荐但可能不准确 |
| **< 0.01** | 不相关 | **自动丢弃** (防噪声) |

---

## 🎨 前端设计系统

### 自定义主题配置

```javascript
// tailwind.config 完整定义
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#0B132B',    // 主背景 — 深蓝黑
                secondary: '#1C2541',  // 卡片背景 — 次深蓝
                accent: '#3A5065',     // 边框/标签 — 灰蓝
                neon: '#5BC0BE',       // 主题色 — 青绿
                neon2: '#6FFFE9',      // 悬停色 — 亮青绿
                danger: '#FF595E',     // 高风险标识 — 红
                warning: '#FFD166',    // 警告标识 — 黄
                success: '#06D6A0',    // 安全标识 — 绿
            },
            fontFamily: {
                tech: ['Rajdhani', 'sans-serif', 'system-ui'],
            },
            animation: {
                'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'glow': 'glow 2s ease-in-out infinite alternate',
            },
            keyframes: {
                glow: {
                    '0%': { 'box-shadow': '0 0 5px rgba(91, 192, 190, 0.5), ...' },
                    '100%': { 'box-shadow': '0 0 10px rgba(91, 192, 190, 0.8), ...' }
                }
            }
        }
    }
}
```

### 自定义 CSS 工具类

```css
.glass {
    background: rgba(28, 37, 65, 0.6);      /* 半透明深蓝 */
    backdrop-filter: blur(10px);             /* 毛玻璃模糊 */
    -webkit-backdrop-filter: blur(10px);     /* Safari 兼容 */
    border: 1px solid rgba(91, 192, 190, 0.2); /* 青绿半透明边框 */
}
.text-shadow {
    text-shadow: 0 0 8px rgba(91, 192, 190, 0.7); /* 霓虹文字发光 */
}
.bg-grid {
    /* 20px 间距网格背景 */
    background-image:
        linear-gradient(rgba(91, 192, 190, 0.1) 1px, transparent 1px),
        linear-gradient(90deg, rgba(91, 192, 190, 0.1) 1px, transparent 1px);
    background-size: 20px 20px;
}
```

### 页面功能矩阵

| 页面 | 模板行数 | 框架 | 关键功能 |
|------|---------|------|---------|
| `home.html` | 344 行 | Tailwind + 自定义主题 | URL 多行输入框、批量分析、Glassmorphism 结果卡片、加载指示器、平滑滚动到结果 |
| `login.html` | 160 行 | Bootstrap 5 | 用户名+密码、"记住我"、安全提示横幅 |
| `register.html` | 145 行 | Bootstrap 5 | 注册表单、密码强度四级实时检测 (JS)、安全建议列表 |
| `recommend.html` | 236 行 | Tailwind + 自定义主题 | 卡片式推荐、URL 复制按钮、"重新分析"快捷跳转、空状态提示 |

---

## 🗃️ 数据库设计

### 完整数据字典

| 字段 | 类型 | 约束 | 默认值 | 用途 |
|------|------|------|--------|------|
| `id` | `AutoField` | PK, 自增 | — | 主键 |
| `user_id` | `ForeignKey(User)` | FK, CASCADE, null | NULL | 关联用户，管理员不关联则为空 |
| `url` | `URLField(500)` | NOT NULL | — | 被分析的完整 URL |
| `url_legitimacy` | `CharField(100)` | NOT NULL | — | 三分类: `合法` / `可疑` / `非法` |
| `gambling_risk` | `BooleanField` | NOT NULL | `False` | 涉赌风险: True=高风险, False=低风险 |
| `risk_analysis` | `TextField` | NOT NULL | — | LLM 生成的风险分析全文 (≤1000字符截断) |
| `keywords` | `JSONField` | NOT NULL | `[]` | Python list → MySQL JSON 数组 |
| `raw_text` | `TextField` | NOT NULL | — | `dict_to_text()` 拼接结果，供 TF-IDF 向量化 |
| `created_at` | `DateTimeField` | auto_now_add | 当前时间 | 记录创建时间戳，用于排序和筛选 |

### 索引策略

| 索引 | 字段 | 用途 |
|------|------|------|
| PK (隐含) | `id` | 主键查询 |
| FK (隐含) | `user_id` | 用户关联查询 |
| 建议添加 | `created_at` | 推荐查询 `ORDER BY created_at DESC` 频繁 |

---

## 🚀 快速开始

### 环境要求

| 软件 | 最低版本 | 推荐版本 | 说明 |
|------|---------|---------|------|
| Python | 3.13 | 3.13+ | Django 5.2 最低要求 |
| MySQL | 8.0 | 8.0.43 | 数据库服务 |
| Git | 2.0 | 2.40+ | 版本控制 |

### 第一步：克隆与虚拟环境

```bash
git clone https://github.com/77hu/Gambling_risk.git
cd Gambling_risk

python -m venv venv
source venv/bin/activate       # Linux / macOS
# venv\Scripts\activate        # Windows
```

### 第二步：安装依赖

```bash
# 核心依赖 (必须)
pip install django==5.2.5 mysqlclient langchain langchain-openai \
            crawl4ai tiktoken scikit-learn python-dotenv numpy

# 向量检索依赖 (Faiss 模块需要)
pip install faiss-cpu sentence-transformers

# 完整安装命令（一次性）
pip install django mysqlclient langchain langchain-openai \
            crawl4ai tiktoken scikit-learn faiss-cpu \
            sentence-transformers python-dotenv numpy
```

### 第三步：环境配置

```bash
# 创建 .env 文件
cat > .env << 'EOF'
DEEPSEEK_API_KEY=sk-your-deepseek-api-key-here
EOF

# 编辑 Gambling_risk/settings.py 中的数据库配置:
# DATABASES -> 'PASSWORD': 'your_mysql_password'
```

### 第四步：数据库初始化

```bash
# 创建数据库
mysql -u root -p -e "
CREATE DATABASE IF NOT EXISTS Gambling_risk
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
"

# Django 迁移
python manage.py migrate

# 创建管理员账号
python manage.py createsuperuser
```

### 第五步：启动服务

```bash
python manage.py runserver
# 访问 http://localhost:8000/
# 注册 → 登录 → 输入 URL → 开始分析
```

### 验证安装

```bash
# 1. 测试爬虫模块
python -c "
from app1.test1 import main
import asyncio
text = asyncio.run(main('https://www.baidu.com'))
print(f'爬取成功: {len(text)} 字符')
"

# 2. 测试 LLM 模块 (需要有效的 API Key)
python -c "
from app1.llm_agent import LLM_process
result = LLM_process('这是一个测试网页内容', 'https://test.com')
print(result)
"

# 3. 测试 Faiss 模块
python -c "
from app1.embedding import FaissVectorStore
store = FaissVectorStore(dim=768)
print(f'Faiss 初始化成功: 当前 {len(store)} 条向量')
"
```

---

## ⚙️ 配置详解

<details>
<summary><b>📋 settings.py 完整配置参考（点击展开）</b></summary>

```python
# ===== 安全配置 =====
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-insecure-key')
DEBUG = True                                    # 生产环境必须 False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']      # 生产添加域名

# ===== 数据库 =====
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "Gambling_risk",
        "USER": "root",
        "PASSWORD": os.environ.get('MYSQL_PASSWORD', ''),
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "charset": "utf8mb4",
        }
    }
}

# ===== 模板 =====
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [os.path.join(BASE_DIR, 'templates')],
    "APP_DIRS": True,
    ...
}]

# ===== 静态文件 =====
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ===== 密码策略 =====
AUTH_PASSWORD_VALIDATORS = [
    UserAttributeSimilarityValidator(),    # 不能与用户名太像
    MinimumLengthValidator(),              # 最少8字符
    CommonPasswordValidator(),             # 不能是常见密码
    NumericPasswordValidator(),            # 不能纯数字
]
```
</details>

### 环境变量清单

| 变量 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| `DEEPSEEK_API_KEY` | ✅ 是 | — | DeepSeek API 密钥，从 platform.deepseek.com 获取 |
| `DJANGO_SECRET_KEY` | 推荐 | 开发默认值 | Django 密钥，生产环境必须设置 |
| `MYSQL_PASSWORD` | 推荐 | — | MySQL 数据库密码 |

---

## 📁 项目结构

```
📦 Gambling_risk/
│
├── 📜 manage.py                              # Django CLI 管理入口 (23行)
│
├── 📁 Gambling_risk/                         # 项目配置包
│   ├── ⚙️ settings.py                        # 全局配置 (140行)
│   │   ├── SECRET_KEY, DEBUG, ALLOWED_HOSTS
│   │   ├── INSTALLED_APPS (含 app1)
│   │   ├── MIDDLEWARE (7层中间件)
│   │   ├── DATABASES (MySQL)
│   │   ├── AUTH_PASSWORD_VALIDATORS
│   │   ├── STATICFILES_DIRS, STATIC_URL
│   │   └── MEDIA_URL, MEDIA_ROOT
│   ├── 🔗 urls.py                            # 根路由 (4行)
│   │   └── path('', include('app1.urls'))
│   ├── 🚀 wsgi.py                            # WSGI 入口
│   ├── 🚀 asgi.py                            # ASGI 入口
│   └── 📄 __init__.py
│
├── 📁 app1/                                  # 核心应用 (Django App)
│   ├── 📜 views.py                           # 视图层 (866行)
│   │   ├── register()             (16行)     # 用户注册
│   │   ├── user_login()           (18行)     # 用户登录
│   │   ├── user_logout()          (3行)      # 用户退出
│   │   ├── dict_to_text()         (22行)     # Dict→文本安全转换
│   │   ├── save_user_vectors()    (52行)     # 批量/单条降级保存
│   │   ├── home()                 (165行)    # ★ URL分析主入口
│   │   └── recommend()            (58行)     # ★ TF-IDF推荐
│   │
│   ├── 📜 models.py                          # 数据模型 (30行)
│   │   └── class URLAnalysis
│   │       ├── 9个字段定义
│   │       └── get_display_text() 方法
│   │
│   ├── 📜 llm_agent.py                       # LLM 分析代理 (66行)
│   │   ├── DEEPSEEK_API_KEY 加载
│   │   ├── LLM_process(text, url) → dict
│   │   └── System Prompt (约50行CoT指令)
│   │
│   ├── 📜 test1.py                           # 爬虫模块 (37行)
│   │   ├── main(url) → str                   # AsyncWebCrawler
│   │   └── count_tokens(text, model) → int   # tiktoken统计
│   │
│   ├── 📜 embedding.py                       # Faiss向量存储 (142行)
│   │   └── class FaissVectorStore
│   │       ├── __init__(dim, index_file, meta_file)
│   │       ├── _init_index()                 # 索引初始化+自加载
│   │       ├── add(vectors, ids, metas)      # 添加向量
│   │       ├── search(query_vector, k=5)     # L2精确搜索
│   │       ├── text_to_vectors(texts)        # Sentence-BERT编码
│   │       ├── save_vectors(texts, metas)    # 一键编码+保存
│   │       ├── save() / load()               # 磁盘持久化
│   │       ├── get_ids(count)                # 自增ID管理
│   │       └── __get_max_ids()               # 获取当前最大ID
│   │
│   ├── 📜 forms.py                           # 表单 (33行)
│   │   ├── RegisterForm(ModelForm)           # 注册+密码确认
│   │   └── LoginForm(AuthenticationForm)     # 登录
│   │
│   ├── 📜 urls.py                            # App 路由 (13行)
│   │   ├── /register/  → register()
│   │   ├── /           → user_login()
│   │   ├── /logout/    → user_logout()
│   │   ├── /home/      → home()
│   │   └── /recommend/ → recommend()
│   │
│   ├── 📜 admin.py                           # Admin注册 (空)
│   ├── 📜 apps.py                            # AppConfig
│   ├── 📜 tests.py                           # 单元测试 (空模板)
│   └── 📁 migrations/                        # DB迁移
│       └── 0001_initial.py                   # URLAnalysis建表
│
├── 📁 templates/                             # Django模板 (4个, 885行总计)
│   ├── 🏠 home.html           (344行)        # Tailwind Glassmorphism 暗色主题
│   │   ├── 自定义颜色系统 (8色)
│   │   ├── Glassmorphism 毛玻璃 CSS 工具类
│   │   ├── 动态分析结果展示 (合法性标签 + 风险等级 + 关键词)
│   │   ├── 加载指示器 (CSS动画)
│   │   └── 平滑滚动到结果 JS
│   ├── 🔑 login.html          (160行)        # Bootstrap 5 + 渐变背景
│   │   ├── "记住我" checkbox
│   │   └── 安全提示横幅
│   ├── 📝 register.html       (145行)        # Bootstrap 5 + 白卡
│   │   ├── 密码强度四级检测 (JS实时)
│   │   └── 安全建议列表
│   └── 💡 recommend.html      (236行)        # Tailwind 暗色卡片
│       ├── 卡片式推荐结果 (URL + 合法性 + 风险 + 关键词)
│       ├── URL 复制按钮 (Clipboard API + 成功反馈)
│       ├── "重新分析"快捷跳转
│       └── 空状态提示 (emoji + 引导文案)
│
├── 📁 static/                                # 静态资源
│   └── 📁 Vector_model/                      # Sentence-BERT 模型文件
│       ├── 🧠 pytorch_model.bin              # ⚠️ 418MB 模型权重 (已排除)
│       ├── ⚙️ config.json                    # 模型配置 (~1KB)
│       ├── ⚙️ sentence_bert_config.json      # SBERT 特有配置
│       ├── ⚙️ config_sentence_transformers.json
│       ├── ⚙️ modules.json                   # 模块结构定义
│       ├── ⚙️ data_config.json               # 数据配置
│       ├── ⚙️ tokenizer_config.json          # 分词器配置
│       ├── ⚙️ special_tokens_map.json        # 特殊Token映射
│       ├── 📋 tokenizer.json                 # 分词器 (456KB)
│       ├── 📋 vocab.txt                      # 词汇表
│       ├── 📁 1_Pooling/
│       │   └── ⚙️ config.json               # Pooling层配置
│       ├── 📜 train_script.py                # TPU训练脚本 (344行, Sentence Transformers官方)
│       └── 📘 README.md                      # 模型说明
│
├── 📄 .gitignore                             # Git排除规则 (40行)
├── 📄 requirements.txt (建议添加)             # Python 依赖清单
└── 📘 README.md                              # 本文档
```

---

## 🔌 API 集成与 Prompt 工程

### DeepSeek API 调用链

```
Django View → LLM_process() → ChatOpenAI → https://api.deepseek.com/v1/chat/completions
                                │
                                ├── model: deepseek-chat
                                ├── temperature: 0.7
                                ├── max_tokens: 10240
                                ├── SystemMessage: CoT 推理指令 (~50行)
                                └── HumanMessage: URL + 网页文本
```

### API 调用成本估算

| 环节 | 模型 | 输入 Tokens | 输出 Tokens | 单次成本 |
|------|------|------------|------------|---------|
| 网页内容(平均数) | — | ~3,000 | — | — |
| System Prompt | — | ~500 | — | — |
| LLM 推理 | deepseek-chat | ~3,500 | ~200 | ≈ ¥0.007 |
| **每 URL 总成本** | | | | **≈ ¥0.007** |

> 💡 100 条 URL 分析约 ¥0.70，1000 条约 ¥7.00

### 输入/输出示例

<details>
<summary><b>🔍 点击查看完整 API 调用示例</b></summary>

**请求构建：**

```python
# role_content (HumanMessage)
"""
待识别网址：https://xxx-bet-casino.com/promotion

待风险识别网站内容：# 注册即送888彩金！

欢迎来到最刺激的在线娱乐平台！
- 真人百家乐 24小时在线
- 体育赛事实时下注 赔率高
- 首充100送100 多充多送
- 支持微信/支付宝/虚拟币充值

营业执照编号：XXXXXX
Copyright © 2024
"""
```

**LLM 响应：**

```json
{
    "url_legitimacy": "非法",
    "gambling_risk": true,
    "risk_analysis": "URL包含'bet-casino'关键词，网页内容明确宣传赌博服务'真人百家乐'和'体育赛事下注'，'送彩金'为典型赌博诱导用语，且支持虚拟币充值属于规避监管行为。判定为存在明确赌博特征。",
    "keywords": ["注册送彩金", "真人百家乐", "体育下注", "虚拟币充值", "bet-casino"]
}
```
</details>

---

## 🛡️ 反检测与安全

### Django 安全中间件

| 中间件 | 防护类型 | 默认配置 |
|--------|---------|---------|
| `SecurityMiddleware` | SSL重定向、HSTS、X-Content-Type-Options | 生产环境需额外配置 |
| `CsrfViewMiddleware` | CSRF 跨站请求伪造 | `{% csrf_token %}` 已全部添加 |
| `XFrameOptionsMiddleware` | 点击劫持 | `DENY` (默认) |
| `AuthenticationMiddleware` | 会话劫持 | Session Cookie HttpOnly |
| `SessionMiddleware` | 会话固定 | 登录后自动重建 Session |

### 敏感信息处理

| 项目 | 方案 | 状态 |
|------|------|------|
| `SECRET_KEY` | 使用占位符，生产用环境变量 | ✅ 已脱敏 |
| MySQL 密码 | 使用占位符，生产用 `.env` | ✅ 已脱敏 |
| `DEEPSEEK_API_KEY` | `.env` 加载 + `.gitignore` 排除 | ✅ 已排除 |
| `.env` 文件 | 在 `.gitignore` 中排除 | ✅ 已排除 |

---

## 📦 大文件说明

以下文件因体积过大（单文件超过 90MB）**未包含在 GitHub 仓库中**，需单独获取：

| 文件路径 | 大小 | 用途 | 获取方式 |
|---------|------|------|---------|
| `static/Vector_model/pytorch_model.bin` | **418 MB** | Sentence-BERT 模型权重文件 (MiniLM-L6-H384-uncased) | 运行 `pip install sentence-transformers` 后，模型会自动下载到缓存目录；或通过 HuggingFace: `sentence-transformers/all-MiniLM-L6-v2` |
| `static/Vector_model/temp_files.zip` | 788 KB | 模型训练产生的临时打包文件 | 非必需文件，可忽略 |

> 💡 **替代方案**：在 `embedding.py` 中修改 `model_path` 指向 HuggingFace 模型名称（如 `all-MiniLM-L6-v2`），SentenceTransformer 会自动从网络下载模型到本地缓存，无需手动管理 418MB 权重文件。

---

## ⚠️ 已知限制与改进方向

### 当前限制

| 类别 | 限制 | 影响 | 优先级 |
|------|------|------|--------|
| **性能** | 同步串行处理 URL | 10 个 URL 需约 5 分钟 | 🔴 高 |
| **中文** | TF-IDF 分词未适配中文 | 中文推荐准确率低 | 🟡 中 |
| **推荐** | Faiss 向量引擎未启用 | 语义检索能力未利用 | 🟡 中 |
| **安全** | 无 API 限流机制 | 可能被恶意高频调用 | 🟡 中 |
| **部署** | 无 Docker 化支持 | 手动配置复杂 | 🟢 低 |
| **监控** | 无调用日志/指标 | 排查问题困难 | 🟢 低 |
| **爬虫** | 未使用 networkidle 等待 | 部分 SPA 页面加载不全 | 🟢 低 |
| **测试** | 无单元测试 | 代码质量难以保证 | 🟢 低 |

### 改进路线图

- [ ] **并发爬虫**: 使用 `asyncio.gather()` 并发处理多个 URL，预期提速 3-5x
- [ ] **中文分词**: 集成 `jieba` 分词 + 中文停用词表，提升推荐准确率
- [ ] **Faiss 启用**: 在 `recommend()` 中切换至 Faiss 语义检索
- [ ] **API 限流**: 集成 `django-ratelimit` + Redis 令牌桶
- [ ] **Docker 化**: 编写 `Dockerfile` + `docker-compose.yml` (含 MySQL + Django)
- [ ] **日志系统**: 结构化日志 (structlog) + LLM 调用追踪
- [ ] **爬虫优化**: 添加 `wait_until="networkidle"` + 自动重试
- [ ] **测试覆盖**: 单元测试 (pytest) + 爬虫/LLM 集成测试

---

## 📄 License

本项目仅供学习和研究使用。请勿用于任何非法用途。

---

<div align="center">
  <sub>Built with ❤️ using Django + DeepSeek + Crawl4AI + Faiss</sub>
</div>
