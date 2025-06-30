from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import json
import os 

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))


class Meal:
    def __init__(self, name, calories, mealtype, time):
        self.name = name 
        self.calories = calories
        self.mealtype = mealtype
        self.time = time 

    def to_dict(self):
        return {
            'name': self.name,
            'calories': self.calories,
            'meal type': self.mealtype,
            'time': self.time.strftime("%H:%M")
        }
    
class MealLogger:
    def  __init__(self, filename = "meal_logs.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename , 'r') as f:
                    return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
                   
    
    def save_data(self):
        with open(self.filename , 'w',encoding= 'utf-8') as f:
            json.dump(self.data , f , indent= 4)

    def add_meal(self, meal):
        date_key = datetime.now().strftime("%d-%m-%Y")
        if date_key not in self.data:
            self.data[date_key] = []
        self.data[date_key].append(meal.to_dict())
        self.save_data()

    def view_today_meals(self):
        date_key = datetime.now().strftime("%d-%m-%Y")
        return self.data.get(date_key,[])
    
    def total_calories(self):
        meals = self.view_today_meals()
        return sum(item['calories'] for item in meals)
    
    def ai_suggest_healthier(self,meal):

        prompt = (
            f"Suggest a healthier alternative to this meal:\n"
            f"Meal: {meal.name}\n"
            f"Calories: {meal.calories}\n"
            f"Type: {meal.mealtype}\n"
            f"Give a brief suggestion in one line."
        )

        try:
            response = client.chat.completions.create(
                    model = "gpt-3.5-turbo",
                    messages= [
                        {"role": "system", "content": "You are a helpful nutrition assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens= 60,
                    temperature= 0.7
            )
            message = response.choices[0].message
            return message.content.strip() if message and message.content else "⚠️ No suggestion returned."
            
        except Exception as e:
            return f"AI suggestion failed: {str(e)}"