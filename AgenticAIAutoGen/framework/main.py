import asyncio

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient

from framework.AgentFactory import AgentFactory


async  def main():
    ollama_model_client = OllamaChatCompletionClient(model="qwen3:latest")

    agent_factory = AgentFactory(ollama_model_client)
    database_agent = agent_factory.create_database_agent("")
    api_agent = agent_factory.create_api_agent("")
    excel_agent = agent_factory.create_excel_agent("")

    team = RoundRobinGroupChat(
        participants=[database_agent, api_agent, excel_agent],
        termination_condition=TextMentionTermination("REGISTRATION PROCESS COMPLETE")
    )

    result = await Console(team.run_stream(task=""))

asyncio.run(main())