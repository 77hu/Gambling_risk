<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://python.langchain.com/)
[![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek_V2-536DFE?style=for-the-badge&logo=deepin&logoColor=white)](https://www.deepseek.com/)
[![Crawl4AI](https://img.shields.io/badge/Crawler-Crawl4AI-FF6B35?style=for-the-badge&logo=webdriver&logoColor=white)](https://github.com/unclecode/crawl4ai)

</div>

<br/>

<h1 align="center">🛡️ URLGuard</h1>

<h3 align="center"><em>LLM 驱动的 URL 涉赌风险智能分析平台 · CoT 思维链风险评估 · TF-IDF 内容推荐</em></h3>

<br/>

---

## 📑 目录

- [✨ 项目亮点](#-项目亮点)
- [🏗️ 系统架构](#️-系统架构)
- [🧩 核心功能](#-核心功能)
- [🚀 快速开始](#-快速开始)
- [📁 项目结构](#-项目结构)
- [🗃️ 数据库设计](#️-数据库设计)
- [🔌 API 集成](#-api-集成)
- [🔒 安全建议](#-安全建议)
- [⚠️ 已知限制](#️-已知限制)

---

## ✨ 项目亮点

<table>
<tr>
<td width="50%">

### 🧠 CoT 思维链风险评估

基于 **Chain-of-Thought** 提示工程，引导 LLM 按三步推理：URL 结构分析 → 网页内容分析 → 综合判断。输出结构化 JSON 结果（合法性 + 风险等级 + 关键词 + 分析文本）。

> *大模型深度理解赌博术语、诱导语言与隐晦表达，告别简单关键词匹配。*

</td>
<td width="50%">

### 🔍 智能爬虫引擎

集成 **Crawl4AI** 异步 Web 爬虫，支持 JavaScript 动态渲染页面。自动抓取目标网页 Markdown 内容，为 LLM 分析提供高质量上下文。

> *支持现代 SPA 页面，覆盖传统爬虫无法获取的动态内容。*

</td>
</tr>
<tr>
<td width="50%">

### 📊 智能推荐系统

基于 **TF-IDF + 余弦相似度** 的内容推荐引擎。从历史分析记录中检索最相似的 6 条结果，支持"猜你想了解"一键跳转。

> *5000 维特征空间，ngram (1,2) 增强语义理解。*

</td>
<td width="50%">

### 👤 用户认证体系

完整的注册 / 登录 / 退出系统，分析记录关联用户。`@login_required` 保护所有分析功能，支持分析历史追溯。

> *Django MTV 架构，session-based 认证。*

</td>
</tr>
</table>

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
│                     Django 5.2 Web 服务                          │
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
│  │  AsyncWebCrawler       DeepSeek CoT Prompt                │  │
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

## 🧩 核心功能

### 1. URL 批量安全分析

| 特性 | 实现 |
|---|---|
| 输入方式 | 多 URL 批量输入（每行一个） |
| 爬虫 | Crawl4AI 异步抓取 + JS 渲染 |
| LLM 分析 | URL 合法性 + 赌博风险 + 关键词 + 风险分析 |
| 结果展示 | Glassmorphism 风格卡片，合法性标签 + 风险等级 |

### 2. CoT 思维链评估流程

```
步骤 1: 分析 URL 结构（关键词、域名、HTTPS、子域名等）
   ↓
步骤 2: 分析网页内容（赌博术语、诱导语言、隐晦表达等）
   ↓
步骤 3: 综合判断输出结构化 JSON 结果
```

### 3. 智能推荐引擎

| 算法环节 | 技术选型 |
|---|---|
| 文本向量化 | TF-IDF (max_features=5000) |
| 特征增强 | ngram_range (1, 2) 二元词组 |
| 相似度计算 | Cosine Similarity |
| 结果数量 | Top-6 推荐 + 低质量过滤 (score < 0.01) |

---

## 🚀 快速开始

### 环境要求

| 依赖 | 版本要求 |
|---|---|
| Python | ≥ 3.13 |
| MySQL | ≥ 8.0 |
| DeepSeek API Key | — |

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/77hu/Gambling_risk.git
cd Gambling_risk

# 2. 安装依赖
pip install django mysqlclient langchain langchain-openai crawl4ai tiktoken scikit-learn faiss-cpu python-dotenv numpy

# 3. 配置环境变量
export DEEPSEEK_API_KEY="your-api-key-here"

# 4. 数据库迁移
mysql -u root -p -e "CREATE DATABASE Gambling_risk CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
python manage.py migrate
python manage.py createsuperuser

# 5. 启动服务
python manage.py runserver
```

---

## 📁 项目结构

```
📦 Gambling_risk/
├── 📜 manage.py                          # Django 管理入口
├── 📁 Gambling_risk/                     # 项目配置
│   ├── ⚙️ settings.py                    # 全局配置（数据库/静态文件/中间件）
│   ├── 🔗 urls.py                        # 根 URL 路由
│   └── 🚀 wsgi.py / asgi.py              # WSGI/ASGI 入口
├── 📁 app1/                              # 核心应用
│   ├── 📜 views.py                       # 视图层（注册/登录/分析/推荐）
│   ├── 📜 models.py                      # 数据模型（URLAnalysis）
│   ├── 📜 llm_agent.py                   # LLM 分析代理（CoT 思维链）
│   ├── 📜 test1.py                       # 爬虫模块（Crawl4AI）
│   ├── 📜 embedding.py                   # Faiss 向量存储
│   └── 📜 forms.py                       # 表单（注册/登录）
├── 📁 templates/                         # HTML 模板
│   ├── 🏠 home.html                      # 首页（URL 输入 + 分析结果）
│   ├── 🔑 login.html                     # 登录页
│   ├── 📝 register.html                  # 注册页
│   └── 💡 recommend.html                 # 推荐页
├── 📁 static/                            # 静态资源
│   └── 📁 Vector_model/                  # Sentence-Transformer 模型
└── 📘 README.md                          # 本文档
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
| `risk_analysis` | TextField | LLM 风险分析文本 |
| `keywords` | JSONField | 提取的关键词列表 |
| `raw_text` | TextField | 拼接文本（用于 TF-IDF） |
| `created_at` | DateTimeField | 分析时间（自动） |

---

## 🔌 API 集成

### DeepSeek LLM 配置

```python
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=DEEPSEEK_API_KEY,        # 通过环境变量配置
    base_url="https://api.deepseek.com",
    temperature=0.7,
    max_tokens=10240,
)
```

### CoT System Prompt 结构

1. **URL 分析**：检查域名结构、关键词（bet/casino/poker 等）
2. **内容分析**：识别赌博术语、诱导语言、隐晦表达
3. **综合判断**：输出结构化 JSON（合法性 + 风险 + 关键词 + 分析）

---

## 🔒 安全建议

| 配置项 | 当前状态 | 生产建议 |
|--------|---------|----------|
| `SECRET_KEY` | 已脱敏 | 使用环境变量 |
| MySQL 密码 | 已脱敏 | 使用 `.env` 或密钥管理服务 |
| DeepSeek API Key | 已脱敏 | 不要提交到版本控制 |
| `DEBUG` | `True`（开发） | 生产设为 `False` |
| `ALLOWED_HOSTS` | `[]` | 配置允许的域名 |
| CSRF 保护 | 已启用 | 保持 `@csrf_protect` |

---

## ⚠️ 已知限制

| 限制 | 说明 |
|------|------|
| 爬虫 JS 渲染 | 部分动态内容可能需要额外等待时间 |
| LLM 成本 | 每次分析调用 API，大量分析会产生费用 |
| 推荐系统语言 | TF-IDF 默认英文分词，中文内容需配置 jieba |
| 并发处理 | 当前为同步串行处理，可优化为异步并发 |
| Faiss 集成 | 向量存储功能已实现但未在推荐中启用 |

---

## 📄 License

本项目仅供学习和研究使用。
