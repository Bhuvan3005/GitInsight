from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_analysis(context):

    prompt = f"""
Analyze this repository.

Return ONLY valid JSON:

{{
    "summary": "...",
    "purpose": "...",
    "tech_stack": [],
    "strengths": [],
    "weaknesses": [],
    "recommendations": [],
    "health_score": 0
}}

Repository:
{context}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    

    return response.text