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

1. Navigate to the langgraph directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Set your API key as an environment variable:
```bash
export OPENAI_API_KEY=your_api_key
```

You can also use other LLM providers by configuring the appropriate environment variables supported by LiteLLM.

## Usage

Run the example:
```bash
python helloworld.py
```

The script will:
1. Initialize a simple graph with two nodes
2. Send a test message asking for a joke
3. Print the conversation exchange

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

## License

MIT 