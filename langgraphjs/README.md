# LangGraph.js Examples

Welcome to the LangGraph.js examples! This directory contains ready-to-run examples demonstrating how to use LangGraph.js for building stateful, multi-actor applications with LLMs.

## ⚡ Quick Start (5-Minute Setup)

Let's create your first LangGraph.js agent! We'll start with a simple ReAct agent example.

1. Install dependencies:
```bash
npm install
```

2. Configure environment:
```bash
cp .env.example .env
```

Edit `.env` with your settings:
```ini
# Anthropic API Key
ANTHROPIC_API_KEY=your-api-key-here

# Optional: LangSmith for observability
LANGSMITH_API_KEY=your-langsmith-key-here
LANGSMITH_TRACING=true
```

3. Run your first agent:
```bash
npm start
```

## 🚀 Available Examples

1. `helloworld.ts` - Basic ReAct agent
   - Learn the fundamentals of LangGraph.js
   - Understand state management
   - See tool usage in action
   - Experience conversation memory

## 💡 Key Features

- **Stateful Agents**: Create agents that maintain state between interactions
- **Tool Integration**: Easy to add and use custom tools
- **Memory Management**: Built-in support for conversation memory
- **Type Safety**: Full TypeScript support
- **Observability**: Optional LangSmith integration for debugging

## 🔧 Customization

1. Add custom tools:
```typescript
const customTool = tool(
  async ({ query }) => {
    // Implement your tool logic
    return "Tool response";
  },
  {
    name: "custom_tool",
    description: "Tool description",
    schema: z.object({
      query: z.string().describe("Input description"),
    }),
  }
);
```

2. Configure the agent:
```typescript
const app = createReactAgent({
  llm: model,
  tools: [customTool],
  checkpointSaver: new MemorySaver(),
});
```

3. Add conversation memory:
```typescript
const result = await app.invoke(
  {
    messages: [{ role: "user", content: "Your question" }]
  },
  { configurable: { thread_id: "unique-id" } }
);
```

## ⚠️ Important Notes

1. Ensure `.env` file is properly configured
2. API keys should never be committed to version control
3. Use TypeScript for better development experience
4. Consider enabling LangSmith for debugging

## 🤝 Next Steps

- Explore the example code in detail
- Add your own custom tools
- Implement more complex conversation flows
- Enable LangSmith for debugging

## 📚 Additional Resources

- [LangGraph.js Documentation](https://langchain-ai.github.io/langgraphjs/)
- [Anthropic Claude Documentation](https://docs.anthropic.com/claude/)