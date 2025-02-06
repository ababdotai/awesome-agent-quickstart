"""
This is a simple example of using autogen to create a team of agents:
- A web surfer agent that can search the web for information
- An assistant agent that can answer questions
- A user proxy agent that can interact with the user

The team is a round robin group chat that will continue to run until the user terminates the conversation.
"""
# pip install -U autogen-agentchat autogen-ext[openai,web-surfer]
# playwright install
import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from env import *

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4o", base_url=os.environ["OPENAI_API_BASE"])
    assistant = AssistantAgent("assistant", model_client)
    web_surfer = MultimodalWebSurfer("web_surfer", model_client)
    user_proxy = UserProxyAgent("user_proxy")
    termination = TextMentionTermination("exit") # Type 'exit' to end the conversation.
    team = RoundRobinGroupChat([web_surfer, assistant, user_proxy], termination_condition=termination)
    await Console(team.run_stream(task="Find information about AutoGen and write a short summary."))

asyncio.run(main())