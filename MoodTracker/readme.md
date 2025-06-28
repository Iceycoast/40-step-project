# 🧠 Mood Tracker with AI Sentiment – CLI Version

A clean and interactive CLI tool that lets users log their daily mood with emojis, a short note, and real AI-based sentiment analysis. Built as part of the CuraLink Unified Health Tracker System (UHTAS).

🌟 Features

- 🎭 Emoji-based mood logging
- 📝 Daily personal note input
- 🤖 Sentiment classification via OpenAI (Positive, Neutral, Negative)
- 🎨 Colored terminal output using Colorama
- 🔍 Search logs by date, emoji, or sentiment
- 💾 Logs stored in UTF-8 readable JSON format
- 🧹 Secure log clearing with confirmation prompt

📁 Project Structure

- `main.py` → Starts the app, imports menu and utils
- `menu.py` → CLI menu logic and routing
- `mood_utils.py` → Log/save/search moods, OpenAI integration
- `.env` → Stores your `OPENAI_API_KEY` securely
- `mood_logs.json` → JSON file with saved logs

⚙️ How to Run

- Install dependencies:
  `pip install openai python-dotenv colorama`
- Add your OpenAI key to a `.env` file:
  `OPENAI_API_KEY=your-key-here`
- Run the app:
  `python main.py`

🧰 Technologies Used

- Python 3.x
- OpenAI API (gpt-3.5-turbo)
- Colorama for terminal styling
- Dotenv for secure key loading
- JSON & Datetime for structured logging

🧾 Sample Log Entry

```json
{
  "date": "2025-06-29",
  "emoji": "😄 Happy",
  "note": "Felt productive and focused today.",
  "ai_mood": "Positive"
}
```

🚀 Future Enhancements

- 🖼️ GUI version with Tkinter (Phase 3)
- 📊 Mood & sentiment charts using matplotlib
- 🔐 Private note encryption
- 🧠 Weekly AI-based mood summaries
- 🧩 Unified dashboard in final CuraLink build

👤 Author

- **Iceycoast**
  Python learner & builder of practical AI-based wellness tools
