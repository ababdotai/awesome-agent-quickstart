# Model Context Protocol Examples

Welcome to the Model Context Protocol (MCP) examples! This directory contains ready-to-run examples demonstrating how to extend Claude's capabilities through custom context protocols.

## ⚡ Quick Start (5-Minute Setup)

Let's create your first MCP server! We'll start with a simple weather service example.

1. Install uv (Fast Python Package Installer):
```shell
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install dependencies:
```shell
cd weather
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

3. Configure Claude Desktop:

Open the configuration file:
```shell
# macOS/Linux
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
# Windows
code $env:AppData\Claude\claude_desktop_config.json
```

Add the server configuration:
```json
# macOS/Linux
{
    "mcpServers": {
        "weather": {
            "command": "/ABSOLUTE/PATH/TO/PARENT/FOLDER/uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                "run",
                "weather.py"
            ]
        }
    }
}
# Windows
{
    "mcpServers": {
        "weather": {
            "command": "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\uv",
            "args": [
                "--directory",
                "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\weather",
                "run",
                "weather.py"
            ]
        }
    }
}
```

4. Test the server
- Claude Desktop: Ask "What is the weather in San Francisco?" or What are the active weather alerts in Texas?", you shall see Claude is asking you for server invocation.