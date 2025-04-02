import os
import asyncio
from contextlib import asynccontextmanager
from typing import Annotated, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from util import get_servers_dir
from llm import deepseek_model as model

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# Make the graph with MCP context
@asynccontextmanager
async def make_graph():
    mcp_client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": [os.path.join(get_servers_dir(), "math_server.py")],
                "transport": "stdio",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": f"http://localhost:{os.getenv('MCP_SERVER_PORT')}/sse",
                "transport": "sse",
            }
        }
    )

    def agent(state: State):
        messages = state["messages"]
        response = llm_with_tool.invoke(messages)
        return {"messages": [response]}

    async with mcp_client:
        mcp_tools = mcp_client.get_tools()
        print(f"Available tools: {[tool.name for tool in mcp_tools]}")
        llm_with_tool = model.bind_tools(mcp_tools)

        # Compile application and test
        graph_builder = StateGraph(State)
        graph_builder.add_node(agent)
        graph_builder.add_node("tool", ToolNode(mcp_tools))

        graph_builder.add_edge(START, "agent")

        # Decide whether to retrieve
        graph_builder.add_conditional_edges(
            "agent",
            # Assess agent decision
            tools_condition,
            {
                # Translate the condition outputs to nodes in our graph
                "tools": "tool",
                END: END,
            },
        )
        graph_builder.add_edge("tool", "agent")

        graph = graph_builder.compile()
        graph.name = "Tool Agent"

        yield graph

# Run the graph with question
async def main():
    async with make_graph() as graph:
        result = await graph.ainvoke({"messages": "what is the weather in nyc?"})
        print(result)
        result = await graph.ainvoke({"messages": "what's (3 + 5) x 12?"})
        print(result)

asyncio.run(main())
