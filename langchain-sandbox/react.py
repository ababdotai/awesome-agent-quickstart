import asyncio

from langchain_sandbox import PyodideSandboxTool
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()
# Define the sandbox tool
sandbox_tool = PyodideSandboxTool(
    # Allow Pyodide to install python packages that
    # might be required.
    allow_net=True,
)

model = ChatOpenAI(model="gpt-4o-mini")

# Create an agent with the sandbox tool
agent = create_react_agent(
    model, [sandbox_tool]
)

query = "Calculate the area of a circle with a radius of 5."


async def run_agent(query: str):
    # Stream agent outputs
    async for chunk in agent.astream({"messages": query}):
        print(chunk)
        print("\n")


if __name__ == "__main__":
    # Run the agent
    asyncio.run(run_agent(query))