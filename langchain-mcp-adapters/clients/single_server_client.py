import os
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from util import get_servers_dir
from llm import deepseek_model as model

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=[os.path.join(get_servers_dir(), "math_server.py")],
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            return agent_response

if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)
    print(result["messages"][-1].content)
