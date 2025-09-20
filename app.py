from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI()

while True: 
    question = input("\nUser😁: ")

    if question == "exit":
        break

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        max_tokens = 50,    # How many maximum words to generate
        n=1,                
        temperature=0,      # How random the response is (0 to 1)
        messages = [{"role": "user", "content": question}]
    )

#print(response)
    for choice in response.choices:
        print(f"\nAI🤖: {choice.message.content}")