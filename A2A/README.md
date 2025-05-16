# Google Agent2Agent Protocol

## Quickstart

1. Setup env for agents:

> Get GOOGLE_API_KEY: https://aistudio.google.com/apikey

- Crewai agent:

```bash
cd agents/crewai
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

- Langgraph agent:

```bash
cd agents/langgraph
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

2. Start the agent servers:

- Crewai agent:
```bash
cd agents/crewai
uv python pin 3.12
uv venv
source .venv/bin/activate
uv run .
INFO:__main__:Starting server on localhost:10001
INFO:     Started server process [53304]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:10001 (Press CTRL+C to quit)
```

- Langgraph agent:
```bash
cd agents/langgraph
uv run .
INFO:__main__:Starting server on localhost:10000
INFO:     Started server process [42606]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:10000 (Press CTRL+C to quit)
```

3. Start the GUI client:
```bash
cd demo/ui
echo "GOOGLE_API_KEY=your_api_key_here" >> .env
# Otherwise, you will enter it directly in the UI everytime
uv run main.py
INFO:     Uvicorn running on http://0.0.0.0:12000 (Press CTRL+C to quit)
WARNING:  --reload-include and --reload-exclude have no effect unless watchfiles is installed.
INFO:     Started reloader process [42916] using StatReload
INFO:     Started server process [43176]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:53827 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:53827 - "GET /zone.js/bundles/zone.umd.js HTTP/1.1" 200 OK
```

4. Open Chrome and navigate to:
```
http://localhost:12000/
```

5. Click _Remote Agents_ tab and input running agent's address (although there is a placeholder, you have to input):

   ```
   localhost:10001
   ```
   Then click _Read_, agents.json will be read and displayed, click _Save_ then.

6. Click _Home_, add a new conversation, then input:
   ```
   What remote agents do you have access to?
   ```
   The connected agents will be listed:
   ```
   I have access to the Currency Agent and the Image Generator Agent.
   ```


## References
- Github Repository: https://github.com/google/A2A/
- Official Website: https://google.github.io/A2A/