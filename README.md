# URLGuard - 基于 LLM 的涉赌风险 URL 智能分析平台

> 结合 Web 爬虫 + 大语言模型 + 向量检索的 URL 安全风险评估系统

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.5-green.svg)](https://www.djangoproject.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)](https://python.langchain.com/)
[![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek--V2-purple.svg)](https://www.deepseek.com/)
[![Crawl4AI](https://img.shields.io/badge/Crawler-Crawl4AI-red.svg)](https://github.com/unclecode/crawl4ai)

---

## 📋 目录

- [项目概述](#-项目概述)
- [系统架构](#-系统架构)
- [核心功能](#-核心功能)
- [技术栈](#-技术栈)
- [快速开始](#-快速开始)
- [项目结构](#-项目结构)
- [工作流程](#-工作流程)
- [分析效果展示](#-分析效果展示)
- [推荐系统](#-推荐系统)
- [数据库设计](#-数据库设计)
- [API 集成](#-api-集成)
- [安全建议](#-安全建议)
- [已知限制](#-已知限制)
- [License](#-license)

---

## 📖 项目概述

**URLGuard** 是一个基于大语言模型（LLM）的 URL 安全风险评估平台，专注于识别网络赌博等高风险内容。系统通过以下步骤完成分析：

1. **智能爬虫**：使用 Crawl4AI 抓取目标网页内容（支持 JS 渲染）
2. **LLM 深度分析**：调用 DeepSeek 大模型，通过 CoT 思维链进行多维度风险评估
3. **结果持久化**：将分析结果存储到 MySQL 数据库
4. **智能推荐**：基于 TF-IDF + 余弦相似度实现历史分析记录的内容推荐

### 应用场景

| 场景 | 说明 |
|------|------|
| 网络赌博检测 | 识别在线博彩、棋牌变现、虚拟货币投注等 |
| URL 合法性验证 | 判断域名是否为钓鱼网站、仿冒域名 |
| 批量安全审计 | 支持多 URL 同时分析，高效处理大量链接 |
| 风险内容推荐 | 基于历史分析记录，推荐相似风险内容 |

---

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────────────┐
│                        用户浏览器                                │
│                    Tailwind CSS 前端界面                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │ HTTP POST / GET
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Django 5.2.5 Web 服务                        │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  views.py    │  │  models.py   │  │  embedding.py        │  │
│  │  (视图层)     │  │  (数据模型)   │  │  (Faiss向量存储)      │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
│         │                 │                      │              │
│         ▼                 ▼                      ▼              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    核心分析管线                            │  │
│  │                                                          │  │
│  │  test1.py (爬虫)  ──→  llm_agent.py (LLM分析)           │  │
│  │  AsyncWebCrawler       Chain-of-Thought Prompt           │  │
│  │  ↓                     ↓                                  │  │
│  │  网页Markdown内容      JSON结构化结果                      │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
     ┌────────────────┐      ┌─────────────────┐
     │  MySQL 数据库   │      │  DeepSeek API   │
     │  (分析记录)     │      │  (LLM推理)       │
     └────────────────┘      └─────────────────┘
```

---

## ✨ 核心功能

### 1. URL 批量安全分析

- 支持每行一个 URL 批量输入
- 自动爬虫抓取网页内容（支持 JavaScript 动态渲染页面）
- LLM 多维度分析：URL 合法性 + 赌博风险 + 关键词提取 + 风险分析

### 2. CoT 思维链风险评估

系统使用 Chain-of-Thought 提示工程，引导 LLM 按三步推理：

```
步骤 1: 分析 URL 结构（关键词、域名、HTTPS、子域名等）
   ↓
步骤 2: 分析网页内容（赌博术语、诱导语言、隐晦表达等）
   ↓
步骤 3: 综合判断输出结构化 JSON 结果
```

### 3. 智能推荐系统

- 基于 **TF-IDF** 向量化 + **余弦相似度** 计算
- 输入关键词，推荐最相似的历史分析记录
- 支持从分析结果页直接跳转"猜你想了解"

### 4. 用户系统

- 注册 / 登录 / 退出
- 分析记录关联到用户
- 需要登录才能使用分析功能（`@login_required`）

---

## 🔧 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| **Web 框架** | Django 5.2.5 | MTV 架构，用户认证，ORM |
| **前端** | Tailwind CSS + Font Awesome | Glassmorphism 设计风格，响应式布局 |
| **爬虫** | Crawl4AI | 异步 Web 爬虫，JS 渲染支持 |
| **LLM** | DeepSeek-V2-Chat (via LangChain) | 128K 上下文，CoT 思维链 |
| **推荐** | TF-IDF + Cosine Similarity | scikit-learn 文本向量化 |
| **向量库** | Faiss (可选) | Facebook AI 向量搜索引擎 |
| **数据库** | MySQL 8.0 | 分析记录持久化 |
| **分词** | tiktoken | GPT-4 / GPT-3.5 Token 计数 |

---

## 🚀 快速开始

### 1. 环境要求

- Python 3.13+
- MySQL 8.0+
- DeepSeek API Key

### 2. 安装依赖

```bash
pip install django mysqlclient langchain langchain-openai crawl4ai tiktoken scikit-learn faiss-cpu python-dotenv numpy
```

### 3. 配置

```bash
# 复制 .env 示例
cp .env.example .env

# 编辑 .env 文件，填入你的 API Key
echo "DEEPSEEK_API_KEY=sk-your-key-here" > .env
```

### 4. 数据库设置

在 `Gambling_risk/settings.py` 中配置 MySQL：

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "Gambling_risk",    # 数据库名
        "USER": "root",             # 用户名
        "PASSWORD": "your_password", # 密码
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

创建数据库并迁移：

```bash
mysql -u root -p -e "CREATE DATABASE Gambling_risk CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
python manage.py migrate
python manage.py createsuperuser  # 创建管理员账号
```

### 5. 启动服务

```bash
python manage.py runserver
```

访问 `http://localhost:8000/` 即可使用。

---

## 📁 项目结构

```
Gambling_risk/
├── manage.py                          # Django 管理入口
├── Gambling_risk/                     # 项目配置
│   ├── settings.py                    # 全局配置（数据库/静态文件/中间件）
│   ├── urls.py                        # 根 URL 路由
│   ├── wsgi.py / asgi.py              # WSGI/ASGI 入口
│   └── __init__.py
├── app1/                              # 核心应用
│   ├── views.py                       # 视图层（注册/登录/分析/推荐）
│   ├── models.py                      # 数据模型（URLAnalysis）
│   ├── llm_agent.py                   # LLM 分析代理（CoT 思维链）
│   ├── test1.py                       # 爬虫模块（Crawl4AI）
│   ├── embedding.py                   # Faiss 向量存储
│   ├── forms.py                       # 表单（注册/登录）
│   ├── admin.py                       # 管理后台
│   └── migrations/                    # 数据库迁移
├── templates/                         # HTML 模板
│   ├── home.html                      # 首页（URL 输入 + 分析结果）
│   ├── login.html                     # 登录页
│   ├── register.html                  # 注册页
│   └── recommend.html                 # 推荐页
├── static/                            # 静态资源
│   ├── Faiss_vector_databases/        # Faiss 向量索引
│   └── Vector_model/                  # Sentence-Transformer 模型
└── .env                               # 环境变量（API Key）
```

---

## 🔄 工作流程

```
用户输入 URL(s)
    │
    ▼
┌─────────────────────────────────┐
│  Step 1: 爬虫抓取 (test1.py)     │
│  AsyncWebCrawler.arun(url)       │
│  返回: 网页 Markdown 文本         │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Step 2: LLM 分析 (llm_agent.py) │
│  DeepSeek-V2-Chat               │
│  CoT 三步推理 → JSON 结果        │
│  {url_legitimacy, gambling_risk, │
│   risk_analysis, keywords}       │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Step 3: 保存记录 (views.py)     │
│  URLAnalysis.objects.bulk_create │
│  存储到 MySQL 数据库             │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Step 4: 展示结果 (home.html)    │
│  合法性标签 + 风险等级 + 关键词   │
│  + 风险分析文本                  │
└─────────────────────────────────┘
```

---

## 📊 分析效果展示

### 分析结果卡片示例

| URL | 合法性 | 赌博风险 | 关键词 |
|-----|--------|---------|--------|
| `example.com` | 🟢 合法 | ✅ 低风险 | — |
| `xxx-casino.com` | 🔴 非法 | ⚠️ 高风险 | "注册送彩金", "真人娱乐", "高赔率" |
| `bet-sports.xyz` | 🟡 可疑 | ⚠️ 高风险 | "sportsbook", "稳赢", "虚拟币投注" |

### 风险等级可视化

```
低风险 (未检测到赌博内容)
████████████████████████████████ 100%

中风险 (发现可疑关键词)
████████████████░░░░░░░░░░░░░░░░  53%

高风险 (明确赌博特征)
████████████████████████████████ 100%
⚠️ 包含"注册送彩金"、"真人娱乐"等典型赌博诱导用语
```

### 推荐系统效果

```
用户查询: "注册送彩金 真人娱乐"

推荐结果 (Top-6):
1. xxx-casino.com    ████████████████████████ 相似度 0.87
2. bet-entertain.xyz ██████████████████░░░░░░ 相似度 0.71
3. poker-room.cc     ██████████████░░░░░░░░░░ 相似度 0.56
4. lottery-pred.cn   ████████████░░░░░░░░░░░░ 相似度 0.48
5. game-platform.io  ████████░░░░░░░░░░░░░░░░ 相似度 0.33
6. news-article.com  ████░░░░░░░░░░░░░░░░░░░░ 相似度 0.17
```

---

## 🎯 推荐系统

系统采用 **TF-IDF + 余弦相似度** 实现内容推荐：

### 算法流程

```
1. 从数据库获取最近 100 条分析记录
2. 提取 raw_text 字段（拼接 URL + 合法性 + 风险分析 + 关键词）
3. 使用 TfidfVectorizer 构建词频-逆文档频率矩阵
   - max_features: 5000
   - ngram_range: (1, 2) 支持二元词组
4. 将查询文本向量化
5. 计算余弦相似度，返回 Top-6 最相似记录
6. 过滤相似度 < 0.01 的低质量结果
```

### 参数配置

```python
vectorizer = TfidfVectorizer(
    max_features=5000,        # 最大特征数
    stop_words='english',     # 停用词过滤
    ngram_range=(1, 2),       # 一元 + 二元词组
    lowercase=True,           # 小写化
    token_pattern=r'(?u)\b\w+\b'
)
```

---

## 🗃️ 数据库设计

### URLAnalysis 表

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | AutoField | 主键 |
| `user` | ForeignKey → User | 关联用户（可空） |
| `url` | URLField(500) | 被分析的 URL |
| `url_legitimacy` | CharField(100) | 合法性：合法 / 可疑 / 非法 |
| `gambling_risk` | BooleanField | 是否存在赌博风险 |
| `risk_analysis` | TextField | LLM 生成的风险分析文本 |
| `keywords` | JSONField | 提取的关键词列表 |
| `raw_text` | TextField | 拼接后的原始文本（用于 TF-IDF） |
| `created_at` | DateTimeField | 分析时间 |

```python
class URLAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(max_length=500)
    url_legitimacy = models.CharField(max_length=100)
    gambling_risk = models.BooleanField(default=False)
    risk_analysis = models.TextField()
    keywords = models.JSONField(default=list)
    raw_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## 🔌 API 集成

### DeepSeek LLM 配置

```python
llm = ChatOpenAI(
    model="deepseek-chat",           # DeepSeek 官方模型名
    api_key=DEEPSEEK_API_KEY,        # API Key（通过 .env 配置）
    base_url="https://api.deepseek.com",
    temperature=0.7,                 # 创造性
    max_tokens=10240,                # 最大输出长度
)
```

### System Prompt 结构

系统使用 CoT 思维链提示词，包含三个分析步骤：

1. **URL 分析**：检查域名结构、关键词（bet/casino/poker 等）
2. **内容分析**：识别赌博术语、诱导语言、隐晦表达
3. **综合判断**：输出结构化 JSON（合法性 + 风险 + 关键词 + 分析）

---

## 🔒 安全建议

| 项目 | 当前状态 | 建议 |
|------|---------|------|
| `SECRET_KEY` | 已脱敏 | 生产环境使用环境变量 |
| MySQL 密码 | 已脱敏 | 使用 `.env` 或密钥管理服务 |
| DeepSeek API Key | 已脱敏 | 不要提交到版本控制 |
| `DEBUG = True` | 开发模式 | 生产环境设为 `False` |
| `ALLOWED_HOSTS` | 空列表 | 配置允许的域名 |
| CSRF 保护 | 已启用 | 保持 `@csrf_protect` |

### `.gitignore` 推荐

```gitignore
# 敏感文件
.env
*.key
*.pem

# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/

# IDE
.idea/
.vscode/

# 数据库
*.sqlite3

# 大文件
static/Vector_model/model.safetensors
static/Vector_model/.git
static/Faiss_vector_databases/*.index

# 媒体文件
media/
```

---

## ⚠️ 已知限制

| 限制 | 说明 |
|------|------|
| 爬虫 JS 渲染 | Crawl4AI 默认开启 JS，但部分动态内容可能需要额外等待 |
| LLM 成本 | 每次分析调用 DeepSeek API，大量分析会产生费用 |
| 推荐系统语言 | TF-IDF 默认英文分词，中文内容需额外配置 jieba |
| 并发处理 | 当前为同步串行处理多个 URL，可优化为并发 |
| Faiss 集成 | 向量存储功能已实现但未在推荐中启用（使用 TF-IDF 替代） |

---

## 📄 License

本项目仅供学习和研究使用。

---

## 📞 联系

如有问题或建议，请提交 [Issue](https://github.com/77hu/Gambling_risk/issues) 或 [Pull Request](https://github.com/77hu/Gambling_risk/pulls)。
