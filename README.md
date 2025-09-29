# Learn Agentic AI

## 一、介绍

### 01. 能学到什么？

#### Table of Contents

我们将构建多代理协作的AI系统。

1. 基础 (Fundamentals)
    - 理解什么是LLM(Large Language Models)、AI Agents、MCP(Model Context Protocal)、Multi Agent System，和Agentic AI Workflows。
        - 理解语言模型和代码的区别。
        - 深入讲解MCP协议及工作原理。
    - 深入了解创建AI代码进行实操的案例。

2. 环境设置 (Environment Setup)
    - 安装 Python 和 suitalbe IDE.
    - 引入 AutoGen 框架。
        - AutoGen 是微软专为多代理工作流设计的框架。
    - 理解 AutoGen 基础概念。

3. 构建AI工作流 (Building Agentic AI Workflow (Multi-Agent System) using AutoGen Framework)
    - 场景 1：
        - 从 `Jira` 中访问最近的Bug数据。
        - 分析并整合这些数据，创建一个全面的`Smoke Test`流程，确保覆盖所有的Bug。
        - 将生成的`Smoke Test`流程转换为`Playwright`自动化操作。
        - 使用`Playwright`执行测试并生成结构化的测试结果。
    - 场景 2:
        - 从数据库中检索与注册相关的数据。
        - 格式化数据并与注册端点的API定义对齐。
        - 使用准备好的数据进行注册API调用。
        - 使用新创建的凭据登录以验证成功。
        - 将结果记录到Excel跟踪器中。

#### 专业化代理生态系统

##### 真实世界代理构建

- `浏览器自动化代理` - Web爬虫和交互。
- `数据库代理` - SQL查询和数据管理。
- `API代理` - RESTAPI 测试和集成。
- `Jira代理` - 自动化项目管理。
- `文件系统代理` - 文件操作和管理。
- `Excel代理` - 表格操作。

##### 高级协作模式

- `MultimodalWebSurfer` - 多模态网络服务器，视觉网络导航和截图。
- `SelectorGroupChat` - 选择器组聊天，基于上下文的动态代理选择。

##### 生产就绪型框架

Agent Factory Pattern
- Generic Reusable Agents
- Context Feeding from Test Files
- MCP Configuration Management
- Framework Best Practices

##### Key Takeaway

From Theory -> Practice: Built autonomous multi-agent systems that can collaborate, self-correct, and complete complex end-to-end workflows without human intervention.

### 02. 什么是 LLM？其特点和局限性是什么？

#### 什么是LLM(Large Language Model)？

- 定义 - AI在大量文本数据上进行训练，以理解和生成人类语言。
- 核心能力 - 文本输入 -> 文本输出
- 训练 - 从数十亿个文本示例中学习模式。

#### 关键特性(Key characteristics)

1. 理解上下文，能跟上对话。
2. 生成连贯文本，像人一样写作。
3. 任务无关的(Task Agnostic)，可以处理大量文本任务。
4. 无动作，只生成响应。

### 03. 从 LLM过渡到AI Agents，AI代理的闪光点(shines)在哪里？

#### 什么是AI Agent？

| 传统LLM | AI Agent |
| ------ | -------- |
| 文本输入 -> 文本输出 | 文本输入 -> 动作 -> 结果 |
| 被动响应 | 主动解决问题 |
| 无外部访问 | 连接到工具/系统 |
| 一次响应 | 多步骤响应 |

#### AI Agent = LLM + 工具 + 自治(Autonomy)

- LLM (大脑)
- Tools (手)
- Autonomy (决策)


#### AI Agents 定义

AI代理是一个自主系统，能够根据环境自主做出决策，并通过执行动作来达成目标。

#### 核心组件

- 面向目标
    - 可以将复杂的目标分解为多个步骤
- 工具访问
    - 可以使用外部系统(数据库、API、文件)
    - 扩展文本生成之外的功能
- 决策
    - 选择何时使用哪些工具。
    - 基于结果进行适配。
- 交互执行
    - 可以尝试多种方法。
    - 从失败中学习和调整。

#### 什么是MCP（Model Context Protocal）?

MCP是一种标准化的方式，用于使AI代理连接到和使用外部工具和服务。

#### 可用的MCP工具

