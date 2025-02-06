"""
This example demonstrates different ways to initialize models for your agents
Choose one of the following inference types by setting chosen_inference:
- "hf_api": Use Hugging Face Inference API (requires API token)
- "transformers": Run models locally using transformers library
- "ollama": Use local Ollama server
- "litellm": Use LiteLLM to access various model providers
"""

from typing import Optional

from smolagents import HfApiModel, LiteLLMModel, TransformersModel, tool
from smolagents.agents import CodeAgent, ToolCallingAgent

available_inferences = ["hf_api", "transformers", "ollama", "litellm"]
chosen_inference = "transformers"

print(f"Chose model: '{chosen_inference}'")

if chosen_inference == "hf_api":
    model = HfApiModel(model_id="meta-llama/Llama-3.3-70B-Instruct")

elif chosen_inference == "transformers":
    # Use a small but capable local model
    model = TransformersModel(model_id="HuggingFaceTB/SmolLM2-1.7B-Instruct", device_map="auto", max_new_tokens=1000)

elif chosen_inference == "ollama":
    model = LiteLLMModel(
        model_id="ollama_chat/llama3.2",
        api_base="http://localhost:11434",  # Change if using remote server
        api_key="your-api-key",  # Add your API key if required
        num_ctx=8192,  # Increased context window for better performance
    )

elif chosen_inference == "litellm":
    # LiteLLM supports many providers including OpenAI, Anthropic, etc.
    # Example: For Claude 3, use model_id='anthropic/claude-3-5-sonnet-latest'
    model = LiteLLMModel(model_id="gpt-4")


# Example tool that agents can use
@tool
def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    A simple mock weather tool to demonstrate tool usage.
    Returns the same response regardless of input (for demo purposes).

    Args:
        location: Location to get weather for
        celsius: Whether to return temperature in Celsius (not implemented in this demo)
    """
    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"


# Demo using ToolCallingAgent - uses a structured approach to call tools
agent = ToolCallingAgent(tools=[get_weather], model=model)
print("ToolCallingAgent:", agent.run("What's the weather like in Paris?"))

# Demo using CodeAgent - writes and executes Python code to solve tasks
agent = CodeAgent(tools=[get_weather], model=model)
print("CodeAgent:", agent.run("What's the weather like in Paris?"))
