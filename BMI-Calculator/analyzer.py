from openai import OpenAI
from dotenv import load_dotenv
import os
from tracker import BMITracker
bmitracker = BMITracker()

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")
client = OpenAI(api_key=api_key)


def generate_summary(name:str) -> str:
    user_logs = bmitracker.get_entries_for(name)

    if not user_logs:
        return f"No entries found for {name}."
    
    logs_text = ""
    for idx, entry in enumerate(user_logs, 1):
        logs_text += (
            f"Entry {idx}\n"
            f"Date:      {entry['date']}\n"
            f"Age:       {entry['age']}\n"
            f"Gender:    {entry['gender']}\n"
            f"Height:    {entry['height']} cm\n"
            f"Weight:    {entry['weight']} kg\n"
            f"BMI:       {entry['bmi']}\n"
            f"Category:  {entry['category']}\n"
            f"AI Advice: {entry['advice']}\n"
            f"{'-'*40}\n\n"
        )

    prompt = (
        f"You are a health analyzer. Review the following BMI logs for {name}:\n\n"
        f"{logs_text}\n"
        f"Give a 3-5 line summary that observes trends or changes in BMI, health category, or behavior. "
        f"Highlight any patterns and suggest one improvement for the future. Avoid repeating the original advice."
    )
        
    try: 
        response = client.chat.completions.create(
            model= "gpt-3.5-turbo",
            messages= [{"role": "user", "content": prompt}],
            temperature= 0.6
        )
        message = response.choices[0].message
        return message.content.strip() if message and message.content else "No summary returned."
    
    except Exception as e:
        return f"AI Summary failed: {str(e)}"