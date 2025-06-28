import json
from datetime import datetime
from dotenv import load_dotenv
from colorama import init, Fore, Style
import openai
import os

# ✅ Initialize
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

# 🎭 Mood choices
moods = {
    "1": "😄 Happy",
    "2": "😐 Neutral",
    "3": "😞 Sad",
    "4": "😡 Angry",
    "5": "😢 Crying",
    "6": "😍 Loved"
}

# 📁 File to save logs
filename = "mood_logs.json"

# 🎨 Mood-to-color mapping
mood_colors = {
    "😄 Happy": Fore.YELLOW,
    "😐 Neutral": Fore.WHITE,
    "😞 Sad": Fore.BLUE,
    "😡 Angry": Fore.RED,
    "😢 Crying": Fore.CYAN,
    "😍 Loved": Fore.MAGENTA
}

# 🎨 Sentiment color mapping
sentiment_colors = {
    "Positive": Fore.GREEN,
    "Neutral": Fore.LIGHTBLACK_EX,
    "Negative": Fore.RED
}

# 📥 Load logs
def load_logs():
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# 💾 Save logs
def save_logs(data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 🧠 Use OpenAI to analyze sentiment
def analyze_sentiment(note):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that classifies emotional sentiment."},
                {"role": "user", "content": f"Classify this note into one word: Positive, Neutral, or Negative.\nNote: {note}"}
            ],
            max_tokens=5,
            temperature=0.3
        )
        message = response.choices[0].message
        if message and message.content:
            return message.content.strip()
        else:
            return "Unknown"
    except Exception as e:
        import traceback
        traceback.print_exc()
        return "Unknown"

# 📝 Log today's mood
def log_mood():
    print(f"\n{Fore.CYAN}=== Log Today's Mood ==={Style.RESET_ALL}")
    for key, value in moods.items():
        print(f"{Fore.YELLOW}[{key}] {value}")

    mood_choice = input("Enter your mood (number): ").strip()
    if mood_choice not in moods:
        print(f"{Fore.RED}❌ Invalid mood choice.")
        return

    emoji_mood = moods[mood_choice]
    note = input("📝 Write a short note on how you feel today: ").strip()
    ai_mood = analyze_sentiment(note)

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "emoji": emoji_mood,
        "note": note,
        "ai_mood": ai_mood
    }

    logs = load_logs()
    logs.append(entry)
    save_logs(logs)

    print(f"\n{Fore.GREEN}✅ Mood logged: {emoji_mood} ({ai_mood})")

# 📋 View all logs
def view_logs():
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            results = ""
            for i in data:
                results += format_entry(i)
            return results.strip() if results else "📭 No logs found."
    except (FileNotFoundError, json.JSONDecodeError):
        return f"{Fore.RED}🚫 Logs not found."

# 🔍 Search logs
def search_logs():
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

            if not data:
                return f"{Fore.YELLOW}📭 No logs to search."

            print(f"\n{Fore.CYAN}🔍 Search by:")
            print("[1] Date (YYYY-MM-DD)")
            print("[2] Mood Emoji")
            print("[3] AI Sentiment (Positive/Negative/Neutral)")
            choice = input("Enter option (1/2/3): ").strip()

            if choice == "1":
                query = input("📅 Enter date (YYYY-MM-DD): ").strip()
            elif choice == "2":
                query = input("😊 Enter mood emoji (e.g. 😄): ").strip()
            elif choice == "3":
                query = input("🧠 Enter sentiment: ").strip()
            else:
                return f"{Fore.RED}❌ Invalid choice."

            results = ""
            for entry in data:
                if choice == "1" and entry["date"] == query:
                    results += format_entry(entry)
                elif choice == "2" and entry["emoji"] == query:
                    results += format_entry(entry)
                elif choice == "3" and entry["ai_mood"].lower() == query.lower():
                    results += format_entry(entry)

            return results.strip() if results else f"{Fore.YELLOW}🔎 No matching logs found."

    except (FileNotFoundError, json.JSONDecodeError):
        return f"{Fore.RED}🚫 Log file not found."

# 🎨 Format log entry for display
def format_entry(entry):
    mood_color = mood_colors.get(entry["emoji"], Fore.WHITE)
    sentiment_color = sentiment_colors.get(entry["ai_mood"], Fore.WHITE)

    return (
        f"\n{Fore.CYAN}📅 Date:      {entry['date']}"
        f"\n{mood_color}😊 Mood:      {entry['emoji']}"
        f"\n{Fore.GREEN}📝 Note:      {entry['note']}"
        f"\n{sentiment_color}🧠 Sentiment: {entry['ai_mood']}"
        f"\n{Style.DIM}{'-' * 35}{Style.RESET_ALL}"
    )

# 🧹 Clear all logs
def clear_logs():
    confirm = input(f"{Fore.RED}⚠️ Are you sure you want to delete all logs? (yes/no): ").strip().lower()
    if confirm == "yes":
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)
        print(f"{Fore.GREEN}🧹 All logs cleared successfully.")
    else:
        print(f"{Fore.YELLOW}❎ Clear operation cancelled.")
