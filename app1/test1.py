import asyncio
from crawl4ai import *


import tiktoken
from .llm_agent import LLM_process
async def main(url):
    async with AsyncWebCrawler() as crawler:

        result = await crawler.arun(
            url=url,
            # 启用 JS 渲染（默认开启）
            # js_code=[
            #     "window.scrollTo(0, document.body.scrollHeight);",
            #     "await new Promise(r => setTimeout(r, 2000));"  # 等待加载
            # ],
            # # 或使用内置 magic 模式（实验性）
            # magic=True,  # 自动滚动 + 等待动态内容
            # wait_until="networkidle"  # 等待网络空闲
            
        )
        # print(result.markdown)
        return result.markdown

#统计tokens
def count_tokens(text: str, model: str = "gpt-4") -> int:
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)


if __name__ == "__main__":
    url="https://m.sporttery.cn/?ref=migs&back=true"
    text = asyncio.run(main(url))# 使用示例
    LLM_process(text,url)
    
    # print(count_tokens(text, "gpt-4"))        # GPT-4 / GPT-4o
    # print(count_tokens(text, "gpt-3.5-turbo"))  # GPT-3.5