- 数据库，MySQL，PostgreSQL，SQLite
- 表格，Excel  
- APIs，RESTful API，GraphQL
- 文件，本地文件系统和云存储
- 浏览器，Playwright自动化
- 项目管理，Jira、Github

## 二、构建AI Agent

### LLM 应用 MCP 的执行流程

1. LLM 读取 config.json 文件。
2. 根据用户输入，LLM 解析出需要调用的 MCP 工具。
3. LLM 调用对应的 MCP 工具。
4. MCP 工具执行任务，返回结果。
5. LLM 根据结果，生成最终的响应。

### 安装 Playwright MCP

```js
{
    "mcpServers": {
        "playwright": {
            "command": "npx",
            "args": ["@playwright/mcp@latest"]
        }
    }
}
```

### 安装 MySQL MCP

使用 `pip` 命令安装 MCP。
```bash
pip install mysql-mcp-server
```

使用 `pip show` 命令查看安装的 MCP 工具所在位置。

```bash
pip show mysql-mcp-server
```

使用 `pip` 命令安装 `uv` 工具。

```bash
pip install uv
```

通过MCP进行数据库操作。

```js
{
    "mcpServers": {
        "mysql": {
            "command": "uv",
            "args": [
                "--directory",
                "C:\\Users\\Byrne.LAPTOP-FJ476S4Q\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages",
                "run",
                "mysql_mcp_server"
            ],
            "env": {
                "MYSQL_HOST": "localhost",
                "MYSQL_PORT": "3306",
                "MYSQL_USER": "admin",
                "MYSQL_PASSWORD": "admin",
                "MYSQL_DATABASE": "mydatabase"
            }
        }
    }
}
```

### 安装 REST-MCP-SERVER

通过MCP进行REST API调用。

```js
{
    "mcpServers": {
        "rest-api": {
            "command": "npx",
            "args": [
                "-y",
                "dkmaker-mcp-rest-api"
            ],
            "env": {
                "REST_BASE_URL": "",
                "HEADER_Accept": "application/json"
            }
        }
    }
}
```

### 安装 FileSystem MCP

通过MCP进行文件系统操作。

```js
{
    "mcpServers": {
        "filesystem": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "D:\\SourceCode\\learn-agentic-ai"
            ]
        }
    }
}
```

### 安装 Excel MCP

通过MCP进行读写Excel文件。

```js
{
    "mcpServers": {
        "excel-mcp-server": {
            "command": "npx",
            "args": [
                "-y",
                "@negokaz/excel-mcp-server"
            ],
            "env": {
                "EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"
            }
        }
    }
}
```

### 查看所有 MCP 列表

