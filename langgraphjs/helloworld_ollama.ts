/**
 * A minimal example of using LangGraph.js to create a simple ReAct agent.
 * This example demonstrates the basic concepts of LangGraph including:
 * - Creating a stateful agent
 * - Using tools
 * - Graph-based workflow
 * - State management
 */
import { ChatOllama } from "@langchain/ollama";
import { createReactAgent } from "@langchain/langgraph/prebuilt";
import { MemorySaver } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";
import dotenv from "dotenv";

// Load environment variables from .env file
dotenv.config();

// Get configuration from environment variables
const MODEL_NAME = process.env.MODEL_NAME || "qwen2.5"; // model must support tools
const TEMPERATURE = parseFloat(process.env.TEMPERATURE || "0.7");
const OLLAMA_BASE_URL = process.env.OLLAMA_BASE_URL || "http://localhost:11434";

// Define a simple search tool
const search = tool(
  async ({ query }) => {
    // This is a mock implementation
    if (query.toLowerCase().includes("weather")) {
      return "It's currently sunny and 75°F.";
    }
    return "No relevant information found.";
  },
  {
    name: "search",
    description: "Search for real-time information.",
    schema: z.object({
      query: z.string().describe("The search query to use."),
    }),
  }
);

async function main() {
  try {
    // Initialize the language model
    const model = new ChatOllama({
      model: MODEL_NAME,
      temperature: TEMPERATURE,
      baseUrl: OLLAMA_BASE_URL,
    });

    // Initialize tools
    const tools = [search];

    // Initialize memory for state persistence
    const checkpointer = new MemorySaver();

    // Create the ReAct agent
    const app = createReactAgent({
      llm: model,
      tools,
      checkpointSaver: checkpointer,
    });

    console.log("Agent initialized! Let's have a conversation.\n");

    // First interaction
    const result = await app.invoke(
      {
        messages: [
          {
            role: "user",
            content: "What's the weather like today?",
          },
        ],
      },
      { configurable: { thread_id: "demo-123" } }
    );

    console.log("User: What's the weather like today?");
    console.log(`Assistant: ${result.messages.at(-1)?.content}\n`);

    // Follow-up question with memory
    const followup = await app.invoke(
      {
        messages: [
          {
            role: "user",
            content: "Is that a good temperature?",
          },
        ],
      },
      { configurable: { thread_id: "demo-123" } }
    );

    console.log("User: Is that a good temperature?");
    console.log(`Assistant: ${followup.messages.at(-1)?.content}\n`);

  } catch (error) {
    console.error("Error:", error);
  }
}

main(); 