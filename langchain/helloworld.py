"""
A minimal example of using LangChain to create a simple conversational agent.
This example demonstrates the basic concepts of LangChain including:
- Creating a conversational agent
- Using tools
- Handling conversations
- Basic error handling
"""

from typing import List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.memory import BaseMemory
from langchain.agents import AgentType, initialize_agent
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel, Field
from config import get_api_key, get_api_base, get_model_config

class SimpleConversationMemory(BaseMemory, BaseModel):
    """A simple conversation memory implementation."""
    
    chat_history: List[Any] = Field(default_factory=list)
    memory_key: str = Field(default="chat_history")
    return_messages: bool = Field(default=True)
    
    @property
    def memory_variables(self) -> List[str]:
        """Define memory variables."""
        return [self.memory_key]
    
    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Load memory variables."""
        return {self.memory_key: self.chat_history}
    
    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        """Save context from this conversation to memory."""
        if "input" in inputs and "output" in outputs:
            self.chat_history.append(HumanMessage(content=inputs["input"]))
            self.chat_history.append(AIMessage(content=outputs["output"]))
        
    def clear(self) -> None:
        """Clear memory contents."""
        self.chat_history = []

def create_agent():
    """Create a simple conversational agent with web search capability."""
    try:
        # Initialize the language model
        model_config = get_model_config()
        llm = ChatOpenAI(
            api_key=get_api_key(),
            base_url=get_api_base(),
            model_name=model_config["model"],
            temperature=model_config["temperature"]
        )

        # Initialize tools
        tools: List = [
            DuckDuckGoSearchRun(name="web_search")
        ]

        # Initialize conversation memory
        memory = SimpleConversationMemory()

        # Initialize the agent
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=memory,
            verbose=True,
            handle_parsing_errors=True
        )

        return agent
    except Exception as e:
        print(f"Error creating agent: {str(e)}")
        return None

def main():
    """Run a simple conversation with the agent."""
    # Create the agent
    agent = create_agent()
    if not agent:
        return

    print("Agent initialized! Let's have a conversation.")
    print("You can ask questions, and the agent will use web search if needed.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            if user_input.lower() == 'exit':
                print("\nGoodbye! Have a great day!")
                break

            # Get agent's response
            response = agent.run(input=user_input)
            print(f"\nAssistant: {response}\n")

        except KeyboardInterrupt:
            print("\nConversation ended by user. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Let's try again with a different question.\n")

if __name__ == "__main__":
    main() 