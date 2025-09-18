import asyncio
import json

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen2.5vl:latest')

    # 创建第一个智能体
    agent1 = AssistantAgent(name='Helper', model_client=ollama_model_client)

    # 创建第二个智能体
    agent2 = AssistantAgent(name='BackupHelper', model_client=ollama_model_client)

    await Console(agent1.run_stream(task="我最喜欢的颜色是蓝色。"))

    # 保存状态
    state = await agent1.save_state()
    with open('memory.json', 'w', encoding='utf-8') as f:
        json.dump(state, f)

    # 加载状态
    with open('memory.json', 'r', encoding='utf-8') as f:
        save_state = json.load(f)
    await agent2.load_state(save_state)

    await Console(agent2.run_stream(task="我最喜欢的颜色是什么？"))

    await ollama_model_client.close()


asyncio.run(main())
