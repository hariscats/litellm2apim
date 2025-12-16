"""
LiteLLM to Azure API Management with Environment Variables

This version uses python-dotenv to load configuration from .env file.
"""

import os
import litellm
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env file
load_dotenv()

# Configuration from environment
APIM_ENDPOINT = os.getenv("APIM_ENDPOINT")
APIM_SUBSCRIPTION_KEY = os.getenv("APIM_SUBSCRIPTION_KEY")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

# Set LiteLLM to drop unmapped params to avoid errors
litellm.drop_params = True


def chat_completion(
    user_message: str,
    system_message: str = "You are a helpful AI assistant.",
    **kwargs
):
    """
    Simple chat completion through APIM to Azure OpenAI.
    """
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    
    response = completion(
        model=f"azure/{DEPLOYMENT_NAME}",
        messages=messages,
        api_base=APIM_ENDPOINT,
        api_key=APIM_SUBSCRIPTION_KEY,
        api_version=API_VERSION,
        **kwargs
    )
    
    return response.choices[0].message.content


def stream_chat_completion(
    user_message: str,
    system_message: str = "You are a helpful AI assistant.",
):
    """
    Streaming chat completion through APIM to Azure OpenAI.
    """
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    
    response = completion(
        model=f"azure/{DEPLOYMENT_NAME}",
        messages=messages,
        api_base=APIM_ENDPOINT,
        api_key=APIM_SUBSCRIPTION_KEY,
        api_version=API_VERSION,
        stream=True,
    )
    
    for chunk in response:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


if __name__ == "__main__":
    # Validate configuration
    if not APIM_ENDPOINT or not APIM_SUBSCRIPTION_KEY:
        print("Error: Please set APIM_ENDPOINT and APIM_SUBSCRIPTION_KEY in .env file")
        print("Copy .env.example to .env and fill in your values")
        exit(1)
    
    print(f"Using endpoint: {APIM_ENDPOINT}")
    print(f"Using deployment: {DEPLOYMENT_NAME}")
    print(f"Using API version: {API_VERSION}")
    print()
    
    # Example: Simple completion
    print("=== Simple Completion ===")
    response = chat_completion(
        "Explain Azure API Management in 2 sentences.",
        max_tokens=100
    )
    print(response)
    
    # Example: Streaming completion
    print("\n=== Streaming Completion ===")
    for chunk in stream_chat_completion("What is LiteLLM?"):
        print(chunk, end="", flush=True)
    print()
