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

3. Run the code:
```shell
python helloworld.py
```

Example output:

```shell
CodeExecutionResult(result=None, stdout='Loading numpyLoaded numpy[1 2 3]', stderr=None, status='success', execution_time=1.5542199611663818, session_metadata={'created': '2025-06-07T06:21:49.539Z', 'lastModified': '2025-06-07T06:21:50.015Z', 'packages': ['numpy']}, session_bytes=None)
Loading numpyLoaded numpy[1 2 3]
```

# References

- [GitHub Repository](https://github.com/langchain-ai/langchain-sandbox)
