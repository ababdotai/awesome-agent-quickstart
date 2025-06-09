# 🛡️ LangChain Sandbox

A secure environment for running Python code using Pyodide (WebAssembly) and Deno.

## Features
The sandbox consists of two main components:

- `pyodide-sandbox-js`: JavaScript/TypeScript module using Deno to provide the core sandboxing functionality.
- `sandbox-py`: Contains `PyodideSandbox` which just wraps the JavaScript/TypeScript module and executes it as a subprocess.


## 🚀 Quick Start

1. Install Node.js and Deno (required): https://docs.deno.com/runtime/getting_started/installation/

```bash
npm install -g deno
```

2. Install dependencies:
  
```bash
pip install -r requirements.txt
```

3. Run code in the sandbox independently:
```shell
python helloworld.py
# or helloworld_stateful.py
```

Example output:

```shell
CodeExecutionResult(result=None, stdout='Loading numpyLoaded numpy[1 2 3]', stderr=None, status='success', execution_time=1.5542199611663818, session_metadata={'created': '2025-06-07T06:21:49.539Z', 'lastModified': '2025-06-07T06:21:50.015Z', 'packages': ['numpy']}, session_bytes=None)
Loading numpyLoaded numpy[1 2 3]
```

# References

- [GitHub Repository](https://github.com/langchain-ai/langchain-sandbox)

4. Run the sandbox as a tool for agent:
```shell
python tool_react.py
# or tool_codeact.py
# or stateful_tool_react.py
```

Example output:

```shell
{'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_BdlVK2dByXS0rCsfPyTfaqP7', 'function': {'arguments': '{"code":"import math\\nradius = 5\\narea = math.pi * (radius ** 2)\\nprint(area)"}', 'name': 'python_code_sandbox'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 38, 'prompt_tokens': 121, 'total_tokens': 159, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': None, 'id': 'chatcmpl-BgN62muHRjLcBvqN54mj4E3f2rTju', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run--63fa3547-d17f-49b7-8a1e-5af3f2a92e94-0', tool_calls=[{'name': 'python_code_sandbox', 'args': {'code': 'import math\nradius = 5\narea = math.pi * (radius ** 2)\nprint(area)'}, 'id': 'call_BdlVK2dByXS0rCsfPyTfaqP7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 121, 'output_tokens': 38, 'total_tokens': 159, 'input_token_details': {}, 'output_token_details': {}})]}}


{'tools': {'messages': [ToolMessage(content='78.53981633974483', name='python_code_sandbox', id='b2965f55-bdf1-47f7-bad4-d47069023d37', tool_call_id='call_BdlVK2dByXS0rCsfPyTfaqP7')]}}


{'agent': {'messages': [AIMessage(content='The area of a circle with a radius of 5 is approximately 78.54.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 176, 'total_tokens': 195, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': None, 'id': 'chatcmpl-BgN655VPIN4K9HDoJyXX0bpkqsX4F', 'finish_reason': 'stop', 'logprobs': None}, id='run--e5dac62d-6c8b-4185-9b19-48579f534751-0', usage_metadata={'input_tokens': 176, 'output_tokens': 19, 'total_tokens': 195, 'input_token_details': {}, 'output_token_details': {}})]}}
```