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

4. Expected output:
```shell
╭──────────────────────────────────────────────────────────────────────────────────── New run ────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                                                                                                 │
│ How many seconds would it take for a leopard at full speed to run through Pont des Arts?                                                                                        │
│                                                                                                                                                                                 │
╰─ HfApiModel - Qwen/Qwen2.5-Coder-32B-Instruct ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  # Gather information about the length of Pont des Arts                                                                                                                           
  pont_des_arts_length_info = web_search(query="what is the length of Pont des Arts")                                                                                              
                                                                                                                                                                                   
  # Gather information about the top speed of a leopard                                                                                                                            
  leopard_speed_info = web_search(query="top speed of a leopard")                                                                                                                  
  print("Pont des Arts Length Info:", pont_des_arts_length_info)                                                                                                                   
  print("Leopard Speed Info:", leopard_speed_info)                                                                                                                                 
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Execution logs:
Pont des Arts Length Info: ## Search Results

[Pont des Arts - Wikipedia](https://en.wikipedia.org/wiki/Pont_des_Arts)
The Pont des Arts (French pronunciation: [pɔ̃ dez‿aʁ]) or Passerelle des Arts ([pasʁɛl-]) is a pedestrian bridge in Paris which crosses the River Seine. It links the Institut de 
France and the central square ( cour carrée ) of the Palais du Louvre , (which had been termed the "Palais des Arts" under the First French Empire ).
...
[How Fast Can a Leopard Run (Average Speed) - brotherspets.com](https://brotherspets.com/how-fast-can-a-leopard-run/)
Leopards are known for their speed and agility, and they are capable of reaching impressive top speeds when they need to. According to various sources, leopards can run at speeds 
ranging from 30-56 mph (48-90 km/h) with an average speed of 58 km/h.

Out: None
[Step 0: Duration 9.44 seconds| Input tokens: 2,086 | Output tokens: 132]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 2 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  # Constants                                                                                                                                                                      
  distance = 155  # length of Pont des Arts in meters                                                                                                                              
  leopard_speed_kmh = 58  # top speed of a leopard in km/h                                                                                                                         
                                                                                                                                                                                   
  # Convert speed from km/h to m/s                                                                                                                                                 
  leopard_speed_ms = leopard_speed_kmh * (5 / 18)                                                                                                                                  
                                                                                                                                                                                   
  # Calculate time in seconds                                                                                                                                                      
  time_seconds = distance / leopard_speed_ms                                                                                                                                       
  final_answer(time_seconds)                                                                                                                                                       
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Out - Final answer: 9.620689655172415
[Step 1: Duration 7.81 seconds| Input tokens: 6,775 | Output tokens: 423]
```


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