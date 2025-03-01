"""
Configuration file for LLM parameters and environment settings.
This file contains common parameters that can be reused across different examples.
"""

import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

# Model configurations
DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'gpt-4o-mini')
DEFAULT_TEMPERATURE = float(os.getenv('DEFAULT_TEMPERATURE', '0.7'))

# API configurations
API_KEY = os.getenv('OPENAI_API_KEY')
API_BASE = os.getenv('OPENAI_API_BASE')

def get_api_key() -> Optional[str]:
    """Get the API key from environment variable."""
    if not API_KEY:
        raise ValueError("Please set API_KEY environment variable")
    return API_KEY

def get_api_base() -> Optional[str]:
    """Get the API base URL from environment variable."""
    return API_BASE

def get_model_config(model: Optional[str] = None, temperature: Optional[float] = None) -> dict:
    """Get model configuration with default values."""
    return {
        "model": model or DEFAULT_MODEL,
        "temperature": temperature if temperature is not None else DEFAULT_TEMPERATURE,
    } 