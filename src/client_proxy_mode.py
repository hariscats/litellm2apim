"""
Client that calls LiteLLM Proxy → APIM → Azure OpenAI

In proxy mode, you use the standard OpenAI SDK to call LiteLLM,
which then routes to APIM and Azure OpenAI.
"""

from openai import OpenAI

# Point to LiteLLM proxy instead of OpenAI
client = OpenAI(
    base_url="http://localhost:4000",  # LiteLLM proxy
    api_key="not needed"  # Any dummy key (proxy handles auth)
)

response = client.chat.completions.create(
    model="gpt-4o",  # Maps to azure/gpt-4o via proxy config
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Azure API Management in 2 sentences."}
    ],
    max_tokens=100
)

print(response.choices[0].message.content)
