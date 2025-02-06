# SmolaGents Examples

Welcome to the SmolaGents examples! This directory contains ready-to-run examples demonstrating how to use SmolaGents for building AI agents.

## ⚡ Quick Start (5-Minute Setup)

Let's create your first SmolaGents agent! We'll start with a simple conversational agent and then explore more advanced examples.

1. Install dependencies:
```bash
cd smolagents
pip install -r requirements.txt
```

2. Set up environment:
```bash
cp env.py.example env.py
```

Edit `env.py` with your settings:
```ini
# OpenAI API configurations
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1  # Optional: for API proxies
```

3. Run your first agent:
```bash
python helloworld.py
```

That's it! You've created your first SmolaGents agent. Let's explore what else you can do!

## 🚀 Available Examples

1. `helloworld.py` - Basic conversational agent
   - Learn the fundamentals of SmolaGents
   - Understand basic agent setup and configuration
   - See how to handle user interactions

2. `multi_agents.py` - Multiple agents working together
   - Create multiple specialized agents
   - Implement agent-to-agent communication
   - Coordinate complex tasks

3. `code_execution.py` - Code execution agent
   - Execute Python code safely
   - Handle code generation and execution
   - Manage execution context and security

4. `any_llm.py` - Model-agnostic example
   - Use different LLM providers
   - Switch between cloud and local models
   - Configure model parameters

## 💡 Key Concepts

- **Agent Configuration**: All examples use the shared `config.py` for model settings
- **Model Flexibility**: Switch between any LLM supported by LiteLLM
- **Error Handling**: Built-in error handling and fallback options
- **Security**: Safe execution environments and API key management

## 🤝 Next Steps

- Explore the examples in order of complexity
- Read the comments in each example for detailed explanations
- Try modifying the examples to understand the concepts better
- Check out the [Smolagents documentation](https://huggingface.co/docs/smolagents/index) for more details

## 📚 Additional Resources

- [Smolagents GitHub Repository](https://github.com/huggingface/smolagents)
- [Smolagents Official Documentation](https://huggingface.co/docs/smolagents/index)