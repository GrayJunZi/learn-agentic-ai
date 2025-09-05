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

```py
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

```py
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

```py
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

https://smithery.ai