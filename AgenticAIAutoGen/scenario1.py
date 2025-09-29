import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

    # Plane 系统 MCP 服务参数
    plane_server_params = StdioServerParams(
        command="npx",
        args=[
            "-y",
            "@makeplane/plane-mcp-server",
        ],
        env={
            "PLANE_API_KEY": "plane_api_69a495b3631d46a2b0b45a79d28926ab",
            "PLANE_API_HOST_URL": "http://localhost",
            "PLANE_WORKSPACE_SLUG": "plane",
        },
    )

    # 创建 Plane 系统 MCP 实例
    plane_workbench = McpWorkbench(plane_server_params)

    # Playwright 系统 MCP 服务参数
    playwright_server_params = StdioServerParams(
        command="npx",
        args=[
            "@playwright/mcp@latest",
        ]
    )

    # 创建 Playwright 系统 MCP 实例
    playwright_workbench = McpWorkbench(playwright_server_params)

    async with plane_workbench as plane_wb, playwright_workbench as playwright_wb:
        # 创建 Plane 智能体
        bug_analyst = AssistantAgent(
            name='BugAnalyst',
            model_client=ollama_model_client,
            workbench=plane_wb,
            system_message=
            """
            你是一名专注于 Plane 缺陷分析的缺陷分析师。
            
            你的任务如下：  
            **目标**：分析缺陷并创建全面的测试场景。
            
            1. 从 Plane 中检索并审查 **CreditCardBanking**项目中**最近的 5 个缺陷**。  
            2. 仔细阅读这些缺陷的描述，识别其中的**重复性问题或常见模式**。  
            3. 基于识别出的模式，设计一个**详细的用户操作流程**，覆盖应用程序的核心功能，并可作为一套可靠的**冒烟测试场景**。
            
            在设计冒烟测试时，请务必具体明确：  
            - 提供清晰、逐步的手动测试说明。  
            - 包含需访问的**确切 URL 或页面路径**。  
            - 描述**用户操作**（如点击、表单输入、提交等）。  
            - 明确说明每个步骤的**预期结果或验证点**。
            
            如果在最近的 Plane 查询中**未发现任何缺陷**，请尝试重新查询，或明确注明此情况。
            
            完成分析和场景设计后：  
            - 清晰地输出最终的冒烟测试步骤。  
            - 最后，写出：**“HANDOFF TO AUTOMATION”**，以表示你的分析工作已完成。
            
            感谢你详尽的分析！
            """
        )

        # 创建 Playwright 智能体
        automation_analyst = AssistantAgent(
            name='AutomationAnalyst',
            model_client=ollama_model_client,
            workbench=playwright_wb,
            system_message=
            """
            你是 Playwright 自动化专家。请根据 BugAnalyst 提供的用户操作流程，
            将其转换为可执行的 Playwright 命令。使用 Playwright MCP 工具执行冒烟测试。
            逐步执行自动化测试，并清晰报告结果，包括任何错误或成功信息。
            在关键节点截取屏幕截图，以记录测试执行过程。
            
            确保在你的测试流程中验证 Bug 中描述的预期结果。
            
            重要提示：使用 browser_wait_for 等待成功/错误消息：
               - 等待按钮状态变化（例如，从“Applying...”变为完成状态）
               - 验证 BugAnalyst 指定的预期结果
            
            始终严格遵守所提供的时序和等待指令。
            
            在声明“TESTING COMPLETE”之前，必须完成所有步骤。请完整执行每一步，切勿急于结束。
            """
        )

        team = RoundRobinGroupChat(
            participants=[bug_analyst],
            termination_condition=TextMentionTermination('TESTING COMPLETE')
        )

        await Console(team.run_stream(
            task=
            """
            BugAnalyst:
            1. 在 CreditCardBanking 项目中搜索近期的 bug。
            2. 然后设计一个稳定的用户操作流程，可用作冒烟测试。
            
            AutomationAgent:
            准备就绪后，使用 Playwright MCP 自动化该流程并执行。
            """
        ))

    # 关闭 ollama 模型客户端 实例
    await ollama_model_client.close()


asyncio.run(main())
