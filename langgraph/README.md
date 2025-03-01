# LangGraph Hello World Example

A minimal example demonstrating how to use LangGraph to create a simple conversational agent. This example shows the basic concepts of LangGraph including creating nodes, building a graph, handling state, and running an agent.

## Features

- Simple conversational agent implementation
- Basic graph structure with two nodes
- Error handling and state management
- Model-agnostic design using LiteLLM

## Prerequisites

- Python 3.9+
- OpenAI API key or compatible API key for other LLMs

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Set up environment:
```bash
cp .env.example .env
```

Edit `.env` with your settings:
```ini
# LLM Model configurations
DEFAULT_MODEL=gpt-4o-mini
DEFAULT_TEMPERATURE=0.7

# OpenAI API configurations
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1  # Optional: custom API endpoint (e.g. for API proxies)
```
3. Run the script:
```bash
python helloworld.py
```

4. Expected output:
```
User: Tell me a short joke
Assistant: Why did the scarecrow win an award? Because he was outstanding in his field!
```

## Code Structure

- `helloworld.py`: Main implementation file
  - `AgentState`: Defines the state structure
  - `get_llm_response()`: Node for getting LLM responses
  - `format_response()`: Node for formatting and updating state
  - `build_graph()`: Creates and configures the graph
  - `main()`: Entry point and execution logic

## Extending the Example

You can extend this example by:
- Adding more nodes to the graph
- Implementing more complex state management
- Adding different types of interactions
- Integrating with other LLM providers

## Error Handling

The example includes basic error handling:
- Checks for required environment variables
- Handles LLM API errors gracefully
- Maintains state consistency