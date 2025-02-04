# awesome-agent-quickstart
Your fast lane to AI Agent development! This repository helps you bypass setup complexities and dive straight into latest AI Agent frameworks. Go from zero to running your first agent in minutes, whether you're interested in LangGraph, AutoGen, Smolagents, or other popular frameworks.

## 🎯 Features

- ⚡ Zero configuration needed - start coding in minutes
- 🎓 Learn by example - all examples are runnable
- 🔄 Model-agnostic - support any LLM (via LiteLLM)
- 🛠️ Centralized configuration - shared settings across frameworks

## 🚀 Supported Frameworks

Ready-to-run templates for:

- LangGraph
- AutoGen
- Smolagents
- CrewAI
- More coming soon...

## 📁 Project Structure

```
awesome-agent-quickstart/
├── langgraph/                 # LangGraph framework examples
│   ├── config.py             # Common configurations (model params, API settings&checking)
│   ├── helloworld.py         # Basic example: Simple conversational agent
│   ├── requirements.txt      # Dependency management
│   └── .env.example         # Environment variables template
```

## ⚡ Quick Start

## ⚙️ Configuration

All examples use common configurations from `config.py`, including:
- Model parameters (model name, temperature, etc.)
- API configurations (API key, base URL)
- Environment variable management (using python-dotenv)

Key configurations:
- `DEFAULT_MODEL`: Default model to use
- `DEFAULT_TEMPERATURE`: Model temperature parameter
- `OPENAI_API_KEY`: API key
- `OPENAI_API_BASE`: API base URL (if using proxy)


### LangGraph

1. Clone and install dependencies:
```bash
git clone https://github.com/yourusername/awesome-agent-quickstart.git
cd awesome-agent-quickstart/langgraph
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
```

Edit `.env` file with your settings:
```
# LLM Model configurations
DEFAULT_MODEL=your-model-name
DEFAULT_TEMPERATURE=0.7

# OpenAI API configurations
OPENAI_API_KEY=your-api-key
OPENAI_API_BASE=your-api-base-url  # Optional: include /v1 if using API proxy
```

3. Run the helloworld example (how to create a simple conversational agent using LangGraph):
```bash
python helloworld.py
```

## ⚠️ Important Notes

1. Ensure `.env` file is properly configured before running examples
2. API keys and other sensitive information are added to `.gitignore`
3. If using a proxy, ensure `OPENAI_API_BASE` includes the complete API path (e.g., `https://your-proxy.com/v1`)
4. All examples support custom model parameters that can override defaults at runtime


## 🤝 Contributing

Contributions for more agent framework examples are welcome! Please ensure:
1. Create examples under the respective framework directory
2. Use common configurations from `config.py`
3. Provide clear documentation and comments
4. Include `requirements.txt` and `.env.example`
5. Follow project code style and best practices

## 📝 Development Guidelines

1. Code Structure
   - Follow modular design
   - Separate configuration from logic
   - Include proper error handling
   - Keep dependency files up-to-date

2. Documentation
   - Add docstrings for main functions and classes
   - Include usage examples
   - Explain key concepts and design decisions

3. Security
   - Use environment variables for sensitive data
   - Include rate limiting considerations
   - Add proper input validation

See [Contributing Guidelines](CONTRIBUTING.md) for more details.

## 📃 License

MIT License - see [LICENSE](LICENSE)

## 🌟 Community

- ⭐ Star us on GitHub
- 🐛 [Report issues](https://github.com/yourusername/awesome-agent-quickstart/issues)
- 💬 [Join Discord](https://discord.gg/yourdiscord)
- 📧 Contact: your.email@example.com

## 🙏 Acknowledgments

Made with ❤️ by the AI community, for the AI community.

- Thanks to all contributors
- Thanks to the framework development teams
- Thanks to the AI/ML community