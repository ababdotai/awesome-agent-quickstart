import asyncio
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph.checkpoint.memory import InMemorySaver
from langchain_sandbox import PyodideSandboxTool, PyodideSandbox
from dotenv import load_dotenv

load_dotenv()

class State(AgentState):
    # important: add session_bytes & session_metadata keys to your graph state schema - 
    # these keys are required to store the session data between tool invocations.
    # `session_bytes` contains pickled session state. It should not be unpickled
    # and is only meant to be used by the sandbox itself
    session_bytes: bytes
    session_metadata: dict

tool = PyodideSandboxTool(
    # Create stateful sandbox
    stateful=True,
    # Allow Pyodide to install python packages that
    # might be required.
    allow_net=True
)
agent = create_react_agent(
    "gpt-4o-mini",
    tools=[tool],
    checkpointer=InMemorySaver(),
    state_schema=State
)

async def run_agent():
    async for typ, chunk in agent.astream(
        {
            "messages": [
                {"role": "user", "content": "what's 5 + 7? save result as 'a'"}
            ],
            # Important: set session_bytes & session_metadata for Input State
            "session_bytes": None,
            "session_metadata": None
        },
        stream_mode=["messages"],
        config={"configurable": {"thread_id": "123"}},
    ):
        if typ == "messages":
            print(chunk[0].content, end="")

    print("\n")
    print("-"*100)
    print("\n")

    async for typ, chunk in agent.astream(
        {"messages": [{"role": "user", "content": "what's the sine of 'a'?"}]},
        stream_mode=["messages"],
        config={"configurable": {"thread_id": "123"}},
    ):
        if typ == "messages":
            print(chunk[0].content, end="")
    print("\n")

if __name__ == "__main__":
    asyncio.run(run_agent())