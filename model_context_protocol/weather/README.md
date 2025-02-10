1. Install uv
```shell
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install dependencies
```shell
uv sync
```

3. Add the server to client
- Claude Desktop

Open the `claude_desktop_config.json` file:
```shell
# macOS/Linux
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
# Windows
code $env:AppData\Claude\claude_desktop_config.json
```

Add the server to the `mcpServers` object:
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