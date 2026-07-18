from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API Key not found!")
    exit()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say Hello from Gemini!"
)

print(response.text)