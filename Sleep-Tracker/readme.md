# 💤 AI-Powered Sleep Tracker

🧠 A smart sleep tracking system that logs your daily sleep and wake times, calculates sleep duration, and uses OpenAI to detect unhealthy trends in your recent sleep habits.

## 🚀 Features

- 🛌 Manual sleep & wake time logging
- 🕒 Auto-calculates duration (handles post-midnight sleep)
- 🗂️ JSON-based persistent log storage
- 📊 Last 7 days sleep summary
- 🧠 AI-powered analysis using OpenAI API
- ⚠️ Detects low sleep patterns (<6 hrs), late nights, and irregularities
- ✅ Clean terminal menu for ease of use

## 📁 Project Structure

- `tracker.py` – main sleep tracking logic and AI analysis
- `menu.py` – interactive terminal-based menu
- `sleep_log.json` – stores all sleep logs
- `requirements.txt` – Python dependencies
- `.env` – stores your OpenAI API key

## ⚙️ How to Run

1. Clone the repo or copy the files
2. Create a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the tracker via menu:
   ```
   python menu.py
   ```

## 📚 Technologies Used

- Python 3.x
- OpenAI API (`gpt-3.5-turbo`)
- `datetime`, `json`, `dotenv`

## 📖 Sample Log Entry

```json
{
  "date": "01-07-2025",
  "sleep time": "03:00 AM",
  "wake time": "07:00 AM",
  "duration": 4.0
}
```

## 🧠 Sample AI Output

```
🧠 AI Sleep Analysis:
- Your average sleep over the past 7 days is 5.5 hours.
- Multiple nights fall below the recommended 6–8 hours.
- Irregular sleep times may disrupt your circadian rhythm.
- Try sleeping before midnight and aim for 7+ hours.
```

## 🧩 Future Enhancements

- 📅 Sleep schedule calendar view
- 📈 Graph-based trend analysis (matplotlib)
- 😴 Sleep quality prediction using ML
- 🖥️ GUI version with Tkinter

## 👤 Author

Iceycoast  
Python learner & builder of practical AI-based wellness tools
