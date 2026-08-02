from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def translate_text(text: str, target_language: str):

    prompt = f"""
Translate the following text into {target_language}.

Return ONLY the translated text.

Text:
{text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",   # <-- same model that worked in test_gemini.py
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"ERROR: {e}"