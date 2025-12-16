# LiteLLM → Azure API Management → Azure OpenAI

Call Azure OpenAI through APIM using LiteLLM.

```
┌─────────────┐     ┌──────────────────┐      ┌─────────────────┐
│   LiteLLM   │ ──▶│  Azure API Mgmt  │ ──▶  │  Azure OpenAI   │
│  (Client)   │     │    (Gateway)     │      │ (GPT-4o Model)  │
└─────────────┘     └──────────────────┘      └─────────────────┘
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and configure:
   ```
   APIM_ENDPOINT=https://your-apim.azure-api.net
   APIM_SUBSCRIPTION_KEY=your-subscription-key
   AZURE_OPENAI_DEPLOYMENT=gpt-4o
   AZURE_OPENAI_API_VERSION=2024-12-01-preview
   ```

3. Run:
   ```bash
   python litellm_apim_dotenv.py
   ```

## Usage

```python
from litellm_apim_dotenv import chat_completion

response = chat_completion("Hello, how are you?")
print(response)
```

## Requirements

- Python 3.8+
- Azure API Management with Azure OpenAI backend configured
- APIM subscription key