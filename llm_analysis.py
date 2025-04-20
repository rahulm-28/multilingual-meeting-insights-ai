import os
import json
import requests
from openai import AzureOpenAI

def analyze_transcript_azure(transcript):
    messages = [
        {"role": "system", "content": """
You are an AI assistant that summarizes meeting transcripts. Extract:
1. Meeting Title
2. Date
3. Participants
4. Key Discussion Points
5. Decisions
6. Action Items
7. Follow-ups
8. Quotes
9. Summary
"""},
        {"role": "user", "content": f"Transcript:\n\n{transcript}"},
    ]

    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_AI_ENDPOINT"),
        api_key=os.getenv("AZURE_AI_KEY"),
        api_version="2025-01-01-preview",
    )

    completion = client.chat.completions.create(
        model=os.getenv("AZURE_AI_DEPLOYMENT"),
        messages=messages,
        max_tokens=800,
        temperature=0.7,
        top_p=0.95
    )

    return completion.choices[0].message.content

def analyze_transcript_ollama(transcript):
    messages = [
        {"role": "system", "content": "Summarize meeting transcript with key sections."},
        {"role": "user", "content": transcript},
    ]

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3:latest",
            "messages": messages,
            "stream": False
        }
    )

    if response.status_code == 200:
        try:
            chunks = response.text.strip().split("\n")
            last_response = json.loads(chunks[-1])
            return last_response.get("message", {}).get("content", "No content from LLaMA")
        except Exception as e:
            return f"Error parsing LLaMA output: {e}"
    else:
        return f"Error from Ollama API: {response.status_code}"