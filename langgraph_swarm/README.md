# 🤖 LangGraph Multi-Agent Swarm Example

A demonstration of how to use LangGraph Swarm to create a multi-agent system where specialized agents can collaborate and hand off control to each other based on their expertise. This example shows how to build a swarm-style architecture using LangGraph.

## Features

- 🤖 **Multi-agent collaboration** - Enable specialized agents to work together
- 🛠️ **Customizable handoff tools** - Built-in tools for communication between agents
- 🧠 **State persistence** - Maintain conversation state across multiple interactions
- 🔄 **Dynamic agent routing** - Automatically route to the appropriate specialized agent

## Prerequisites

- Python 3.10+
- OpenAI API key

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
OPENAI_API_KEY=your-api-key-here
```

3. Run the script:
```bash
python helloworld.py
```

4. Expected output:
```
{'messages': [HumanMessage(content="i'd like to speak to Bob", additional_kwargs={}, response_metadata={}, id='7ba5c118-b7a8-495d-833b-566b2cb48555'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_vHpb41yhpeqTu0KjdypfG7od', 'function': {'arguments': '{}', 'name': 'transfer_to_bob'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 77, 'total_tokens': 90, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, name='Alice', id='run-40f0da0b-6f97-4072-b334-f007d2905a1e-0', tool_calls=[{'name': 'transfer_to_bob', 'args': {}, 'id': 'call_vHpb41yhpeqTu0KjdypfG7od', 'type': 'tool_call'}], usage_metadata={'input_tokens': 77, 'output_tokens': 13, 'total_tokens': 90, 'input_token_details': {}, 'output_token_details': {}}), ToolMessage(content='Successfully transferred to Bob', name='transfer_to_bob', id='7325a0ed-4b8c-44ee-a369-8cd9de02a303', tool_call_id='call_vHpb41yhpeqTu0KjdypfG7od'), AIMessage(content="Ahoy, matey! Ye be speakin' to Bob now, the finest pirate in these digital seas. What treasures or troubles bring ye to my humble presence today? Arrr!", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 40, 'prompt_tokens': 88, 'total_tokens': 128, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, name='Bob', id='run-a60be441-4a16-443a-8298-c906a6339e1b-0', usage_metadata={'input_tokens': 88, 'output_tokens': 40, 'total_tokens': 128, 'input_token_details': {}, 'output_token_details': {}})], 'active_agent': 'Bob'}
{'messages': [HumanMessage(content="i'd like to speak to Bob", additional_kwargs={}, response_metadata={}, id='7ba5c118-b7a8-495d-833b-566b2cb48555'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_vHpb41yhpeqTu0KjdypfG7od', 'function': {'arguments': '{}', 'name': 'transfer_to_bob'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 77, 'total_tokens': 90, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, name='Alice', id='run-40f0da0b-6f97-4072-b334-f007d2905a1e-0', tool_calls=[{'name': 'transfer_to_bob', 'args': {}, 'id': 'call_vHpb41yhpeqTu0KjdypfG7od', 'type': 'tool_call'}], usage_metadata={'input_tokens': 77, 'output_tokens': 13, 'total_tokens': 90, 'input_token_details': {}, 'output_token_details': {}}), ToolMessage(content='Successfully transferred to Bob', name='transfer_to_bob', id='7325a0ed-4b8c-44ee-a369-8cd9de02a303', tool_call_id='call_vHpb41yhpeqTu0KjdypfG7od'), AIMessage(content="Ahoy, matey! Ye be speakin' to Bob now, the finest pirate in these digital seas. What treasures or troubles bring ye to my humble presence today? Arrr!", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 40, 'prompt_tokens': 88, 'total_tokens': 128, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, name='Bob', id='run-a60be441-4a16-443a-8298-c906a6339e1b-0', usage_metadata={'input_tokens': 88, 'output_tokens': 40, 'total_tokens': 128, 'input_token_details': {}, 'output_token_details': {}}), HumanMessage(content="what's 5 + 7?", additional_kwargs={}, response_metadata={}, id='5045abf9-d856-4c6e-85fc-10b2414c06dc'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_PHlAyjwcBOMRNivc40CHBCsB', 'function': {'arguments': '{}', 'name': 'transfer_to_alice'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 144, 'total_tokens': 157, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, name='Bob', id='run-45e2eafe-b008-4b74-8fa5-28d353016d0c-0', tool_calls=[{'name': 'transfer_to_alice', 'args': {}, 'id': 'call_PHlAyjwcBOMRNivc40CHBCsB', 'type': 'tool_call'}], usage_metadata={'input_tokens': 144, 'output_tokens': 13, 'total_tokens': 157, 'input_token_details': {}, 'output_token_details': {}}), ToolMessage(content='Successfully transferred to Alice', name='transfer_to_alice', id='f6199050-d8c3-4218-8cb5-43076eb7e3f6', tool_call_id='call_PHlAyjwcBOMRNivc40CHBCsB'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uxtttnGs1JnSAMhs2G5NSlfE', 'function': {'arguments': '{"a":5,"b":7}', 'name': 'add'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 189, 'total_tokens': 207, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, name='Alice', id='run-b96b0597-15e6-4b80-86c1-46fb48147e06-0', tool_calls=[{'name': 'add', 'args': {'a': 5, 'b': 7}, 'id': 'call_uxtttnGs1JnSAMhs2G5NSlfE', 'type': 'tool_call'}], usage_metadata={'input_tokens': 189, 'output_tokens': 18, 'total_tokens': 207, 'input_token_details': {}, 'output_token_details': {}}), ToolMessage(content='12', name='add', id='1172b8d2-0f26-4ae9-9209-f7f9b0eb3975', tool_call_id='call_uxtttnGs1JnSAMhs2G5NSlfE'), AIMessage(content='The sum of 5 and 7 is 12.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 216, 'total_tokens': 230, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, name='Alice', id='run-f3400b53-915e-4913-8a4c-7dffc97249e2-0', usage_metadata={'input_tokens': 216, 'output_tokens': 14, 'total_tokens': 230, 'input_token_details': {}, 'output_token_details': {}})], 'active_agent': 'Alice'}
```

## Code Structure

- `helloworld.py`: Main implementation file
  - Creates two agents: Alice (math expert) and Bob (speaks like a pirate)
  - Implements a custom `add` tool for Alice
  - Sets up handoff tools for inter-agent communication
  - Creates a swarm workflow with `create_swarm`
  - Uses `InMemorySaver` for state persistence

## How It Works

The example demonstrates a swarm architecture where:
1. Alice is the default agent and can handle math calculations
2. Bob speaks like a pirate
3. Agents can hand off control to each other using `create_handoff_tool`
4. The system remembers which agent was last active
5. Conversation history is preserved across interactions

## Extending the Example

You can extend this example by:
- Adding more specialized agents to the swarm
- Creating custom handoff tools with additional parameters
- Implementing a more complex state schema
- Adding long-term memory with a store

## Important Notes

- Always compile the swarm with a checkpointer to maintain conversation state
- All agents in the default implementation share a single messages history
- For more complex customization, see the [customizing agent implementation](https://github.com/langchain-ai/langgraph-swarm/blob/main/README.md#customizing-agent-implementation) section