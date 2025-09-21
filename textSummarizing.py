# Summarising Simple Chatbot
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


client = OpenAI()

# Function to extract keywords from text ✨
def text_summarizer(prompt: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=256
    )
    return response.choices[0].message.content.strip()

