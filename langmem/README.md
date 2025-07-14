# LangGraph Memory Hello World Example

A minimal example demonstrating how to use LangMem to create a simple conversational agent that learns and adapts from their interactions over time.

## Features

- Simple conversational agent implementation
- Uses LangGraph's ReAct Agent
- Uses LangMem to manage memory
- Uses LangGraph's InMemoryStore for persistence

## Prerequisites

- Python 3.12+
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
```bash
# OpenAI API configurations
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=  # Optional: custom API endpoint (e.g. for API proxies)
```
3. Run the script:
```bash
python helloworld.py
```

4. Expected output:
```
Your lighting preference is for dark mode in applications and interfaces.
```

# References

- [LangMem docs](https://docs.langchain.com/langmem)
- [LangMem code](https://github.com/langchain-ai/langmem)