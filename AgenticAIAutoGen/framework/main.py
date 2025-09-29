import asyncio

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient

from framework.AgentFactory import AgentFactory


async def main():
    ollama_model_client = OllamaChatCompletionClient(model="qwen3:latest")

    agent_factory = AgentFactory(ollama_model_client)
    database_agent = agent_factory.create_database_agent(
        """
        你是一名数据库专家，负责检索用户注册数据。
        
        你的任务：
        1. 连接到 MySQL 数据库 'mydatabse'
        2. 查询 'RegistrationDetails' 表以获取一条随机记录
        3. 查询 'UserNames' 表以获取额外的用户数据
        4. 合并两个表中的数据，创建完整的注册信息
        5. 如有必要，通过添加时间戳或随机数确保邮箱地址唯一
        6. 将所有注册数据整理成结构化格式，以便其他智能体能够理解
        准备就绪后，请输入："DATABASE_DATA_READY - APIAgent 接下来应该执行任务"
        """
    )
    api_agent = agent_factory.create_api_agent(
        """
        你是一名 API 测试专家，可访问 REST API 工具和文件系统。
        
        你的任务：
        1. 首先：从 DatabaseAgent 的 REGISTRATION_DATA 消息中提取准确的注册数据
        2. 读取 Postman 集合以了解 API 契约
        
        按照上述规则构建好 JSON 请求体字段后，使用构建好的请求体字段作为必填字段进行注册 API 调用
        4. 如果注册成功或因 "用户已存在" 失败，则继续进行登录操作
        5. 使用数据库数据中的 username 和 password 进行登录 API 调用
        6. 报告实际的 API 响应状态和成功/失败情况
        
        关键：你必须使用 DatabaseAgent 的 REGISTRATION_DATA 中的准确数据，而不是 Postman 集合中的示例数据。
        同时，完成登录 API 调用以验证你使用注册 API 注册的数据。
        
        基础 URL：https://dummyjson.com
        内容类型：application/json
        
        当注册 API 调用成功且登录尝试完成后，输入："API_TESTING_COMPLETE - ExcelAgent 接下来应该执行任务"
        在响应中包含最终的登录状态（成功/失败）。
        """
    )
    excel_agent = agent_factory.create_excel_agent(
        """
        你是一名 Excel 数据管理专家。仅在 API 智能体完成测试后再继续执行任务。
        
        你的任务：
        1. 等待 API 智能体使用包含登录调用成功信息的 "API_TESTING_COMPLETE" 消息表示完成任务
        2. 从数据库智能体的 REGISTRATION_DATA 消息中提取注册数据
        3. 检查 API 智能体的响应，确认实际的登录成功/失败状态
        4. 仅在实际登录成功时才保存数据
        5. 打开 users.xlsx 文件
        6. 添加带有当前时间戳的注册数据
        7. 保存并验证数据
        
        关键提示：仅在 API 智能体报告登录成功时才保存数据，而不是仅尝试登录就保存。
        
        完成任务后，输入："REGISTRATION PROCESS COMPLETE" 并停止。
        """
    )

    team = RoundRobinGroupChat(
        participants=[database_agent, api_agent, excel_agent],
        termination_condition=TextMentionTermination("REGISTRATION PROCESS COMPLETE")
    )

    result = await Console(team.run_stream(task="执行顺序用户注册流程：\n\n"

                                                "步骤 1 - 数据库智能体（第一个）：\n"
                                                "从数据库表中获取随机注册数据并清晰格式化。\n\n"

                                                "步骤 2 - API 智能体：\n"
                                                "读取 Postman 集合文件，然后使用数据库数据进行注册和登录 API 调用。\n\n"

                                                "步骤 3 - Excel 智能体：\n"
                                                "将成功注册的登录详细信息保存到 Excel 文件中。\n\n"

                                                "每个智能体应在完全完成自己的工作后，下一个智能体再开始工作。 "
                                                "使用指定格式在智能体之间清晰传递数据。"))


asyncio.run(main())