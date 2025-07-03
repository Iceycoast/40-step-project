from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(date: str, data: dict) -> str:
    prompt = f"""
You are a health assistant. Summarize this user's health on {date} in 3 short lines:
- Water intake: {data.get('water_ml', 'N/A')} ml
- Calorie intake: {data.get('calories', 'N/A')}
- BMI: {data.get('bmi', 'N/A')}

Respond in friendly, short sentences — avoid technical jargon.
"""

    try:
        response = client.chat.completions.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=100,
            temperature=0.7
        )
        message = response.choices[0].message
        return message.content.strip() if message and message.content else "No summary returned"
    except Exception as e:
        return f"AI summary failed: {str(e)}"
