# LangChain MCP Adapters

This library provides a lightweight wrapper that makes [Anthropic Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) tools compatible with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph).

## Features

- 🛠️ Convert MCP tools into [LangChain tools](https://python.langchain.com/docs/concepts/tools/) that can be used with [LangGraph](https://github.com/langchain-ai/langgraph) agents
- 📦 A client implementation that allows you to connect to multiple MCP servers and load tools from them

## Quickstart

1. Copy `.env.example` to `.env`, and set up your config:

```shell
# OpenAI API configurations
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=your_openai_api_base
```

2. Install the dependencies:

```shell
pip install -r requirements.txt
```

3. Run the code:
```shell
python helloworld.py
```

Example output:

```shell

---answer---

 {'messages': [HumanMessage(content='A batter hits a baseball at 45.847 m/s at an angle of 23.474° above the horizontal. The outfielder, who starts facing the batter, picks up the baseball as it lands, then throws it back towards the batter at 24.12 m/s at an angle of 39.12 degrees. How far is the baseball from where the batter originally hit it? Assume zero air resistance.', additional_kwargs={}, response_metadata={}, id='27708279-3aef-4cea-a78f-7dd9fb7f69a8')]}
To solve this problem, we can break down the projectile motion of the baseball hit by the batter and the throw made by the outfielder into their respective horizontal and vertical components.

Let's outline the steps to calculate the distance:

1. **Calculate the initial velocity components of the baseball:**
   - \( V_{x, \text{batter}} = V_{\text{batter}} \cdot \cos(\theta_{\text{batter}}) \)
   - \( V_{y, \text{batter}} = V_{\text{batter}} \cdot \sin(\theta_{\text{batter}}) \)

2. **Calculate the time of flight for the baseball:**
   The time it takes for the baseball to hit the ground can be calculated using the formula: 
   - \( t = \frac{2 \cdot V_{y, \text{batter}}}{g} \)
   Where \( g \) is the acceleration due to gravity, approximately \( 9.81 \, m/s^2 \).

3. **Calculate the horizontal distance traveled by the baseball:**
   - \( D_{\text{baseball}} = V_{x, \text{batter}} \cdot t \)

4. **Calculate the components of the outfielder's throw velocity:**
   - \( V_{x, \text{outfielder}} = V_{\text{outfielder}} \cdot \cos(\theta_{\text{outfielder}}) \)
   - \( V_{y, \text{outfielder}} = V_{\text{outfielder}} \cdot \sin(\theta_{\text{outfielder}}) \)

5. **Calculate the horizontal distance traveled by the outfielder's throw:**
   Since the outfielder catches the baseball at ground level, we can assume the time of flight for the throw back to the batter is similar to the time it takes the baseball to hit the ground.

Now, let's put the calculations into Python code:

```python
import math

# Constants
g = 9.81  # Acceleration due to gravity in m/s^2

# Given data
V_batter = 45.847  # m/s
theta_batter = 23.474  # degrees
V_outfielder = 24.12  # m/s
theta_outfielder = 39.12  # degrees

# Convert angles to radians
theta_batter_rad = math.radians(theta_batter)
theta_outfielder_rad = math.radians(theta_outfielder)

# Step 1: Calculate components of the batter's hit
Vx_batter = V_batter * math.cos(theta_batter_rad)
Vy_batter = V_batter * math.sin(theta_batter_rad)

# Step 2: Calculate time of flight (baseball)
time_of_flight = (2 * Vy_batter) / g

# Step 3: Calculate horizontal distance traveled by the baseball
D_baseball = Vx_batter * time_of_flight

# Step 4: Calculate components of the outfielder's throw
Vx_outfielder = V_outfielder * math.cos(theta_outfielder_rad)
Vy_outfielder = V_outfielder * math.sin(theta_outfielder_rad)

# We can consider the time of flight for the throw back to be the same as the time of flight for the baseball.
# Step 5: Calculate horizontal distance traveled by the outfielder's throw
D_outfielder = Vx_outfielder * time_of_flight

# Total distance from where the batter originally hit the baseball
total_distance = D_baseball + D_outfielder

total_distance
```

Now we can execute the code to find the total distance from the original position of the batter to where the baseball was picked up. Let's run the calculations.


# References

- [GitHub Repo](https://github.com/langchain-ai/langgraph-codeact)
- [CodeAct paper](https://arxiv.org/abs/2402.01030)