import os
import time

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def ask_gemini(question: str, repository_data: dict):

    prompt = f"""
You are an expert AI Repository Assistant.

Your job is to help developers understand GitHub repositories by analyzing the repository information provided below.

Repository Information:
{repository_data}

User Question:
{question}

Instructions:

1. Answer in clear, professional, and simple English.

2. Use the repository information as your primary source of truth.

3. If the question is about:
   - technologies
   - programming languages
   - frameworks
   - project structure
   - architecture
   - README
   - repository health
   - code quality
   - deployment
   - documentation
   - best practices
   - recommendations
   - improvements

   answer directly using the repository information.

4. If the user asks for an opinion or reasoning, such as:
   - Is this project useful?
   - Can this project be used in real life?
   - Is this project good?
   - Can this project be used in companies?
   - Who can use this project?
   - What are its advantages?
   - What are its limitations?
   - Is this project suitable for a hackathon?
   - What features can be added?

   provide a logical answer based on the repository information.
   Do not refuse simply because the answer requires reasoning.

5. If the repository information is insufficient to fully answer a question,
   clearly mention the limitation and then provide the best possible answer
   based on the available repository analysis.

6. Only refuse questions that are completely unrelated to the repository,
   for example:
   - weather
   - sports
   - movies
   - politics
   - personal advice
   - general knowledge unrelated to the repository

   In those cases reply:

   "I can answer questions related to this repository and provide insights based on its analysis. Please ask about the repository, its technologies, architecture, quality, features, improvements, or possible applications."

7. Never invent technologies, files, frameworks, or features that are not present in the repository analysis.

8. When appropriate:
   - Use bullet points.
   - Explain your reasoning.
   - Give practical suggestions.

9. Keep answers informative, concise, and professional.

10. Format your response using Markdown.

Use:

- ## Main headings
- ### Subheadings
- Bullet points
- **Bold important terms**

Avoid writing one large paragraph.
"""

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            if response and hasattr(response, "text") and response.text:
                return response.text

            return """
## ⚠️ No Response

Gemini returned an empty response.

Please try asking your question again.
"""

        except Exception as error:

            print(f"Gemini Attempt {attempt + 1} Failed: {error}")

            if attempt < 2:

                time.sleep(2)

            else:

                return f"""
## ⚠️ AI Service Temporarily Unavailable

The Gemini AI service is currently unavailable.

**Reason:** {error}

Please wait a few moments and try again.
"""