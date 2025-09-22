import asyncio

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='deepseek-r1:14b')

    web_surfer_agent = MultimodalWebSurfer(
        name="WebSurfer",
        model_client=ollama_model_client,
        headless=False,
        animate_actions=True,
    )

    team = RoundRobinGroupChat(
        participants=[web_surfer_agent],
        max_turns=3
    )

    await Console(team.run_stream(task="导航到必应中搜索 'AutoGen 框架 Python' 然后总结你找到的内容。"))

    await web_surfer_agent.close()

    # 关闭 ollama 模型客户端 实例
    await ollama_model_client.close()

asyncio.run(main())
