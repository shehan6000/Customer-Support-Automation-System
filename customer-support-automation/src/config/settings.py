import os
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    # API Keys
    openai_api_key: str
    serper_api_key: Optional[str] = None
    
    # Model Configuration
    openai_model_name: str = "gpt-3.5-turbo"
    
    # CrewAI Configuration
    verbose: bool = False
    memory: bool = True
    
    # Tool Configuration
    enable_web_search: bool = False
    enable_web_scrape: bool = True
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()

# Initialize settings
settings = get_settings()