[Smithery](https://www.smithery.ai)是MCP服务器托管平台。

## 三、Agentic AI介绍 与AutoGen框架环境配置

AI Agent = LLM + MCP

MCP Configuration (JSON配置文件)
1. Playwright MCP -> Web浏览器
2. MySQL MCP -> 数据库
3. REST API MCP -> 外部API
4. FileSystem MCP -> 文件系统
5. Excel MCP -> Excel文件

这种架构存在一些缺点，单个Agent承担太多责任、低性能。

### 为什么使用多代理系统？

#### 单个代理的限制

（1）认知超载 ( cognitive overload )
- 单个代理所承担的职责过多，导致性能下降。
- "Jack of all trades, master of none"（翻译过来就是：啥都会，啥都不精）

（2）工具复杂度
- 1个拥有20个工具的代理 vs 4个代理各有5个工具。
- 更难管理与调试。

（3）没有并行化 ( no parallelization )
- 一切都是顺序发生的
- 瓶颈(bottlenecks)与延迟

#### 多代理系统的优势

（1）专业化
数据库专家(expert) + API专家(specialist) + Excel大师(master) = 更好的结果

（2）并行处理
代理A (数据) || 代理B (分析) || 代理C (报告)

（3）易于维护
- 更新一个代理不影响其他
- 清晰的职责边界

（4）可扩展性（scalability）
- 为新功能(capabilities)添加新代理
- 当不需要时移除代理。

> 相比较下多代理要比单代理节省成本。

### 什么是 Agentic AI？

#### Agentic AI 定义

Agentic AI 是指能够自主采取行动并做出决定以实现目标的AI系统，而不仅仅是对提示做出响应。

> Agentic AI refers to AI systems that can autonomously take actions and make decisions to achieve goals, rather than just responding to prompts.

#### 关键原则

1. 自主性 ( Autonomy )
    - 在没有人类持续指导的情况下做出决定
    - 能够处理突发情况
2. 机构 ( Agency )
    - 主动解决问题
    - 主动而非被动
3. 编排 ( Orchestration )
    - 协调多种能力
    - 管理复杂的工作流
4. 推理 ( Reasoning )
    - 规划多步解决方案
    - 根据结果调整策略

### 多代理工作流模式

| 模式 | 说明 |
| -- | -- |
| 顺序工作流( Sequential Workflow ) | 代理A -> 代理B -> 代理C -> 结果<br>示例：数据采集 -> 分析 -> 报告生成 |
| 并行工作流( Parallel Workflow ) | 代理B (API测试)<br>代理A和代理D同时处理其他任务<br>代理C (数据分析)<br>示例：不同系统组件的并行测试 |
| 分层工作流( Hierarchical Workflow ) | 管理智能体作为协调者，用于决定调用哪个智能体<br>示例：项目管理协调专家团队 |
| 协作工作流( Collaborative Workflow ) | 代理A <-> 代理B <-> 代理C<br>示例：用反馈循环迭代解决问题 |

> 多个AI代理共同解决问题被称为Agentic AI。

#### 传统AI 与 Agentic AI 对比

| 传统AI | Agentic AI |
| -- | -- |
| 回答问题 | 解决问题 |
| 单一交互 | 多步骤执行 |
| 被动 | 主动 |
| 人类指导 | 自主 |
| 无工具 | 工具驱动(tool enabled) |

#### 整合所有内容

- `AI Agent` = `LLM(大脑)` + `MCP(工具)` + `自主(automony)`
- `Multi-Agent System` = `Multiple AI Agent` + `协调(Coordination)`
- `Agentic AI` = `Multi-Agent System` + `目标驱动(Goal Oriented Design)`

### 配置Python开发环境

打开 [Python官网](https://www.python.org/downloads/) 下载Python安装包。

查看Python安装位置：
```bash
where python
```

查看Python安装版本：
```bash
python --version
```

可以使用 PyCharm 社区版，进行Python开发。

### 设置Python虚拟环境并且安装AutoGen

#### 创建虚拟环境

创建虚拟环境：
```bash
python -m venv .venv
```

> 虚拟环境可以隔离项目依赖，避免不同项目之间的冲突。

激活虚拟环境：
```bash
.venv\Scripts\activate
```

> 虚拟环境激活后，命令行前面会显示虚拟环境的名称。

#### 安装 AutoGen

安装AutoGen：
```bash
pip install -U autogen-agentchat
```

安装模型客户端：
```bash
pip install -U "autogen-ext[ollama]"
```

安装MCP工具：
```bash
pip install -U "autogen-ext[mcp]"
```

## 四、AutoGen框架基础 AssistantAgents 与 RoundRobinGroupChat

### 如何启动运行任何Python代码及其函数调用

```py
import asyncio

async def main():
    print('I am inside function')

asyncio.run(main())
```

### AssistantAgent 介绍及其实现

#### AI Agent系统架构

- 单智能体 - 该智能体能解决问题并返回单一响应，这个智能体将成为任务助手。
- 多智能体 - 多个智能体合作完成任务，每个智能体负责不同的任务。
- 人机交互智能体 - 每个阶段都需要人类的介入，代理与人类互动以逐步提供协助，直至任务完成。

#### 构建智能体

```py
import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    ollama_model_client = OllamaChatCompletionClient(model='deepseek-r1:14b')

    AssistantAgent(name='assistant', model_client=ollama_model_client)

asyncio.run(main())
```

### 如何让AssistantAgent回答图像文件等多模态输入

> 多模态输入指的是模型能够处理多种类型的输入，例如文本、图像、音频、视频等。

```py
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

    image = Image.from_file("..\\1.png")

    multimodal_message = MultiModalMessage(
        content=["What do you see in this image", image],
        source="user",
    )

    await Console(assistant.run_stream(task=multimodal_message))
    await ollama_model_client.close()

asyncio.run(main())
```

### 什么是RoundRobinGroupChat？如何在团队中的代理之间进行协调

> RoundRobinGroupChat 是一种团队合作模式，其中每个代理在团队中轮流执行任务。

```py
import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
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

    team = RoundRobinGroupChat(participants=[agent1, agent2])
    team.run_stream(task="让我们讨论一下什么是乘法以及它是如何运作的。")


asyncio.run(main())
```

## 五、AutoGen框架基础 Termination、StateSaving以及HumanInLoop

### 什么是Termination？我们为什么需要它？

> 可以定义终止条件(Termination)来控制团队的轮询群聊(RoundRobinGroupChat)，例如任务完成、时间限制、用户输入等。
> 终止条件可以是静态的，也可以是动态的，根据任务的进度和结果来确定。
> 终止条件的设置可以确保任务在合理的时间内完成，避免无限循环或资源浪费。

通过最大消息数来控制终止。
> 可以设置最大消息数，当团队成员之间的消息数量超过最大消息数时，团队将停止轮询。
> 最大消息数的设置可以确保团队在合理的时间内完成任务，避免无限循环或资源浪费。

```py
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
```

### 如何让人类进入循环，AutoGen中的UserProxyAgent介绍

将 `UserProxyAgent` 加入到聊天群组中以实现人类参与循环。

```py
import asyncio

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

    # 创建第一个智能体（老师）
    assistant = AssistantAgent(
        name='MathTutor',
        model_client=ollama_model_client,
        system_message="你是一位乐于助人的数学辅导老师，请帮助用户一步一步解决数学问题。"
        "当用户说 '已完成' 或类似语句表示结束时,予以确认并回复 '课程完成' 以结束会话。"
    )

    # 创建第二个智能体（学生用户）
    user_proxy = UserProxyAgent(
        name='Student',
    )

    team = RoundRobinGroupChat(
        participants=[assistant, user_proxy],
        termination_condition=TextMentionTermination("课程完成"),
    )

    await Console(team.run_stream(task="我需要帮助解决代数问题，你能帮我解答 2*4+5 的结果吗？"))

    await ollama_model_client.close()

asyncio.run(main())
```

### 状态保存机制，如何在保留状态的代理之间切换

假设我们在与智能体进行对话，如果遇到突发情况代理将被关闭，或者Tokens耗尽等，导致智能体被关闭时，如果启动新代码那么必须从头开始，之前讨论的内容将消失。

我们可以将对话内容保存至`json`文件中，这样无论切换哪几种代理，都可以保留之前的对话状态。

我们可以使用 `save_state()` 函数 和 `load_state()` 函数来保存和加载智能体的状态。

```py
import asyncio
import json

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

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
```

### 使用 SelectorGroupChat 实现动态选择在团队中执行任务的代理

`SelectorGroupChat` 会根据当前的任务和上下文，动态选择在团队中执行任务的代理。

```py
import asyncio
import json

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

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
```

可以使用 `|` 将多种终止条件组合使用，例如：
- `TextMentionTermination`：当智能体在回复中提到特定文本时触发终止。
- `MaxMessageTermination`：当智能体发送的消息数量达到预设值时触发终止。

```py
text_termination = TextMentionTermination("TERMINATE")
max_messages_termination = MaxMessageTermination(max_messages=15)

termination = text_termination | max_messages_termination

team = SelectorGroupChat(
    participants=[critic, writer, researcher],
    model_client=ollama_model_client,
    termination_condition=termination,
    allow_repeated_speaker=True
)
```

## 六、AutoGen框架基础 SelectorGroupChat、MCPWorkbench和BrowserAgent

### Autogen中具有内置浏览器自动化功能的特殊代理

AutoGen中内置的`MultimodalWebSurfer`代理可以用于浏览器自动化任务，例如搜索、导航和提取信息。

其底层使用了`Playwright`库来实现浏览器自动化。

```py
import asyncio

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main():
    # 创建 ollama 模型客户端 实例
    ollama_model_client = OllamaChatCompletionClient(model='qwen3:latest')

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
```

### 如何通过 mcpworkbench 类为 Assistant Agent 添加 MCP 工具支持

```py
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
```

## 七、了解Agentic工作流的目标及设置Agent的前置条件

- 场景：
    - 从`Jira`中访问最近的`bug`数据，并且需要修复并关闭缺陷。
    - 分析所有最近关闭的缺陷并将它们整合到全面的冒烟测试(`Smoke Test`)流程中。
    - 将测试用例转换并生成为`Playwright`自动化操作。
    - 使用`Playwright`执行生成的测试用例并生成结构化测试结果。
- `Jira Agent` ：
    - 用于从`Jira`中访问和操作缺陷数据。
    - 分析缺陷并准备整合的冒烟测试逻辑。
- `Playwright Agent` ：
    - `Jira Agent` 将创建的冒烟测试流程交给 `Playwright Agent`。
    - `Playwright Agent` 负责将测试步骤转换为可执行的`Playwright`命令并执行。

> 由于`Jira`需要`License`才能正常运行，所以本文后续采用`Plane`作为示例。

### 本地部署 Jira

创建 `podman-compose.yml` 文件，配置jira容器。 

```yml
version: '3'

services:
  jira-postgres:
    image: postgres:latest
    container_name: jira-postgres
    environment:
      - POSTGRES_DB=jira
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - jira-net
    ports:
      - "5432:5432"
    restart: unless-stopped

  jira:
    image: cptactionhank/atlassian-jira-software:latest
    container_name: jira
    depends_on:
      - jira-postgres
    ports:
      - "8080:8080"
    volumes:
      - jira_data:/var/atlassian/jira
        networks:
      - jira-net
    environment:
      - CATALINA_OPTS=-Xms2048m -Xmx4096m
    restart: unless-stopped

volumes:
  postgres_data:
  jira_data:
  
networks:
  jira-net:
    driver: bridge
```

> - 启动容器: `podman-compose up -d`
> - 访问 Jira: 打开浏览器并访问 `http://localhost:8080`
> - 登录 Jira: 初始用户名是 `admin`，密码是 `admin`。
> - 删除容器：`podman-compose down`
> - 移除数据卷：`podman volume rm postgres_data jira_data`

### 本地部署 Plane

1. 创建一个文件夹用于部署和数据存储。

```bash
mkdir plane-selfhost
```

2. 进入该文件夹中。

```bash
cd plane-selfhost
```

3. 下载最新稳定版。

```bash
curl -fsSL -o setup.sh https://github.com/makeplane/plane/releases/latest/download/setup.sh
```

4. 设置 `setup.sh` 文件的可执行权限。

```bash
chmod +x setup.sh
```

5. 运行 `setup.sh` 文件进行安装。

```bash
./setup.sh
```

## 八、使用 Plane Agent 和 Playwright Agent 构建自主的多智能体工作流

### 使用 Plane 的 McpWorkbench 创建 Plane 智能体

添加 `Plane` 的 MCP 服务参数。

```py
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

async with plane_workbench as plane_wb:
    # 创建 Plane 智能体
    assistant = AssistantAgent(
        name='BugAnalyst',
        model_client=ollama_model_client,
        workbench=plane_wb,
        system_message=""
    )
```

### 使用 Playwright 的 McpWorkbench 创建浏览器自动化智能体

添加 `Playwright` 的 MCP 服务参数。

```py
# Playwright 系统 MCP 服务参数
playwright_server_params = StdioServerParams(
    command="npx",
    args=[
        "@playwright/mcp@latest",
    ]
)

# 创建 Playwright 系统的 MCP 实例
playwright_workbench = McpWorkbench(playwright_server_params)

async with playwright_workbench as playwright_wb:
    # 创建 Playwright 智能体
    automation_analyst = AssistantAgent(
        name='AutomationAnalyst',
        model_client=ollama_model_client,
        workbench=playwright_wb,
        system_message=""
    )
```

### 构建基于 RoundRobinGroupChat 的 Agentic AI 解决方案的完整端到端工作流

为每个智能体添加各自的提示词并设定任务目标。

```py
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
            
            1. 从 Plane 中检索并审查 **CreditCardBanking 项目**（项目标识符：`CRED`）中**最近的 5 个缺陷**。  
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
            participants=[bug_analyst, automation_analyst],
            termination_condition=TextMentionTermination('TESTING COMPLETE')
        )

        await Console(team.run_stream(
            task=
            """
            BugAnalyst:
            1. 在 CRED 项目中搜索近期的 bug。
            2. 然后设计一个稳定的用户操作流程，可用作冒烟测试。
            3. 使用真实 URL，例如：https://rahulshettyacademy.com/seleniumPractise/#/
            
            AutomationAgent:
            准备就绪后，使用 Playwright MCP 自动化该流程并执行。
            """
        ))

    # 关闭 ollama 模型客户端 实例
    await ollama_model_client.close()


asyncio.run(main())
```

## 九、智能体工程模式 使用 数据库、API 和 Excel 设计多智能体系统

### 理解多智能体系统的目标及其工作流程

- 数据库智能体：连接多个数据库并且获取多个表的数据，这个智能体返回结构化的数据给下游智能体。
- API+文件系统智能体：从本地文件系统读取定义好的API调用的方式，能够根据数据库智能体提供的结构化数据进行API调用。
- Excel智能体：写入本地Excel文件。

### 什么是 AgentFactory？如何在工厂内隔离和创建代理

场景：
1. 连接数据并且从多个表中获取数据。
2. 读取API定义文件理解API调用所必须的结构。
3. 使用从数据库中获取的数据去构建调用注册接口的方法。
4. 验证提交数据并调用登录接口。
5. 最终将注册的信息存储至Excel文件。

#### 定义MCP配置类

将各个智能体的MCP配置类进行封装。

```py
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


class McpConfig:
    def __init__(self):
        pass

    def get_mysql_workbench(self):
        mysql_server_params = StdioServerParams(
            command="uv",
            args=[
                "--directory",
                "C:\\Users\\Byrne.LAPTOP-FJ476S4Q\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages",
                "run",
                "mysql_mcp_server"
            ],
            env={
                "MYSQL_HOST": "localhost",
                "MYSQL_PORT": "3306",
                "MYSQL_USER": "admin",
                "MYSQL_PASSWORD": "admin",
                "MYSQL_DATABASE": "mydatabase"
            }
        )

        return McpWorkbench(server_params=mysql_server_params)

    def get_rest_api_workbench(self):
        rest_api_server_params = StdioServerParams(
            command="npx",
            args=[
                "-y",
                "dkmaker-mcp-rest-api"
            ],
            env={
                "REST_BASE_URL": "",
                "HEADER_Accept": "application/json",
            }
        )
        return McpWorkbench(server_params=rest_api_server_params)

    def get_excel_workbench(self):
        excel_server_params = StdioServerParams(
            command="npx",
            args=[
                "-y",
                "@negokaz/excel-mcp-server"
            ],
            env={
                "EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"
            }
        )
        return McpWorkbench(server_params=excel_server_params)

    def get_filesystem_workbench(self):
        filesystem_server_params = StdioServerParams(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "D:\\SourceCode\\learn-agentic-ai"
            ]
        )
        return McpWorkbench(server_params=filesystem_server_params)
```

#### 定义AgentFactory类

将各个智能体的创建方法进行封装。

```py
from autogen_agentchat.agents import AssistantAgent

from framework.McpConfig import McpConfig


class AgentFactory:
    def __init__(self,model_client):
        self.model_client = model_client
        self.mcp_config = McpConfig()
    
    def create_database_agent(self, system_message):
        database_agent = AssistantAgent(
            name="DatabaseAgent",
            model_client=self.model_client,
            workbench=self.mcp_config.get_mysql_workbench(),
            system_message=system_message,
        )
        return database_agent

    def create_api_agent(self, system_message):
        rest_api_workbench = self.mcp_config.get_rest_api_workbench()
        filesystem_workbench = self.mcp_config.get_filesystem_workbench()

        api_agent = AssistantAgent(
            name="APIAgent",
            model_client=self.model_client,
            workbench=[rest_api_workbench, filesystem_workbench],
            system_message=system_message,
        )
        return api_agent

    def create_excel_agent(self, system_message):
        excel_agent = AssistantAgent(
            name="ExcelAgent",
            model_client=self.model_client,
            workbench=self.mcp_config.get_excel_workbench(),
            system_message=system_message,
        )
        return excel_agent     
```

#### 创建智能体实例

在主函数中，我们使用OllamaChatCompletionClient创建一个模型客户端实例，然后通过AgentFactory创建数据库智能体、API智能体和Excel智能体。

```py
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
```

## 十、上下文工程定义系统消息给智能体用以内部协调

### 为各个智能体设置提示词

```py
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
```