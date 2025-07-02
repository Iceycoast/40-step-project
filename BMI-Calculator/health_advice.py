from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")
client = OpenAI(api_key=api_key)

def get_health_advice(age:int, gender:str, bmi:float, category:str) -> str:
    prompt = (
        f"You're a health advisor. Give clear, actionable, 2-3 line health advice "
        f"for a {age}-year-old {gender} with a BMI of {bmi} ({category}). "
        f"Avoid medical jargon. Be friendly, precise, and helpful."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        message =response.choices[0].message
        return message.content.strip() if message and message.content else "No Advice returned."
    except Exception as e:
        return f"AI Advice failed: {str(e)}"