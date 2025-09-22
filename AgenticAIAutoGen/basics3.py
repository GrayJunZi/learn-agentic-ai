import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

    # 创建第一个智能体（老师）
    agent1 = AssistantAgent(
        name='MathTeacher',
        model_client=ollama_model_client,
        system_message="你是一名数学老师，要清晰地解释概念并提出问题。"
    )

    # 创建第二个智能体（学生）
    agent2 = AssistantAgent(
        name='Student',
        model_client=ollama_model_client,
        system_message="你是一名好奇的学生。请提出问题，并展示你的思考过程。"
    )

    team = RoundRobinGroupChat(
        participants=[agent1, agent2],
        termination_condition=MaxMessageTermination(max_messages=6),
    )

    await Console(team.run_stream(task="让我们讨论一下什么是乘法以及它是如何运作的。"))

    await ollama_model_client.close()

asyncio.run(main())