import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from util import get_servers_dir
from llm import deepseek_model as model

async def run_agent():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": [os.path.join(get_servers_dir(), "math_server.py")],
                "transport": "stdio",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": f"http://localhost:{os.getenv('MCP_SERVER_PORT')}/mcp",
                "transport": "streamable_http",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(model, tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    print(math_response["messages"][-1].content)
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    print(weather_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_agent())
