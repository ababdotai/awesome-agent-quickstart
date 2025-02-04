"""
A minimal example of using langgraph to create a simple conversational agent.
This example demonstrates the basic concepts of langgraph including:
- Creating nodes (functions)
- Building a graph
- Handling state
- Running the agent
"""

from typing import Dict, TypedDict, Annotated, List
from langgraph.graph import StateGraph
from litellm import completion
from config import *

# Define our state schema
class AgentState(TypedDict):
    messages: list[str]
    current_response: str

# Node functions
def get_llm_response(state: AgentState) -> AgentState:
    """Get response from LLM based on conversation history."""
    try:
        # Combine messages into a prompt
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant. Keep responses brief and friendly."
            }
        ]
        
        for msg in state["messages"]:
            messages.append({"role": "user", "content": msg})
            
        # Get response from LLM using config
        model_config = get_model_config()
        response = completion(
            messages=messages,
            api_base=get_api_base(),
            api_key=get_api_key(),
            **model_config
        )
        
        state["current_response"] = response.choices[0].message.content
        return state
    except Exception as e:
        state["current_response"] = f"Error: {str(e)}"
        return state

def format_response(state: AgentState) -> AgentState:
    """Format the response and add it to message history."""
    response = state["current_response"]
    state["messages"].append(response)
    return state

# Build the graph
def build_graph() -> StateGraph:
    """Build the workflow graph."""
    # Create new workflow with state
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("get_response", get_llm_response)
    workflow.add_node("format", format_response)
    
    # Add edges
    workflow.add_edge("get_response", "format")
    
    # Set entry and finish points
    workflow.set_entry_point("get_response")
    workflow.set_finish_point("format")
    
    return workflow

def main():
    # Initialize the graph
    graph = build_graph().compile()
    
    # Initialize state
    state = {
        "messages": ["Tell me a short joke"],
        "current_response": ""
    }
    
    # Run the graph
    result = graph.invoke(state)
    print("User:", state["messages"][0])
    print("Assistant:", result["messages"][-1])

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(str(e))
