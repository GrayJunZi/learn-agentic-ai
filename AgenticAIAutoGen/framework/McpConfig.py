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