from langchain_core.runnables import RunnableConfig
from agents.supervisor.supervisor_configuration import Configuration
from agents.supervisor.subagents import create_subagents
from agents.utils import load_chat_model

from langgraph_supervisor import create_supervisor

# Main graph construction
async def make_supervisor_graph(config: RunnableConfig):
    # Extract configuration values directly from the config
    configurable = config.get("configurable", {})
    supervisor_model = configurable.get("supervisor_model", "openai/gpt-4.1")
    supervisor_system_prompt = configurable.get("supervisor_system_prompt", "You are a helpful supervisor agent.")
    
    # Create subagents using the new async function, passing configurable values
    subagents = await create_subagents(configurable)

    # Create supervisor graph
    supervisor_graph = create_supervisor(
        agents=subagents,
        model=load_chat_model(supervisor_model),
        prompt=supervisor_system_prompt,
        config_schema=Configuration
    )

    compiled_graph = supervisor_graph.compile()
    return compiled_graph
