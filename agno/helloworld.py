from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="Share 15 minute healthy recipes.",
    markdown=True,
)
agent.print_response("Share a breakfast recipe.", stream=True)