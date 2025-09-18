import asyncio
import json

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen2.5vl:latest')

    researcher = AssistantAgent(
        name="ResearcherAgent",
        model_client=ollama_model_client,
        system_message="你是一位研究人员。你的职责是收集信息并仅提供研究结果。"
                       "不要撰写文章或创建内容——只需提供研究数据和事实。"
    )

    writer = AssistantAgent(
        name="WriterAgent",
        model_client=ollama_model_client,
        system_message="你是一位作家。你的职责是接收研究信息，"
                       "并据此创作出高质量的文章。请等待研究信息提供完毕后再进行内容撰写。"
    )

    critic = AssistantAgent(
        name="CriticAgent",
        model_client=ollama_model_client,
        system_message="你是一位评论家。请审阅撰写好的内容并提供反馈意见。"
                       "当对最终结果满意时，请说‘TERMINATE’（终止）。"
    )

    text_termination = TextMentionTermination("TERMINATE")
    max_messages_termination = MaxMessageTermination(max_messages=15)

    termination = text_termination | max_messages_termination

    team = SelectorGroupChat(
        participants=[critic, writer, researcher],
        model_client=ollama_model_client,
        termination_condition=termination,
        allow_repeated_speaker=True
    )

    await Console(team.run_stream(task="研究可再生能源趋势，并撰写一篇关于太阳能未来发展的简短文章。"))

    # 关闭 ollama 模型客户端 实例
    await ollama_model_client.close()

asyncio.run(main())
