from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime,time, timedelta
import os
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Sleep:
    def __init__(self,sleeptime,waketime):
        self.sleeptime = sleeptime
        self.waketime = waketime
        self.date = datetime.now()

    def calculate_sleep_hours(self):
        if self.waketime <= self.sleeptime:
            self.waketime = self.waketime + timedelta(days=1)
        sleep_duration = self.waketime - self.sleeptime
        return round(sleep_duration.total_seconds()/3600, 2)
        

    def to_dict(self):
        return {
            "date": self.date.strftime("%d-%m-%Y"),
            "sleep time": self.sleeptime.strftime("%I:%M %p"),
            "wake time": self.waketime.strftime("%I:%M %p"),
            "duration": self.calculate_sleep_hours()
        }
    
class SleepTracker:
    def __init__(self,filename = "sleep_log.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.filename, 'w', encoding= 'utf-8') as f:
            json.dump(self.data, f, indent=4)

    def log_sleep_wake_time(self,sleep,wake):
        try:
            sleep = datetime.strptime(sleep,"%I:%M %p")
            wake = datetime.strptime(wake,"%I:%M %p")

            new_entry = Sleep(sleep,wake).to_dict()

            for i,entry in enumerate(self.data):
                if entry['date'] == new_entry['date']:
                    choice = input(f"Entry for {new_entry['date']} already exists. Overwrite? (yes/no): ").strip().lower()
                    if choice in ["yes","y"]:
                        self.data[i] = new_entry
                        self.save_data()
                        return"Entry Updated"
                    else:
                        return"Entry not Added."
                    
            
            self.data.append(new_entry)
            self.save_data()
            return"Sleep Entry added successfully."

        except ValueError:
            return "Invalid time format. Please use HH:MM AM/PM format."
        
    def view_logs(self):
        if not self.data:
            return "No sleep logs found."
        logs = "📘 All Sleep Logs\n" + "=" * 30
        for idx, i in enumerate(self.data, 1):
            logs += (
                f"\n\n🔹 Log {idx}"
                f"\nDate:       {i['date']}"
                f"\nSleep Time: {i['sleep time']}"
                f"\nWake Time:  {i['wake time']}"
                f"\nDuration:   {i['duration']} hours"
                f"\n{'-'*30}"
            )
        return logs.strip() 
        
    def get_last_7_days_summary(self):
        if not self.data:
            return ""

        seven_days_ago = datetime.now() - timedelta(days=7)
        recent_logs = [
            entry for entry in self.data
            if datetime.strptime(entry["date"], "%d-%m-%Y") >= seven_days_ago
        ]

        if not recent_logs:
            return ""

        summary = "🛏️ Sleep Logs (Last 7 Days)\n" + "=" * 30
        for i, log in enumerate(recent_logs, 1):
            summary += (
                f"\n\n🔹 Log {i}"
                f"\nDate:       {log['date']}"
                f"\nSleep Time: {log['sleep time']}"
                f"\nWake Time:  {log['wake time']}"
                f"\nDuration:   {log['duration']} hours"
                "\n" + "-" * 30
            )
        return summary.strip()


        
    def ai_sleep_analyzer(self):
        summary = self.get_last_7_days_summary()
        if not summary:
            return "No sleep data found in the last 7 days."
        try:
            response = client.chat.completions.create(
                    model= 'gpt-3.5-turbo',
                    messages= [
                        {'role': 'system', 'content': "You're a sleep expert. Analyze the user's last 7 days of sleep logs. Detect unhealthy trends, average sleep hours, and give practical advice in bullet points."},
                        {'role': 'user', 'content': summary}
                    ],
                    max_tokens= 400,
                    temperature= 0.4,
                    top_p=1.0,
                    frequency_penalty=0.3,
                    presence_penalty=0.0
            )
            message = response.choices[0].message
            return "🧠 AI Sleep Analysis:\n" + message.content.strip() if message and message.content else "No suggestion returned."
        except Exception as e:
            return f"AI suggestion failed: {str(e)}"