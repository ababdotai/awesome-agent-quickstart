# LangChain Hello World Example

A minimal example demonstrating how to use LangChain to create a simple conversational agent. This example shows the basic concepts of LangChain including creating a conversational agent, using tools, handling conversations, and basic error handling.

> Note: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows.

## ⚡ Quick Start (5-Minute Setup)

1.  Install dependencies:
```shell
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

3. Run the example:
```shell
python helloworld.py
```

4. Expected output:
```
awesome-agent-quickstart/langchain/helloworld.py:66: LangChainDeprecationWarning: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the `LangGraph documentation <https://langchain-ai.github.io/langgraph/>`_ as well as guides for `Migrating from AgentExecutor <https://python.langchain.com/docs/how_to/migrate_agent/>`_ and LangGraph's `Pre-built ReAct agent <https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/>`_.
  agent = initialize_agent(
Agent initialized! Let's have a conversation.
You can ask questions, and the agent will use web search if needed.
Type 'exit' to end the conversation.

You: Hello
awesome-agent-quickstart/langchain/helloworld.py:100: LangChainDeprecationWarning: The method `Chain.run` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.
  response = agent.run(input=user_input)


> Entering new AgentExecutor chain...
```json
{
    "action": "Final Answer",
    "action_input": "Hello! How can I help you?"
}
```

> Finished chain.

Assistant: Hello! How can I help you?
```