import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen2.5vl:latest')

    assistant = AssistantAgent(name='MultiModalAssistant', model_client=ollama_model_client)

    image = Image.from_file("C:\\Users\\Byrne.LAPTOP-FJ476S4Q\\Pictures\\Screenshots\\Screenshot 2025-09-12 093057.png")

    multimodal_message = MultiModalMessage(
        content=["你在这张图片中看到了什么？", image],
        source="user",
    )

    await Console(assistant.run_stream(task=multimodal_message))
    await ollama_model_client.close()

asyncio.run(main())