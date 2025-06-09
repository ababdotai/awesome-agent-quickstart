from langchain_sandbox import PyodideSandbox
import asyncio

async def main():
    # Create a sandbox instance
    sandbox = PyodideSandbox(
        # Allow Pyodide to install python packages that
        # might be required.
        allow_net=True,
    )
    code = """\
    import numpy as np
    x = np.array([1, 2, 3])
    print(x)
    """

    # Execute Python code
    response = await sandbox.execute(code)
    print(response)
    
    # Check if execution was successful
    if response.stderr:
        return f"Error during execution: {response.stderr}", {}

    # Get the output from stdout
    output = (
        response.stdout
        if response.stdout
        else "<Code ran, no output printed to stdout>"
    )
    result = response.result

    print(output)
    print(result)

    # CodeExecutionResult(
    #   result=None, 
    #   stdout='[1 2 3]', 
    #   stderr=None, 
    #   status='success', 
    #   execution_time=2.8578367233276367,
    #   session_metadata={'created': '2025-05-15T21:26:37.204Z', 'lastModified': '2025-05-15T21:26:37.831Z', 'packages': ['numpy']},
    #   session_bytes=None
    # )

if __name__ == "__main__":
    asyncio.run(main())