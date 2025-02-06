"""
This example demonstrates how to use the CodeAgent to execute code.
"""
from smolagents import CodeAgent, VisitWebpageTool, HfApiModel

agent = CodeAgent(
    tools = [VisitWebpageTool()],
    model=HfApiModel(),
    additional_authorized_imports=["requests", "markdownify"],
    use_e2b_executor=True
)

agent.run("What was Abraham Lincoln's preferred pet?")