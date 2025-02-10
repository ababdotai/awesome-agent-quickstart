# Swarm Examples

Welcome to the Swarm examples! This directory contains ready-to-run examples demonstrating how to use Swarm for building decentralized multi-agent systems with emergent behaviors.

## ⚡ Quick Start (5-Minute Setup)

Let's create your first Swarm agent system! We'll start with a simple example and then explore more advanced scenarios.

1. Install dependencies:
```bash
cd swarm
pip install -r requirements.txt
```

2. Set up environment:
```bash
cp env.py.example env.py
```

Edit `env.py` with your settings:
```python
# OpenAI API configurations
OPENAI_API_KEY = "your-api-key-here"
```

3. Run your first swarm:
```bash
python helloworld.py
```

4. Expected output:
```shell
Hope glimmers brightly,
New paths converge gracefully,
What can I assist?
```

## 🚀 Available Examples

1. `helloworld.py` - Basic swarm behavior
   - Learn the fundamentals of Swarm
   - Understand agent communication patterns
   - See emergent behavior in action

2. `collaborative_task.py` - Multi-agent collaboration
   - Create a swarm of specialized agents
   - Implement decentralized task distribution
   - Handle complex problem-solving scenarios

3. `emergent_behavior.py` - Emergent intelligence
   - Observe collective intelligence
   - Study swarm dynamics
   - Analyze group decision making

## 💡 Key Features

- **Decentralized System**: Create autonomous agents that work together
- **Emergent Behavior**: Watch collective intelligence emerge from simple rules
- **Scalable Architecture**: Easy to add or remove agents dynamically
- **Flexible Configuration**: Customize agent behaviors and interactions
- **Fault Tolerance**: Built-in resilience through decentralization

## 🔧 Customization

1. Configure agent behavior:
```python
from swarm import Agent, Behavior

class CustomBehavior(Behavior):
    def act(self, context):
        # Define agent behavior here
        pass

agent = Agent(behavior=CustomBehavior())
```

2. Adjust swarm parameters:
```python
from swarm import Swarm

swarm = Swarm(
    num_agents=10,
    communication_range=2,
    decision_threshold=0.7
)
```

3. Define interaction rules:
```python
def interaction_rule(agent1, agent2):
    # Define how agents interact
    pass

swarm.set_interaction_rule(interaction_rule)
```

## ⚠️ Important Notes

1. Ensure `env.py` is properly configured before running examples
2. API keys and sensitive information are added to `.gitignore`
3. Some examples may require specific model capabilities
4. Monitor resource usage when running large swarms

## 🤝 Next Steps

- Start with `helloworld.py` to understand basic concepts
- Experiment with different swarm sizes and behaviors
- Try creating custom agent behaviors
- Explore emergent patterns in larger swarms

## 📚 Additional Resources

- [Swarm GitHub Repository](https://github.com/openai/swarm)
- [Community Examples](https://github.com/openai/swarm/tree/main/examples)
- [OpenAI API Documentation](https://platform.openai.com/docs/quickstart?language=python)

## 🛠️ Troubleshooting

1. Installation Issues:
   - Check Python version (3.10+ required)
   - Verify all dependencies are installed
   - Try creating a fresh virtual environment (conda recommended)

2. API Errors:
   - Verify API key in `env.py`
   - Ensure sufficient API credits

3. Performance Issues:
   - Reduce swarm size for testing
   - Monitor memory usage
   - Check network connectivity
