# 🌐 Browser-use agent example

A demonstration of how to use Browser-use to enable the agent to control a browser to fulfill tasks.

## Features

- 🌐 **Browser control** - Enable the agent to control a browser to fulfill tasks.
- 🧠 **State persistence** - Maintain conversation state across multiple interactions
- 🔄 **Dynamic agent routing** - Automatically route to the appropriate specialized agent

## Prerequisites

- Python 3.11+
- OpenAI API key

## Environment setup

```shell
pip install -r requirements.txt
playwright install
```

## Quick start!

```shell
python helloworld.py
```

## Expected output

~~~~markdown
INFO     [browser_use] BrowserUse logging setup complete with level info
INFO     [root] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
.../browser_use/agent/message_manager/views.py:59: LangChainBetaWarning: The function `load` is in beta. It is actively being worked on, so the API may change.
  value['message'] = load(value['message'])
INFO     [agent] 🚀 Starting task: Compare the price of gpt-4o and DeepSeek-V3
INFO     [agent] 📍 Step 1
INFO     [agent] 🤷 Eval: Unknown - The browser is started and ready for navigation.
INFO     [agent] 🧠 Memory: Task initiated. Need to compare prices of GPT-4O and DeepSeek-V3.
INFO     [agent] 🎯 Next goal: Search for the price of GPT-4O and DeepSeek-V3 using Google.
INFO     [agent] 🛠️  Action 1/1: {"search_google":{"query":"GPT-4O pricing"}}
INFO     [controller] 🔍  Searched for "GPT-4O pricing" in Google
INFO     [agent] 📍 Step 2
INFO     [agent] 👍 Eval: Success - Searched for GPT-4O pricing and found relevant results.
INFO     [agent] 🧠 Memory: Found GPT-4O pricing information. Need to search for DeepSeek-V3 pricing next.
INFO     [agent] 🎯 Next goal: Search for DeepSeek-V3 pricing using Google.
INFO     [agent] 🛠️  Action 1/1: {"search_google":{"query":"DeepSeek-V3 pricing"}}
INFO     [controller] 🔍  Searched for "DeepSeek-V3 pricing" in Google
INFO     [agent] 📍 Step 3
INFO     [agent] 👍 Eval: Success - Both searches for GPT-4O and DeepSeek-V3 pricing were completed.
INFO     [agent] 🧠 Memory: Retrieved pricing information for GPT-4O and DeepSeek-V3. Need to extract details for comparison.
INFO     [agent] 🎯 Next goal: Extract detailed pricing information for both GPT-4O and DeepSeek-V3 from search results.
INFO     [agent] 🛠️  Action 1/2: {"extract_content":{"goal":"Extract GPT-4O pricing details."}}
INFO     [agent] 🛠️  Action 2/2: {"extract_content":{"goal":"Extract DeepSeek-V3 pricing details."}}
INFO     [controller] 📄  Extracted from page
: ```json
{
  "message": "The document does not contain specific information about GPT-4O pricing details. It appears to primarily focus on DeepSeek-V3 pricing, including comparisons and updates. There is no mention of GPT-4O within the given content."
}
```

INFO     [controller] 📄  Extracted from page
: ```json
{
  "DeepSeek-V3 Pricing Details": [
    {
      "source": "api-docs.deepseek.com",
      "details": [
        {
          "time": "UTC 00:30-16:30",
          "1M tokens input (cache hit)": "$0.07",
          "1M tokens input (cache miss)": "$0.27"
        }
      ]
    },
    {
      "source": "artificialanalysis.ai",
      "details": [
        {
          "average price": "$0.48 per 1M tokens",
          "input token price": "$0.27",
          "output token price": "N/A"
        }
      ]
    },
    {
      "source": "livechatai.com",
      "details": [
        {
          "1,000 input tokens": "$0.000140",
          "1,000 output tokens": "$0.000280",
          "additional fee": "$0.0004"
        }
      ]
    },
    {
      "source": "scmp.com",
      "details": [
        {
          "DeepSeek-V3 Input token price": "$0.27 per million",
          "DeepSeek-V3 Output token price": "$1.1 per million"
        }
      ]
    },
    {
      "source": "microsoft.com",
      "details": [
        {
          "DeepSeek-V3 Global": {
            "input pricing": "$0.00114 per 1K tokens",
            "output pricing": "$0.00456 per 1K tokens"
          }
        }
      ]
    }
  ]
}
```

