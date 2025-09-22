import asyncio

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench

async def main():
    # 文件系统MCP服务参数
    filesystem_server_params = StdioServerParams(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "..\\AgenticAIAutoGen",
        ],
        read_timeout_seconds=60
    )

    # 创建 MCP 实例
    fs_workbench = McpWorkbench(filesystem_server_params)

    async with fs_workbench as fs_wb:
        # 创建 ollama 模型客户端 实例
        ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

        assistant = AssistantAgent(
            name='MathTutor',
            model_client=ollama_model_client,
            workbench=fs_wb,
            system_message="你是一位乐于助人的数学辅导老师。请帮助用户一步一步解决数学问题，你需要能够访问文件系统。"
                           "当用户说出“谢谢，已完成”或类似话语时，请予以回应，并说出“课程结束”来结束本次会话。"
        )

        user_proxy = UserProxyAgent(name="Student")

        team = RoundRobinGroupChat(
            participants=[user_proxy, assistant],
            termination_condition=TextMentionTermination('课程完成')
        )

        await Console(team.run_stream(task="我需要解决代数问题，你可以自由创建文件来帮助学生学习。"))

    # 关闭 ollama 模型客户端 实例
    await ollama_model_client.close()

asyncio.run(main())