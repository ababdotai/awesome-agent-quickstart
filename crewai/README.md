# CrewAI Examples

Welcome to the CrewAI examples! This directory contains ready-to-run examples demonstrating how to use CrewAI for building collaborative AI agent teams. CrewAI makes it easy to create agents that work together like a well-organized crew.

## ⚡ Quick Start (5-Minute Setup)

Let's create your first AI crew! We'll start with a simple example and then explore more advanced scenarios.

1. Install uv (Fast Python Package Installer):
```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# OR via pip
pip install uv
```

2. Install dependencies:
```bash
cd helloworld
python -m venv .venv
# Linux/macOS
source .venv/bin/activate 
# Windows: 
.venv\Scripts\activate

uv pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
```

Edit `.env` with your settings:
```ini
MODEL=your-chosen-model

# OpenAI API configurations
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1  # Optional: for API proxies
```

4. Run your first crew:
```bash
crewai run
```

5. Expected Output

When running the helloworld example, you'll see something like:
```shell
Running the Crew
# Agent: AI LLMs Senior Data Researcher
## Task: Conduct a thorough research about AI LLMs Make sure you find any interesting and relevant information given the current year is 2025.

# Agent: AI LLMs Senior Data Researcher
## Final Answer: 
...

# Agent: AI LLMs Reporting Analyst
## Task: Review the context you got and expand each topic into a full section for a report. Make sure the report is detailed and contains any and all relevant information.
...
```

That's it! You'll see your AI crew working together to accomplish the task!

> Remember to manually exit the venv with `deactivate` to switch to other frameworks.

## 🚀 Available Examples

1. `helloworld/` - Basic research crew
   - Learn the fundamentals of CrewAI
   - See how agents collaborate in a crew
   - Understand role-based task delegation

2. `research_crew/` - Advanced research team
   - Create specialized research agents
   - Implement hierarchical task breakdown
   - Handle complex research scenarios

3. `coding_crew/` - Software development team
   - Code generation and review
   - Technical documentation
   - Project planning and estimation

4. `custom_tools/` - Tool integration example
   - Create custom agent tools
   - Integrate external APIs
   - Enhance agent capabilities

## 💡 Key Features

- **Role-Based Agents**: Create agents with specific roles and expertise
- **Hierarchical Task Management**: Break down complex tasks into manageable subtasks
- **Tool Integration**: Extend agent capabilities with custom tools
- **Process Automation**: Automate complex workflows with agent collaboration
- **Flexible Configuration**: Easy to customize agent behaviors and crew composition

## 🔧 Customization

1. Configure agent roles in `config/agents.yaml`:
```yaml
researcher:
  role: "AI LLMs Senior Data Researcher"
  goal: "Conduct thorough research about AI LLMs"
  backstory: "You are an experienced AI researcher..."

analyst:
  role: "AI LLMs Reporting Analyst"
  goal: "Create comprehensive reports from research"
  backstory: "You are a skilled technical writer..."
```

2. Add custom tools in `tools/`:
```python
from crewai import Tool

class CustomResearchTool(Tool):
    def search_papers(self, query: str) -> str:
        # Implement paper search logic
        pass
```

3. Modify crew workflow in `main.py`:
```python
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    process=Process.sequential
)
```

## ⚠️ Important Notes

1. Ensure `.env` file is properly configured before running examples
2. API keys and other sensitive information are added to `.gitignore`
3. Some examples may require specific model capabilities (e.g., GPT-4)
4. Virtual environment is recommended for dependency management

## 🤝 Next Steps

- Start with the `helloworld` example to understand basic concepts
- Explore different agent roles and crew compositions
- Try creating custom tools for specific tasks
- Experiment with different process flows (sequential vs parallel)
- Build your own specialized crews

## 📚 Additional Resources

- [CrewAI GitHub Repository](https://github.com/joaomdmoura/crewAI)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Example Gallery](https://github.com/joaomdmoura/crewAI-examples)