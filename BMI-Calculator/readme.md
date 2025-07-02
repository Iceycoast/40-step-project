# 🧠 AI-Powered BMI Tracker

A modular, OpenAI-integrated BMI tracker that logs user health data, gives real-time AI health advice, and summarizes patterns using past logs.

## 🚀 Features

- 📏 BMI Calculation with Age & Gender
- 🧠 AI Health Advice via OpenAI API
- 📊 AI-Powered Trend Summary by Name
- 📂 JSON Log Storage
- 🔍 View entries for all users or specific users by name
- 🗑️ Delete Entries by Index or All at Once
- 🔢 Log Count Per User
- ✅ CLI Menu with Clean UX
- 📁 Modular File Structure

## 📁 Project Structure

```
BMI-Calculator/
├── bmi.py                 # BMI class with BMI logic + calls AI advice
├── tracker.py             # BMITracker: data operations (add/view/delete)
├── health_advice.py       # get_health_advice(): OpenAI logic for per-entry advice
├── analyzer.py            # generate_summary(): OpenAI logic for log summaries
├── bmi_menu.py            # CLI interface logic
├── main.py                # Program entry point
├── bmi_log.json           # Stored log data
├── .env                   # Contains your OpenAI API key
```

## 🧠 Sample Log Entry

```json
{
  "date": "30-06-2025",
  "name": "Neha Sinha",
  "age": 29,
  "gender": "Female",
  "height": 160,
  "weight": 58,
  "bmi": 22.7,
  "category": "Normal",
  "advice": "Neha, your BMI is ideal. Maintain it by balancing carbs and protein."
}
```

## ▶️ How to Run

```bash
1. Clone this repo
2. Create a .env file with: OPENAI_API_KEY=your_api_key
3. Run: python main.py
```

## 🛠️ Technologies Used

- Python 3.11+
- OpenAI API (gpt-3.5-turbo)
- `json`, `os`, `dotenv`, `datetime`

## 🧠 AI Modules

- `get_health_advice(age, gender, bmi, category)` → health advice per entry
- `generate_summary(name, entries)` → summary across all logs for a user

## 🔮 Future Enhancements

- 🖼️ GUI version with Tkinter (Phase 3)
- 📈 Graphs for BMI trend using matplotlib
- 🔐 Auth for multiple users
- 🧠 Weekly AI-based health reports
- 📲 Export logs as CSV or PDF

## 👤 Author

**Iceycoast**  
Learning Python, building AI tools, chasing the dev life.
