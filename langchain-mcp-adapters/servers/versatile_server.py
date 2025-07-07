import asyncio
from fastmcp import Client
from fastmcp import FastMCP
from pathlib import Path

# create a mcp object with name TopicExplainer
mcp = FastMCP(name='VersatileServer')


# define the tool
@mcp.tool()
def hello_world(name: str) -> str:
    return f"Hello World. This is {name} 👋"


# create prompt
@mcp.prompt
def explain_topic(topic: str) -> str:
    """Generates a query prompt for explanation of topic"""
    return f"Can you explain {topic} in a beginner friendly manner with simple wordings and no technical jargon. Include Concept & Examples."


# basic resource
@mcp.resource("resource://greeting")
def greet() -> str:
    """Simple greet"""
    return "Hey This Is Zu👋"


# Image resource with URL - protocol://host//path
@mcp.resource("images://zu.jpeg", mime_type="image/jpeg")  # defined uri -> returns in json output for resource calls
def fetch_image_bytes() -> bytes:
    """Returns Zu's profile photo"""
    file_path = Path("resources/zu.jpeg").resolve()  # file must be present at script route

    if not file_path.exists():
        raise FileNotFoundError(f"Image file not found: {file_path}")

    return file_path.read_bytes()


async def self_test():
    # create a aynschronus loop to run mcp client
    async with Client(mcp) as client:
        # fetch all tools
        tools = await client.list_tools()
        print("Available tools:", [t.name for t in tools])

        # fetch all prompts
        prompts = await client.list_prompts()
        print("Available prompts:", [p.name for p in prompts])

        # fetch all resources
        resources = await client.list_resources()
        print("Available resources:", [r.uri for r in resources])

        # Provide the topic to explain_topic for testing and check results
        result = await client.get_prompt("explain_topic", {"topic": "machine learning"})  # change topic
        # add more prompts here for testing multiple prompts

        print("Generated prompt:", result.messages[0].content.text)


if __name__ == "__main__":
    # `fastmcp run versatile_server.py` to start the server
    # `fastmcp dev versatile_server.py` to debug the server
    # mcp.run(transport="stdio")

    # `uv run versatile_server.py` to test the server
    # `python versatile_server.py` to test the server
    asyncio.run(self_test())
