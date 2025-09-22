import asyncio

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

    # 创建第一个智能体（老师）
    assistant = AssistantAgent(
        name='MathTutor',
        model_client=ollama_model_client,
        system_message="你是一位乐于助人的数学辅导老师，请帮助用户一步一步解决数学问题。"
        "当用户说 '已完成' 或类似语句表示结束时,予以确认并回复 '课程完成' 以结束会话。"
    )

    # 创建第二个智能体（学生用户）
    user_proxy = UserProxyAgent(
        name='Student',
    )

    team = RoundRobinGroupChat(
        participants=[assistant, user_proxy],
        termination_condition=TextMentionTermination("课程完成"),
    )

    await Console(team.run_stream(task="我需要帮助解决代数问题，你能帮我解答 2*4+5 的结果吗？"))

    await ollama_model_client.close()

asyncio.run(main())