from langchain_sandbox import PyodideSandbox
import asyncio

async def main():
    sandbox = PyodideSandbox(
        # Create stateful sandbox
        stateful=True,
        # Allow Pyodide to install python packages that
        # might be required.
        allow_net=True,
    )
    code = """\
    import numpy as np
    x = np.array([1, 2, 3])
    print(x)
    """

    result = await sandbox.execute(code)

    # Pass previous result
    print(await sandbox.execute("float(x[0])", session_bytes=result.session_bytes, session_metadata=result.session_metadata))

    #  CodeExecutionResult(
    #     result=1, 
    #     stdout=None, 
    #     stderr=None, 
    #     status='success', 
    #     execution_time=2.7027177810668945
    #     session_metadata={'created': '2025-05-15T21:27:57.120Z', 'lastModified': '2025-05-15T21:28:00.061Z', 'packages': ['numpy', 'dill']},
    #     session_bytes=b'\x80\x04\x95d\x01\x00..."
    # )

if __name__ == "__main__":
    asyncio.run(main())