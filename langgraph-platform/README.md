# LangGraph Configuration Patterns Demo

This project demonstrates **how to implement configuration patterns** in ReAct Agents and supervisor-style architectures using [LangGraph](https://github.com/langchain-ai/langgraph). It shows the progression from hardcoded agents to flexible, configurable systems.


## Configuration Pattern Progression

This demo showcases three approaches to agent configuration:

### 1. **No Configuration** (`agents/react_agent/graph_without_config.py`)
- Hardcoded ReAct agent
- Fixed model, prompt, and tools
- Simple but inflexible

### 2. **Single Agent Configuration** (`agents/react_agent/graph.py`)
- Dynamic configuration via `RunnableConfig`
- Configurable models, prompts, and tools
- Clean `config.get("configurable", {})` pattern

### 3. **Multi-Agent Configuration** (`agents/supervisor/`)
- Supervisor orchestrating multiple configured agents
- Each subagent uses the same configuration pattern
- Shows how configuration scales to complex architectures

## What it demonstrates

### Configuration Evolution
1. **Start simple**: Hardcoded values for quick prototyping
2. **Add flexibility**: Runtime configuration for different use cases  
3. **Scale complexity**: Same configuration patterns across multiple agents

### Key Configuration Patterns
- **Direct extraction**: `configurable = config.get("configurable", {})`
- **Default values**: `configurable.get("model", "default-model")`
- **Reusable functions**: Same `make_graph(config)` pattern everywhere
- **Simplified approach**: No complex configuration classes needed

## Configuration in Action

### Single Agent Configuration
```python
async def make_graph(config: RunnableConfig):
    # Extract configuration values directly
    configurable = config.get("configurable", {})
    model = configurable.get("model", "anthropic/claude-3-5-sonnet-latest")
    system_prompt = configurable.get("system_prompt", "You are a helpful AI assistant.")
    selected_tools = configurable.get("selected_tools", ["get_todays_date"])
    
    # Use the configuration
    llm = load_chat_model(model)
    tools = get_tools(config)
    
    return create_react_agent(model=llm, tools=tools, prompt=system_prompt)
```

### Multi-Agent Configuration
```python
async def create_subagents():
    # Each subagent gets its own configuration
    finance_config = RunnableConfig(
        configurable={
            "model": supervisor_config.finance_model,
            "system_prompt": supervisor_config.finance_system_prompt,
            "selected_tools": supervisor_config.finance_tools
        }
    )
    finance_agent = await make_graph(finance_config)
    # ... more agents using same pattern
```

## Why This Approach?

### ✅ **Simplicity**
- No complex configuration classes
- Direct dictionary access
- Easy to understand and modify

### ✅ **Consistency** 
- Same pattern for single and multi-agent systems
- Reusable `make_graph()` function
- Predictable configuration structure

### ✅ **Flexibility**
- Runtime configuration changes
- Easy to add new configuration options
- Works with LangGraph Studio

### ✅ **Scalability**
- Pattern works from simple to complex architectures
- No architectural debt when scaling up
- Clean separation of concerns

## Getting Started

Assuming you have already [installed LangGraph Studio](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file#download), to set up:

1. **Install dependencies**:
   ```bash
   # Create and activate a virtual environment
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Create a `.env` file**:
   ```bash
   cp .env.example .env
   ```

3. **Define required API keys** in your `.env` file.

The primary search tool uses [Tavily](https://tavily.com/). Create an API key [here](https://app.tavily.com/sign-in).

<!--
Setup instruction auto-generated by `langgraph template lock`. DO NOT EDIT MANUALLY.
-->

4. **Debug locally**:
```bash
langgraph dev
INFO:langgraph_api.cli:

        Welcome to

╦  ┌─┐┌┐┌┌─┐╔═╗┬─┐┌─┐┌─┐┬ ┬
║  ├─┤││││ ┬║ ╦├┬┘├─┤├─┘├─┤
╩═╝┴ ┴┘└┘└─┘╚═╝┴└─┴ ┴┴  ┴ ┴

- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs

This in-memory server is designed for development and testing.
For production use, please use LangGraph Platform.
```

5. **Run the server** (Docker must be installed):

```bash
langgraph up
Starting LangGraph API server...
For local dev, requires env var LANGSMITH_API_KEY with access to LangGraph Platform.
For production use, requires a license key in env var LANGGRAPH_CLOUD_LICENSE_KEY.
/ Pulling...⚠️  Security Recommendation: Consider switching to Wolfi Linux for enhanced security.
   Wolfi is a security-oriented, minimal Linux distribution designed for containers.
   To switch, add '"image_distro": "wolfi"' to your langgraph.json config file.

Ready!       
- API: http://localhost:8123
- Docs: http://localhost:8123/docs
- LangGraph Studio: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:8123
```

6. **Run the client**

```bash
python client.py
```

Example output:
```bash
Creating assistant
Running assistant
Receiving event of type: metadata
{'run_id': '1f05e348-e5ed-6a81-82fa-e97e6957969a', 'attempt': 1}



Receiving event of type: updates
{'agent': {'messages': [{'content': 'I was created by OpenAI, an artificial intelligence research and deployment company. My underlying architecture is based on the GPT (Generative Pre-trained Transformer) model, which has been developed and trained by teams of researchers and engineers at OpenAI. If you have more questions about OpenAI or how I work, feel free to ask!', 'additional_kwargs': {'refusal': None}, 'response_metadata': {'token_usage': {'completion_tokens': 67, 'prompt_tokens': 49, 'total_tokens': 116, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4.1-2025-04-14', 'system_fingerprint': None, 'id': 'chatcmpl-Bs3nnsKZr8r9DOGQ9fPScDwQMJraA', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, 'type': 'ai', 'name': 'react_agent', 'id': 'run--99ee788b-3d53-456e-ae84-d5dcab486b47-0', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 49, 'output_tokens': 67, 'total_tokens': 116, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}}]}}



Updating assistant
Running assistant
Receiving event of type: metadata
{'run_id': '1f05e349-2c2c-69e6-a5dd-561cd00c1b83', 'attempt': 1}



Receiving event of type: updates
{'agent': {'messages': [{'content': 'I was created by a bunch of brilliant (and probably over-caffeinated) engineers and researchers at OpenAI! They programmed me to tell jokes, answer your questions, and occasionally throw in a terrible pun. So, if you don’t like my sense of humor, blame them! 😄', 'additional_kwargs': {'refusal': None}, 'response_metadata': {'token_usage': {'completion_tokens': 60, 'prompt_tokens': 49, 'total_tokens': 109, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4.1-2025-04-14', 'system_fingerprint': None, 'id': 'chatcmpl-Bs3nuxKWEIc5ONbzJhevOAdAL98lY', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, 'type': 'ai', 'name': 'react_agent', 'id': 'run--d190fc7d-c46e-40c1-aec9-af1988e2e042-0', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 49, 'output_tokens': 60, 'total_tokens': 109, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}}]}}



Running assistant
Receiving event of type: metadata
{'run_id': '1f05e349-413b-6ba0-84f8-7e4b81d5e311', 'attempt': 1}



Receiving event of type: updates
{'agent': {'messages': [{'content': 'I was created by OpenAI, an artificial intelligence research organization. My architecture is based on the GPT-4 model, which has been trained and developed by researchers, engineers, and scientists at OpenAI. If you have more detailed questions about AI, my development, or OpenAI itself, feel free to ask!', 'additional_kwargs': {'refusal': None}, 'response_metadata': {'token_usage': {'completion_tokens': 64, 'prompt_tokens': 49, 'total_tokens': 113, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4.1-2025-04-14', 'system_fingerprint': None, 'id': 'chatcmpl-Bs3nwnarzZFyK0h9IPeXezdP1I5b6', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, 'type': 'ai', 'name': 'react_agent', 'id': 'run--06591015-df85-457a-b3d9-1bf18e6f3018-0', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 49, 'output_tokens': 64, 'total_tokens': 113, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}}]}}
```

> More about LangGraph CLI [here](https://langchain-ai.github.io/langgraph/cloud/reference/cli/).


### Setup Model

The defaults values for `model` are shown below:

```yaml
model: anthropic/claude-3-5-sonnet-latest
```

Follow the instructions below to get set up, or pick one of the additional options.

#### Anthropic

To use Anthropic's chat models:

1. Sign up for an [Anthropic API key](https://console.anthropic.com/) if you haven't already.
2. Once you have your API key, add it to your `.env` file:

```
ANTHROPIC_API_KEY=your-api-key
```
#### OpenAI

To use OpenAI's chat models:

1. Sign up for an [OpenAI API key](https://platform.openai.com/signup).
2. Once you have your API key, add it to your `.env` file:
```
OPENAI_API_KEY=your-api-key
```

<!--
End setup instructions
-->

4. Customize whatever you'd like in the code.
5. Open the folder in LangGraph Studio!

## Exploring the Configuration Patterns

### Start with No Configuration
Examine `agents/react_agent/graph_without_config.py` to see the hardcoded baseline.

### Add Single Agent Configuration  
Look at `agents/react_agent/graph.py` to see how configuration is added while keeping the code simple.

### Scale to Multi-Agent Configuration
Explore `agents/supervisor/` to see how the same configuration patterns work with multiple specialized agents.

## Development

### Configuration Best Practices Shown

- **Direct dictionary access** over complex configuration classes
- **Default values** for graceful fallbacks  
- **Consistent patterns** across different complexity levels
- **Runtime flexibility** without architectural complexity

### Local Development

While iterating on your configuration:
- Test different models and prompts via configuration
- Add new tools by updating the `selected_tools` list
- Create new agent types using the same configuration pattern
- Debug configuration issues in LangGraph Studio

## Documentation

You can find the latest LangGraph documentation [here](https://github.com/langchain-ai/langgraph), including examples and references for configuration patterns.

LangGraph Studio integrates with [LangSmith](https://smith.langchain.com/) for comprehensive tracing and team collaboration.

## Configuration Philosophy

This demo shows that **good configuration doesn't have to be complex**:
- Start with hardcoded values for rapid prototyping
- Add simple dictionary-based configuration for flexibility
- Scale the same patterns to multi-agent architectures
- Keep it simple - avoid over-engineering configuration systems

Perfect for learning how to build configurable AI systems that remain maintainable as they grow!

<!--
Configuration auto-generated by `langgraph template lock`. DO NOT EDIT MANUALLY.
{
  "config_schemas": {
    "agent": {
      "type": "object",
      "properties": {
        "model": {
          "type": "string",
          "default": "anthropic/claude-3-5-sonnet-20240620",
          "description": "The name of the language model to use for the agent's main interactions. Should be in the form: provider/model-name.",
          "environment": [
            {
              "value": "anthropic/claude-1.2",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "anthropic/claude-2.0",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "anthropic/claude-2.1",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "anthropic/claude-3-5-sonnet-20240620",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "anthropic/claude-3-haiku-20240307",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "anthropic/claude-3-opus-20240229",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "anthropic/claude-3-sonnet-20240229",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "anthropic/claude-instant-1.2",
              "variables": "ANTHROPIC_API_KEY"
            },
            {
              "value": "openai/gpt-3.5-turbo",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-3.5-turbo-0125",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-3.5-turbo-0301",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-3.5-turbo-0613",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-3.5-turbo-1106",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-3.5-turbo-16k",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-3.5-turbo-16k-0613",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-0125-preview",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-0314",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-0613",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-1106-preview",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-32k",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-32k-0314",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-32k-0613",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-turbo",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-turbo-preview",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4-vision-preview",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4o",
              "variables": "OPENAI_API_KEY"
            },
            {
              "value": "openai/gpt-4o-mini",
              "variables": "OPENAI_API_KEY"
            }
          ]
        }
      },
      "environment": [
        "TAVILY_API_KEY"
      ]
    }
  }
}
-->