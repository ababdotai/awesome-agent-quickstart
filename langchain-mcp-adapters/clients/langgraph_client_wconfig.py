import os
import asyncio
import json
from pathlib import Path
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
    """State definition for the graph"""
    messages: Annotated[Sequence[BaseMessage], add_messages]

# Make the graph with MCP context
async def make_graph():
    """Create and configure the LangGraph with MCP tools from configuration file"""
    # Read mcpServers.json configuration
    config_path = Path(__file__).parent / "mcpServers.json"
    with open(config_path, "r") as f:
        server_config = json.load(f)
    
    # Replace environment variables for path and url
    server_config["mcpServers"]["math"]["args"][0] = server_config["mcpServers"]["math"]["args"][0].replace("$SERVERS_DIR", get_servers_dir())
    server_config["mcpServers"]["weather"]["url"] = server_config["mcpServers"]["weather"]["url"].replace("$MCP_SERVER_PORT", os.getenv('MCP_SERVER_PORT', '8000'))
    
    print(f"Server configuration: {server_config['mcpServers']}")
    
    mcp_client = MultiServerMCPClient(server_config["mcpServers"])
    mcp_tools = await mcp_client.get_tools()
    print(f"Available tools: {[tool.name for tool in mcp_tools]}")
    
    llm_with_tool = model.bind_tools(mcp_tools)

    def call_model(state: State):
        """Call the language model with the current state"""
        messages = state["messages"]
        response = llm_with_tool.invoke(messages)
        return {"messages": [response]}

    # Compile application and test
    graph_builder = StateGraph(State)
    graph_builder.add_node("call_model", call_model)
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
    """Main function to run the agent with test questions"""
    graph = await make_graph()
    
    # Test weather query
    result = await graph.ainvoke({"messages": "what is the weather in nyc?"})
    print(result["messages"][-1].content)
    
    # Test math query
    result = await graph.ainvoke({"messages": "what's (3 + 5) x 12?"})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())