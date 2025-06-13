import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes the main idea of a text."},
            {"role": "user", "content": f"Summarize the main idea of the following article in one sentence:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content
