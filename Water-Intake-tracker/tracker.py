from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime,time
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Water:
    def __init__(self, time, quantity):
        self.time = time
        self.quantity = quantity

    def to_dict(self):
        return {
            "time": self.time.strftime("%H:%M") if isinstance(self.time,time) else self.time,
            "quantity": self.quantity
        }
    
class IntakeTracker:
    def  __init__(self,filename = "water_intake.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def save_data(self):
        with open(self.filename, 'w', encoding= "utf-8") as f:
            json.dump(self.data , f , indent= 4)

    def add_log(self, water):
        date_key = datetime.now().strftime("%d-%m-%Y")
        self.data[date_key] = self.data.get(date_key, [])
        self.data[date_key].append(water.to_dict())
        self.save_data()

    def view_daily_logs(self, date = None):
        if date is None:
            date = datetime.now().strftime("%d-%m-%Y")
        return self.data.get(date,[])
    
    def total_water_intake(self):
        intake = self.view_daily_logs()
        return sum(item['quantity'] for item in intake)
    
    def ai_goal(self):
        current_time = datetime.now().strftime("%H:%M")
        intake = self.total_water_intake()
        try:
            response = client.chat.completions.create(
                    model= "gpt-3.5-turbo",
                    messages= [
                        {"role":"system", "content": "You are a water intake assistant. Based on the user's daily goal and current time, remind them to drink water if they haven't met their target. Suggest how much they should drink now to stay on track."},
                        {"role": "user", "content": f"My current water intake is {intake} ml and the time is {current_time}. Suggest if I should drink more and how much. Make it brief"}
                    ],
                    max_tokens= 70,
                    temperature= 0.4
            )
            message = response.choices[0].message
            return message.content.strip() if message and message.content else "No suggestion returned."
        except Exception as e:
            return f"AI suggestion failed: {str(e)}"





