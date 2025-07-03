# 🩺 Daily Health Summary Aggregator

A modular Python program that summarizes users' daily health data — including water intake, meal calories, and BMI — and generates friendly AI-powered summaries using OpenAI's GPT API.

## 🚀 Features

- 📦 Aggregates data from:
  - Water intake logs (per ml entry)
  - Meal logs (per meal with calorie counts)
  - BMI tracker (with user info + advice)
- 📊 Organizes data by date
- 🤖 Generates daily summaries via OpenAI
- 🧠 Error-handled, auto-loaded JSON logs
- 📅 Date-based interactive menu

## 🗂️ Project Structure

```
Daily-Health-Summary/
│
├── aggregator.py           # Core logic: loads, converts, aggregates logs
├── ai_summary.py           # GPT-4 integration for natural language summaries
├── menu.py                 # CLI menu interface to view summaries
│
├── MealLogger/
│   └── meal_logs.json
├── Water-Intake-tracker/
│   └── water_intake.json
├── BMI-Calculator/
│   └── bmi_log.json
│
├── .env                    # Stores OpenAI API key
├── .gitignore
└── requirements.txt
```

## 🧪 How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Set your OpenAI API key**  
   Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

3. **Run the main program**

```bash
python menu.py
```

## 🧰 Technologies Used

- Python 3.10+
- `pathlib`, `json`, `collections.defaultdict`
- [OpenAI API](https://platform.openai.com/)
- `python-dotenv`

## 📝 Sample Log Entry

```json
{
  "01-07-2025": [
    { "time": "07:30", "quantity": 300 },
    { "time": "10:15", "quantity": 500 }
  ]
}
```

## 🔮 Future Enhancements

- 🧑‍🤝‍🧑 Filter logs by user
- 📤 Export summaries as CSV/PDF
- 🖥️ GUI with date picker and charts
- 📡 Real-time API integration

## 👨‍💻 Author

**Iceycoast**  
🧊 GitHub: [github.com/Iceycoast](https://github.com/Iceycoast)
