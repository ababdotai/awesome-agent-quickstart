"""
A minimal example of using smolagents to create a simple agent.
This example demonstrates the basic concepts of smolagents including:
- Defining a tool
- Choosing a model
- Creating a code agent
"""
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from env import *

model = HfApiModel()
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")