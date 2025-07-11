"""Create all subagents using the make_graph pattern from react_agent."""
from agents.supervisor.supervisor_configuration import Configuration

from agents.react_agent.graph import make_graph
from langchain_core.runnables import RunnableConfig

# Load supervisor configuration
supervisor_config = Configuration()

async def create_subagents(configurable: dict = None):
    """Create all subagents using the make_graph pattern from react_agent."""
    
    # Use configurable values if provided, otherwise fall back to defaults
    if configurable is None:
        configurable = {}
    
    # Create finance research agent using make_graph
    finance_config = RunnableConfig(
        configurable={
            "model": configurable.get("finance_model", supervisor_config.finance_model),
            "system_prompt": configurable.get("finance_system_prompt", supervisor_config.finance_system_prompt),
            "selected_tools": configurable.get("finance_tools", supervisor_config.finance_tools),
            "name": "finance_research_agent"
        }
    )
    finance_research_agent = await make_graph(finance_config)

    # Create general research agent using make_graph  
    research_config = RunnableConfig(
        configurable={
            "model": configurable.get("research_model", supervisor_config.research_model),
            "system_prompt": configurable.get("research_system_prompt", supervisor_config.research_system_prompt),
            "selected_tools": configurable.get("research_tools", supervisor_config.research_tools),
            "name": "general_research_agent"
        }
    )
    general_research_agent = await make_graph(research_config)

    # Create writing agent using make_graph
    writing_config = RunnableConfig(
        configurable={
            "model": configurable.get("writing_model", supervisor_config.writing_model),
            "system_prompt": configurable.get("writing_system_prompt", supervisor_config.writing_system_prompt),
            "selected_tools": configurable.get("writing_tools", supervisor_config.writing_tools),
            "name": "writing_agent"
        }
    )
    writing_agent = await make_graph(writing_config)
    
    return [finance_research_agent, general_research_agent, writing_agent]



