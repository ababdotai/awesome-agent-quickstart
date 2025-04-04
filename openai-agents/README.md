# OpenAI Agents SDK

The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows.

### Core concepts:

1. [**Agents**](https://openai.github.io/openai-agents-python/agents): LLMs configured with instructions, tools, guardrails, and handoffs
2. [**Handoffs**](https://openai.github.io/openai-agents-python/handoffs/): A specialized tool call used by the Agents SDK for transferring control between agents
3. [**Guardrails**](https://openai.github.io/openai-agents-python/guardrails/): Configurable safety checks for input and output validation
4. [**Tracing**](https://openai.github.io/openai-agents-python/tracing/): Built-in tracking of agent runs, allowing you to view, debug and optimize your workflows

## Quickstart

1. Copy `.env.example` to `.env`, and set up your config:

```shell
# OpenAI API configurations
OPENAI_API_KEY=your_openai_api_key
```

2. Install the dependencies:

```shell
pip install -r requirements.txt
```

For voice support, install with the optional `voice` group: `pip install 'openai-agents[voice]'`.

3. Run the hello world example:

```shell
python helloworld.py
```

4. Example output:

```shell
Code within the code,
Functions calling themselves,
Infinite loop's dance.
```

