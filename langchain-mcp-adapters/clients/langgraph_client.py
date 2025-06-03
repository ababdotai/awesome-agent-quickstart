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
                "url": f"http://localhost:{os.getenv('MCP_SERVER_PORT')}/mcp",
                "transport": "streamable_http",
            }
        }
    )

    def call_model(state: State):
        messages = state["messages"]
        response = llm_with_tool.invoke(messages)
        return {"messages": [response]}

    mcp_tools = await mcp_client.get_tools()
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")
    
    llm_with_tool = model.bind_tools(mcp_tools)

    # Compile application and test
    graph_builder = StateGraph(State)
    graph_builder.add_node(call_model)
    graph_builder.add_node("tool", ToolNode(mcp_tools))

    graph_builder.add_edge(START, "call_model")

    # Decide whether to retrieve
    graph_builder.add_conditional_edges(
        "call_model",
        # Assess agent decision
        tools_condition,
        {
            # Translate the condition outputs to nodes in our graph
            "tools": "tool",
            END: END,
        },
    )
    graph_builder.add_edge("tool", "call_model")

    graph = graph_builder.compile()
    graph.name = "Tool Agent"

    return graph

# Run the graph with question
async def main():
    graph = await make_graph()
    result = await graph.ainvoke({"messages": "what is the weather in nyc?"})
    print(result["messages"][-1].content)
    result = await graph.ainvoke({"messages": "what's (3 + 5) x 12?"})
    print(result["messages"][-1].content)

asyncio.run(main())
