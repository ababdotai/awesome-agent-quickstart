"""This module provides example tools for web scraping, search functionality, and content creation.

It includes tools for general search, finance research, blog research, social media research.

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Callable, Optional, cast, Any

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_core.tools import tool
from datetime import datetime

@tool
async def finance_research(ticker_symbol: str) -> Optional[list[dict[str, Any]]]:
    """Search for finance research, must be a ticker symbol."""
    wrapped = YahooFinanceNewsTool()
    result = await wrapped.ainvoke({"query": ticker_symbol})
    return cast(list[dict[str, Any]], result)

@tool   
async def advanced_research_tool(query: str) -> Optional[list[dict[str, Any]]]:
    """Perform in-depth research for blog content.
    
    This tool conducts comprehensive web searches with higher result limits and
    deeper analysis, ideal for creating well-researched blog posts backed by
    authoritative sources.
    """
    # Using Tavily with higher result count for more comprehensive research
    wrapped = TavilySearchResults(
        max_results=10,  # Default to 10 if not specified
        search_depth="advanced"  # More thorough search
    )
    result = await wrapped.ainvoke({"query": query})
    return cast(list[dict[str, Any]], result)

@tool
async def basic_research_tool(query: str) -> Optional[list[dict[str, Any]]]:
    """Research trending topics for social media content.
    
    This tool performs quick searches optimized for trending and viral content,
    returning concise results ideal for social media post creation.
    """
    # Using Tavily with lower result count and quicker search for social content
    wrapped = TavilySearchResults(
        max_results=5,  # Default to 3 if not specified
        search_depth="basic",  # Faster, less comprehensive search
        include_raw_content=False,  # Just the highlights
        include_images=True  # Social posts often benefit from images
    )
    result = await wrapped.ainvoke({"query": f"trending {query}"})
    return cast(list[dict[str, Any]], result)

@tool
async def get_todays_date() -> str:
    """Get the current date."""
    return datetime.now().strftime("%Y-%m-%d")


def get_tools(selected_tools: list[str]) -> list[Callable[..., Any]]:
    """Convert a list of tool names to actual tool functions."""
    tools = []
    for tool in selected_tools:
        if tool == "finance_research":
            tools.append(finance_research)
        elif tool == "advanced_research_tool":
            tools.append(advanced_research_tool)
        elif tool == "basic_research_tool":
            tools.append(basic_research_tool)
        elif tool == "get_todays_date":
            tools.append(get_todays_date)
    
    return tools