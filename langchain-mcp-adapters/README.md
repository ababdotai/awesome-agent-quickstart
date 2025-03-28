# LangChain MCP Adapters

This library provides a lightweight wrapper that makes [Anthropic Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) tools compatible with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph).

## Features

- 🛠️ Convert MCP tools into [LangChain tools](https://python.langchain.com/docs/concepts/tools/) that can be used with [LangGraph](https://github.com/langchain-ai/langgraph) agents
- 📦 A client implementation that allows you to connect to multiple MCP servers and load tools from them

## Quickstart

1. Copy `.env.example` to `.env`, and set up your config:

```shell
# OpenAI API configurations
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=your_openai_api_base

NO_PROXY=localhost,127.0.0.1

# MCP server configurations
MCP_SERVER_PORT=8000
MCP_SERVER_LOG_LEVEL=INFO
```

2. Install the dependencies:

```shell
pip install -r requirements.txt
```

3. Run the single server example:
```shell
# client talk to server through stdio, server will be started by the client
python clients/single_server_client.py
```

Example output:
```json
{
   "messages":[
      "HumanMessage(content=""what's (3 + 5) x 12?",
      "additional_kwargs="{
         
      },
      "response_metadata="{
         
      },
      "id=""0573b0c0-8403-4bce-8e7c-c0a3543adcd3"")",
      "AIMessage(content=""",
      "additional_kwargs="{
         "tool_calls":[
            {
               "id":"call_JUnJ3w9uSTk9TjIjwS79sbf6",
               "function":{
                  "arguments":"{\"a\": 3, \"b\": 5}",
                  "name":"add"
               },
               "type":"function"
            },
            {
               "id":"call_7vl88I06X2L8MIDjqtk34Fqk",
               "function":{
                  "arguments":"{\"a\": 8, \"b\": 12}",
                  "name":"multiply"
               },
               "type":"function"
            }
         ],
         "refusal":"None"
      },
      "response_metadata="{
         "token_usage":{
            "completion_tokens":51,
            "prompt_tokens":77,
            "total_tokens":128,
            "completion_tokens_details":"None",
            "prompt_tokens_details":"None"
         },
         "model_name":"gpt-4o-2024-08-06",
         "system_fingerprint":"None",
         "id":"chatcmpl-BFxR34FDYotSpoff4StmvcWNm2waO",
         "finish_reason":"tool_calls",
         "logprobs":"None"
      },
      "id=""run-5a053b8e-9f2e-4742-9836-8d7173a89656-0",
      "tool_calls="[
         {
            "name":"add",
            "args":{
               "a":3,
               "b":5
            },
            "id":"call_JUnJ3w9uSTk9TjIjwS79sbf6",
            "type":"tool_call"
         },
         {
            "name":"multiply",
            "args":{
               "a":8,
               "b":12
            },
            "id":"call_7vl88I06X2L8MIDjqtk34Fqk",
            "type":"tool_call"
         }
      ],
      "usage_metadata="{
         "input_tokens":77,
         "output_tokens":51,
         "total_tokens":128,
         "input_token_details":{
            
         },
         "output_token_details":{
            
         }
      }")",
      "ToolMessage(content=""8",
      "name=""add",
      "id=""e05a3e7e-570d-49c9-96f4-4746651f2e2c",
      "tool_call_id=""call_JUnJ3w9uSTk9TjIjwS79sbf6"")",
      "ToolMessage(content=""96",
      "name=""multiply",
      "id=""c7499b42-9ca9-4b1b-8f03-a0730ab7e270",
      "tool_call_id=""call_7vl88I06X2L8MIDjqtk34Fqk"")",
      "AIMessage(content=""The result of (3 + 5) × 12 is 96.",
      "additional_kwargs="{
         "refusal":"None"
      },
      "response_metadata="{
         "token_usage":{
            "completion_tokens":18,
            "prompt_tokens":143,
            "total_tokens":161,
            "completion_tokens_details":"None",
            "prompt_tokens_details":"None"
         },
         "model_name":"gpt-4o-2024-08-06",
         "system_fingerprint":"None",
         "id":"chatcmpl-BFxR4InEu1Fi0gdMcmfBhRE8Yn9PB",
         "finish_reason":"stop",
         "logprobs":"None"
      },
      "id=""run-475ead2f-6c5b-4f6d-b1f6-c9405deb4edd-0",
      "usage_metadata="{
         "input_tokens":143,
         "output_tokens":18,
         "total_tokens":161,
         "input_token_details":{
            
         },
         "output_token_details":{
            
         }
      }")"
   ]
}

The result of \((3 + 5) \times 12\) is 96.
```

4. Run the multiple servers example:

```shell
# start weather server via SSE
python servers/weather_server.py

INFO:     Started server process [28417]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
```

```shell
# client talk to both servers
python clients/multi_server_client.py
```

Example output in client (here we only print the final result):
```shell
The result of \((3 + 5) \times 12\) is 96.
The weather in New York City is described as "always sunny."
```

Example output in server:
```shell
INFO:     127.0.0.1:55941 - "GET /sse HTTP/1.1" 200 OK
INFO:     127.0.0.1:55943 - "POST /messages/?session_id=cb4481fbe7094d17a1a8b3025c6bbbde HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:55943 - "POST /messages/?session_id=cb4481fbe7094d17a1a8b3025c6bbbde HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:55943 - "POST /messages/?session_id=cb4481fbe7094d17a1a8b3025c6bbbde HTTP/1.1" 202 Accepted
Processing request of type ListToolsRequest
INFO:     127.0.0.1:55943 - "POST /messages/?session_id=cb4481fbe7094d17a1a8b3025c6bbbde HTTP/1.1" 202 Accepted
Processing request of type CallToolRequest
```

