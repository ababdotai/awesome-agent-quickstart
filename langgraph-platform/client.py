import asyncio
from langgraph_sdk import get_client

# replace url with API url after langgraph up (locally) or LangGraph Platform (remotely)
client = get_client(url="http://localhost:8123")

openai_assistant = None


async def create_assistant():
    print("Creating assistant")
    assistant = await client.assistants.create(
        "react_agent", config={"configurable": {
            "model_name": "openai/gpt-4.1-mini",
            "system_prompt": "You are a helpful assistant."
        }},
        name="Open AI Assistant"
    )
    return assistant


async def update_assistant(assistant):
    print("Updating assistant")
    assistant_v2 = await client.assistants.update(
        assistant["assistant_id"],
        config={
            "configurable": {
                "model_name": "openai/gpt-4.1",
                "system_prompt": "You are a funny assistant!",
            }
        },
    )
    return assistant_v2


async def run_assistant(assistant):
    print("Running assistant")
    thread = await client.threads.create()
    input = {"messages": [{"role": "user", "content": "who made you?"}]}
    async for event in client.runs.stream(
        thread["thread_id"],
        # this is where we specify the assistant id to use
        assistant["assistant_id"],
        input=input,
        stream_mode="updates",
    ):
        print(f"Receiving event of type: {event.event}")
        print(event.data)
        print("\n\n")


async def main():
    global openai_assistant
    if openai_assistant is None:
        openai_assistant = await create_assistant()
    await run_assistant(openai_assistant)
    openai_assistant = await update_assistant(openai_assistant)
    await run_assistant(openai_assistant)
    await client.assistants.set_latest(openai_assistant['assistant_id'], 1)
    await run_assistant(openai_assistant)

if __name__ == "__main__":
    asyncio.run(main())
