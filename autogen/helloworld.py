"""
This is a simple example of using autogen to create an assistant agent.
"""
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from env import *

async def main() -> None:
    agent = AssistantAgent("assistant", OpenAIChatCompletionClient(model="gpt-4o", base_url=os.environ["OPENAI_API_BASE"]))
    result = await agent.run(task="Introuce your self!'")
    for msg in result.messages:
        tokens_num = 0 if msg.models_usage is None else msg.models_usage.prompt_tokens + msg.models_usage.completion_tokens
        print(f"{msg.source}: {msg.content} ({tokens_num} tokens)")

asyncio.run(main())