INFO     [agent] 📍 Step 4
INFO     [agent] 👍 Eval: Partial Success - Successfully extracted DeepSeek-V3 pricing but did not find specific GPT-4O pricing.
INFO     [agent] 🧠 Memory: DeepSeek-V3 pricing details obtained. GPT-4O pricing needs further research.
INFO     [agent] 🎯 Next goal: Open a new tab and search for GPT-4O pricing again for better results.
INFO     [agent] 🛠️  Action 1/1: {"open_tab":{"url":"https://www.google.com/search?q=GPT-4O+pricing"}}
INFO     [controller] 🔗  Opened new tab with https://www.google.com/search?q=GPT-4O+pricing
INFO     [agent] 📍 Step 5
INFO     [agent] 👍 Eval: Success - Found GPT-4O pricing information in search results.
INFO     [agent] 🧠 Memory: Both GPT-4O and DeepSeek-V3 pricing information available for comparison.
INFO     [agent] 🎯 Next goal: Summarize and compare the pricing details of GPT-4O and DeepSeek-V3.
INFO     [agent] 🛠️  Action 1/1: {"extract_content":{"goal":"Retrieve specific GPT-4O pricing details from visible elements."}}
INFO     [controller] 📄  Extracted from page
: ```json
{
  "GPT-4O_pricing_details": [
    {
      "source": "OpenAI",
      "details": [
        {
          "model": "GPT-4o mini",
          "price": "$0.150 per 1M tokens",
          "fine_tuning_price": "$0.30 per 1M tokens"
        }
      ]
    },
    {
      "source": "Azure",
      "details": [
        {
          "model": "GPT-4o-2024-1120 Global",
          "input_price": "$2.50",
          "cached_input_price": "$1.25",
          "output_price": "$10",
          "US/EU_input_price": "$2.75"
        }
      ]
    },
    {
      "source": "Artificial Analysis AI",
      "details": [
        {
          "model": "GPT-4o (Nov '24)",
          "blended_price": "$4.38 per 1M tokens",
          "input_token_price": "$2.50 per 1M tokens"
        }
      ]
    }
  ]
}
```

INFO     [agent] 📍 Step 6
INFO     [agent] 👍 Eval: Success - Retrieved both GPT-4O and DeepSeek-V3 pricing details.
INFO     [agent] 🧠 Memory: Completed extraction for both GPT-4O and DeepSeek-V3 pricing. Ready to compare prices.
INFO     [agent] 🎯 Next goal: Compare GPT-4O and DeepSeek-V3 pricing and summarize the findings.
INFO     [agent] 🛠️  Action 1/1: {"done":{"text":"Comparison Completed:\n\n**GPT-4O Pricing Details:**\n1. OpenAI: GPT-4o mini - $0.150 per 1M tokens; Fine-tuning - $0.30 per 1M tokens.\n2. Azure: GPT-4o Global - Input: $2.50; Cached Input: $1.25; Output: $10; US/EU Input: $2.75.\n3. Artificial Analysis AI: Blended Price - $4.38 per 1M tokens.\n\n**DeepSeek-V3 Pricing Details:**\n1. API-docs: $0.07 per 1M tokens (cache hit); $0.27 per 1M tokens (cache miss).\n2. Artificial Analysis AI: Average - $0.48 per 1M tokens.\n3. LiveChatAI: $0.000140 per 1,000 input tokens; Additional fee - $0.0004.\n4. SCMP: Input - $0.27 per million; Output - $1.1 per million.\n5. Microsoft: Input - $0.00114 per 1K tokens; Output - $0.00456 per 1K tokens.\n\nConclusion: GPT-4O has a wider range and higher prices compared to DeepSeek-V3, which offers competitive rates particularly with caching benefits. GPT-4O provides more premium options, while DeepSeek-V3 provides cost efficiency, especially for large volumes.\n","success":true}}
INFO     [agent] 📄 Result: Comparison Completed:

**GPT-4O Pricing Details:**
1. OpenAI: GPT-4o mini - $0.150 per 1M tokens; Fine-tuning - $0.30 per 1M tokens.
2. Azure: GPT-4o Global - Input: $2.50; Cached Input: $1.25; Output: $10; US/EU Input: $2.75.
3. Artificial Analysis AI: Blended Price - $4.38 per 1M tokens.

**DeepSeek-V3 Pricing Details:**
1. API-docs: $0.07 per 1M tokens (cache hit); $0.27 per 1M tokens (cache miss).
2. Artificial Analysis AI: Average - $0.48 per 1M tokens.
3. LiveChatAI: $0.000140 per 1,000 input tokens; Additional fee - $0.0004.
4. SCMP: Input - $0.27 per million; Output - $1.1 per million.
5. Microsoft: Input - $0.00114 per 1K tokens; Output - $0.00456 per 1K tokens.

Conclusion: GPT-4O has a wider range and higher prices compared to DeepSeek-V3, which offers competitive rates particularly with caching benefits. GPT-4O provides more premium options, while DeepSeek-V3 provides cost efficiency, especially for large volumes.

INFO     [agent] ✅ Task completed
INFO     [agent] ✅ Successfully
~~~~

# References

- [Browser-use docs](https://docs.browser-use.com)
- [Browser-use github](https://github.com/browser-use/browser-use)