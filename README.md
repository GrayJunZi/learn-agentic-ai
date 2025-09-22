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