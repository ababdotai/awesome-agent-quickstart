# AutoGen Examples

Welcome to the AutoGen examples! This directory contains ready-to-run examples demonstrating how to use Microsoft AutoGen for building powerful multi-agent systems.

## ⚡ Quick Start (5-Minute Setup)

Let's create your first AutoGen multi-agent system! We'll start with a simple example and then explore more advanced scenarios.

1. Install dependencies:
```bash
cd autogen
pip install -r requirements.txt
```

2. Set up environment:
```bash
cp env.py.example env.py
```

Edit `env.py` with your settings:
```python
# OpenAI API configurations
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1  # Optional: for API proxies
```

3. Run your first multi-agent conversation:
```bash
python helloworld.py
```

## 🚀 Available Examples

1. `helloworld.py` - Basic two-agent conversation
   - Learn the fundamentals of AutoGen
   - See how agents interact with each other
   - Understand basic agent configuration

2. `team.py` - Multi-agent team collaboration
   - Create a team of specialized agents
   - Implement group chat and task delegation
   - Handle complex problem-solving scenarios

## 💡 Key Features

- **Multi-Agent System**: Create multiple agents with different roles
- **Agent Communication**: Enable natural conversations between agents
- **Web Capabilities**: Agents can browse and analyze web content
- **Flexible Configuration**: Easy to customize agent behaviors
- **Error Recovery**: Built-in error handling and conversation recovery

## 🤝 Next Steps
- Explore the examples in order of complexity
- Read the comments in each example for detailed explanations
- Try modifying the examples to understand the concepts better
- Check out the [AutoGen documentation](https://microsoft.github.io/autogen/stable/reference/index.html) for more details

## 📚 Additional Resources

- [AutoGen GitHub Repository](https://github.com/microsoft/autogen)
- [AutoGen Official Documentation](https://microsoft.github.io/autogen/stable/reference/index.html)

## 🛠️ Troubleshooting

1. If you see API key errors:
   - Check if your API key is correctly set in `env.py`
   - Verify your API key has sufficient credits

2. If web browsing fails:
   - Ensure you installed with `pip install 'autogen-ext[web-surfer]'`
   - Check your internet connection
   - Verify the website is accessible

3. For model-specific errors:
   - Try using a different model from your config list
   - Check if your API key has access to the requested model
