# Import core components 
from langgraph.prebuilt import create_react_agent
from langgraph.store.memory import InMemoryStore
from langmem import create_manage_memory_tool, create_search_memory_tool
from dotenv import load_dotenv

load_dotenv()


# Set up storage 
store = InMemoryStore(
    index={
        "dims": 1536,
        "embed": "openai:text-embedding-3-small",
    }
) 

# Create an agent with memory capabilities 
agent = create_react_agent(
    "openai:gpt-4o",
    tools=[
        # Memory tools use LangGraph's BaseStore for persistence (4)
        create_manage_memory_tool(namespace=("memories",)),
        create_search_memory_tool(namespace=("memories",)),
    ],
    store=store,
)
# Store a new memory 
agent.invoke(
    {"messages": [{"role": "user", "content": "Remember that I prefer dark mode."}]}
)

# Retrieve the stored memory 
response = agent.invoke(
    {"messages": [{"role": "user", "content": "What are my lighting preferences?"}]}
)
print(response["messages"][-1].content)
# Output: "You've told me that you prefer dark mode."