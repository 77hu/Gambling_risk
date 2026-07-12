
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import json
load_dotenv()
# 请将你的 DeepSeek API Key 填在这里，或通过环境变量 DEEPSEEK_API_KEY 设置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "YOUR_DEEPSEEK_API_KEY_HERE")

def LLM_process(text,url):

    # 初始化 DeepSeek 模型（使用 DeepSeek-V2-Chat，支持 128K 上下文）
    llm = ChatOpenAI(
        model="deepseek-chat",                # DeepSeek 官方模型名
        api_key=DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com",  # DeepSeek API 地址
        temperature=0.7,
        max_tokens=1024*10,
    )
    role_content=f"""待识别网址：{url}\n
                    待风险识别网站内容：{text}
                    """
    #CoT思维链
    system_content = """你是一位资深网络安全风险评估专家，专注于识别网络内容中的非法或高风险行为，尤其是网络赌博相关活动。你的任务是基于提供的网址（URL）和网页文本内容，严格按照以下 Chain-of-Thought（思维链）步骤进行分析，并输出结构化结论。
                    请按以下三步逐步推理：

                    ### 步骤 1：分析网址（URL）
                    - 检查 URL 是否包含可疑关键词（如“bet”、“casino”、“win”、“lotto”、“gamble”、“poker”、“sportsbook”等）；
                    - 判断域名是否为已知赌博平台、短链接、仿冒域名或异常子域名；
                    - 评估 URL 结构是否符合正规网站特征（如使用 HTTPS、有明确机构归属等）。

                    ### 步骤 2：分析网页内容
                    - 识别文本中是否包含赌博相关术语、诱导性语言（如“稳赢”、“高赔率”、“注册送彩金”、“真人娱乐”等）；
                    - 检查是否存在虚拟货币投注、体育赛事下注、棋牌游戏变现、彩票预测等典型赌博行为描述；
                    - 注意是否存在规避监管的隐晦表达（如用“娱乐”代指赌博、“积分兑换”实为现金交易等）；
                    - 若内容为正常新闻、科普、法律声明或反赌宣传，则不应判定为赌博。

                    ### 步骤 3：综合判断与输出
                    - 仅当 URL 或内容中存在**明确、可验证的赌博特征**时，才判定为“存在赌博嫌疑”；
                    - 若证据不足或内容中性，请明确说明“未发现赌博嫌疑”；
                    - 输出必须严格遵循以下 JSON 格式（不要包含任何额外解释或 Markdown）：

                    {
                    "url_legitimacy": "合法" 或 "可疑" 或 "非法"
                    "gambling_risk": true 或 false
                    "risk_analysis": "简明扼要的推理过程（100字以内）"
                    "keywords": "关键词1", "关键词2", ...
                    }
                    注意：请勿臆测，所有结论必须基于提供的 URL 和文本内容。若内容为空或无法判断，请将 gambling_risk 设为 false，并说明原因。
                    """
    # 构造对话消息
    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=role_content)
    ]

    # 调用模型
    response = llm.invoke(messages)

    # 输出结果
    # print("🤖 DeepSeek 回答：")
    # print(response.content)
    final_data = json.loads(response.content)
    return final_data
