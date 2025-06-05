import asyncio
import json
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from llm import deepseek_model as model
from util import get_servers_dir

async def run_agent():
    # read mcpServers.json
    config_path = Path(__file__).parent / "mcpServers.json"
    with open(config_path, "r") as f:
        server_config = json.load(f)
    # replace environment variables for path and url
    server_config["mcpServers"]["math"]["args"][0] = server_config["mcpServers"]["math"]["args"][0].replace("$SERVERS_DIR", get_servers_dir())
    server_config["mcpServers"]["weather"]["url"] = server_config["mcpServers"]["weather"]["url"].replace("$MCP_SERVER_PORT", "8001")

    print(server_config["mcpServers"])

    client = MultiServerMCPClient(server_config["mcpServers"])
    tools = await client.get_tools()
    agent = create_react_agent(model, tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    print(math_response["messages"][-1].content)
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    print(weather_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_agent())
