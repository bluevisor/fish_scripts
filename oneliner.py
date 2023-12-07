import os
import json
import random
import requests

# OpenAI API information
OPENAI_API_KEY = "Put your OpenAI API Key here"
OPENAI_API_URL = "https://api.openai.com/v1/completions"

# Prompt templates
AI_PROMPT = "Generate a funny one-liner quote from an AI."
MATRIX_PROMPT = "Generate a funny one-liner quote from movie The Matrix."
HITCHHIKERS_PROMPT = "Generate a funny one-liner quote from The Hitchhiker's Guide to the Galaxy."

# Prompts list
prompts_list = [AI_PROMPT, MATRIX_PROMPT, HITCHHIKERS_PROMPT]

# Local greetings file path
GREETINGS_FILE_PATH = os.path.expanduser("~/greetings.txt")

# Function to check internet connection
def is_connected_to_internet():
    try:
        requests.get("https://www.google.com", timeout=10)
        return True
    except requests.exceptions.ConnectionError:
        return False

# Function to generate a quote
def generate_quote(prompt):
    if is_connected_to_internet():
        try:
            headers = {
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": "text-davinci-003",
                "prompt": prompt,
                "temperature": 0.7,
                "max_tokens": 64,
            }
            response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
            response.raise_for_status()
            data = json.loads(response.content.decode())
            quote = data["choices"][0]["text"]
            return quote.strip()
        except Exception as e:
            print(f"Error generating quote: {e}")
    else:
        try:
            with open(GREETINGS_FILE_PATH, "r") as f:
                quotes = f.readlines()
            return random.choice(quotes).strip()
        except (FileNotFoundError, OSError) as e:
            # print(f"Error reading greetings file: {e}")
            return "42"

# Choose a random prompt
prompt = random.choice(prompts_list)

# Generate and print the quote
print(generate_quote(prompt))
