from agents.react_agent.tools import basic_research_tool, get_todays_date
from langgraph.prebuilt import create_react_agent
from agents.utils import load_chat_model

async def make_graph():
    
    # initialize our model and tools    
    llm = load_chat_model("openai/gpt-4.1-mini")
    tools = [basic_research_tool, get_todays_date]
    prompt = """
        You are a helpful AI assistant trained in creating engaging social media content!
        you have access to two tools: basic_research_tool and get_todays_date. Please get_todays_date then 
        perform any research if needed, before generating a social media post.
        """

    # Compile the builder into an executable graph
    graph = create_react_agent(
        model=llm, 
        tools=tools, 
        prompt=prompt
    )

    return graph