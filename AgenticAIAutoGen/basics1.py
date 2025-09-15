import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='deepseek-r1:14b')

    # 创建 AssistantAgent 实例
    assistant = AssistantAgent(name='assistant', model_client=ollama_model_client)
    await Console(assistant.run_stream(task="25*8等于多少？"))

    # 关闭 ollama 模型客户端
    await ollama_model_client.close()

asyncio.run(main())