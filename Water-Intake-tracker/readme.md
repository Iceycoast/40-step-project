# 💧 Water Intake Tracker (CLI)

A clean, user-friendly Python CLI tool designed to help you log and track your daily water intake. Simple, efficient, and powered by OpenAI for hydration tips — perfect for personal health tracking or building your wellness project stack.

## ⚙️ Features

- ✍️ Add new water entries with time and quantity (in ml)
- 📅 Automatically sorted and grouped by date
- 📊 View today's or specific date's intake logs
- 🧮 Total daily intake calculator
- 🤖 AI-generated hydration tips using OpenAI
- 💾 Local data storage using JSON
- 🧩 Lightweight, fast, and beginner-friendly

## 🗂️ Project Structure

WaterTracker/  
├── water_intake.json – stores all logs  
├── tracker.py – defines core classes (Water, IntakeTracker)  
├── main.py – CLI menu and user interaction  
└── .env – holds OpenAI API key

## 🚀 How to Run

1. Ensure Python 3 is installed on your system
2. Create a `.env` file with your OpenAI key:

   ```
   OpenAI_API_Key=your-api-key-here
   ```

3. Install dependencies:

   ```bash
   pip install openai python-dotenv
   ```

4. Launch the app:

   ```bash
   python main.py
   ```

## 🧠 Technologies Used

- 🐍 Python 3
- 📄 JSON for structured data storage
- ⏰ datetime for time logging and sorting
- 🤖 OpenAI for smart hydration advice
- 🖥️ CLI for smooth terminal interaction

## 💾 Sample Log Entry

```json
{
  "30-06-2025": [
    {
      "time": "08:30",
      "quantity": 300
    },
    {
      "time": "11:45",
      "quantity": 500
    }
  ]
}
```

## ✅ Future Enhancements

- 🎯 Daily water intake goals with visual progress
- 📈 Weekly and monthly analytics
- 🪟 GUI version using `tkinter`
- 🔔 Reminder alerts for hydration

## 👤 Author

**Iceycoast** – Python Developer
GitHub: [https://github.com/Iceycoast](https://github.com/Iceycoast)
