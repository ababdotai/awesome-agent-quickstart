import os
from dotenv import load_dotenv
load_dotenv()

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather", port=os.getenv("MCP_SERVER_PORT"), log_level=os.getenv("MCP_SERVER_LOG_LEVEL"))

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always sunny in New York"

if __name__ == "__main__":
    mcp.run(transport="sse")