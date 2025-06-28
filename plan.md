# 🩺 Road to Mega Project 1 – CuraLink (UHTAS)

🎯 Goal:
Build a unified health tracking system with medicine logs, health data, GUI interface, reminders, charts, and smart AI suggestions.

=========================================================
PHASE 1: Health Loggers (Q1 – Q10)
=========================================================
Learn to store and retrieve health data using JSON and CLI.

Q1 - Medicine Intake Logger | JSON, datetime, CLI
Q2 - Mood Tracker | Emoji logging, mood state
Q3 - Meal Logger | Calories, food categories
Q4 - Water Intake Tracker | Daily water goal tracking
Q5 - Sleep Tracker | Sleep time logs, duration
Q6 - BMI Calculator | Formula and input logic
Q7 - Daily Health Summary | Combine daily entries
Q8 - Symptom Checker (AI-Lite) | Keyword symptom mapping
Q9 - Mental Health Journal (AI) | Mood from journal text
Q10 - Habit Tracker | Daily habit completion

=========================================================
PHASE 2: Scheduling & Alerts (Q11 – Q20)
=========================================================
Build time-based reminders and user tracking systems.

Q11 - Appointment Scheduler | Date handling, sorting
Q12 - Emergency Contact Logger | JSON contact log
Q13 - Medicine Reminder System | Time matching logic
Q14 - Daily Checklist System | Custom to-do lists
Q15 - Health Goal Tracker | Long-term milestone system
Q16 - Calendar View CLI | View scheduled logs
Q17 - Vaccination Log | Save doses, dates
Q18 - Profile System (Multi-user) | Profile switching
Q19 - Notification System (CLI) | Warnings and reminders
Q20 - Period Tracker (Optional) | Optional advanced tracker

=========================================================
PHASE 3: GUI & OOP (Q21 – Q30)
=========================================================
Add Tkinter GUI and begin OOP design and reusable classes.

Q21 - GUI Diary App | Multi-screen Tkinter
Q22 - GUI Mood Tracker | Buttons/dropdowns
Q23 - GUI Appointment System | Calendar picker
Q24 - GUI Login/Register System | Credential storage
Q25 - GUI Reminder System | Visual alerts
Q26 - GUI Health Dashboard | Multi-frame app
Q27 - GUI BMI Calculator | Dynamic input/output
Q28 - GUI Meal Logger | Reusable entry system
Q29 - GUI Medication Viewer | Scrollable medicine list
Q30 - GUI Profile Switcher | Manage multiple profiles

=========================================================
PHASE 4: Reporting & Integration (Q31 – Q40)
=========================================================
Visualize, summarize and export data. Full system integration.

Q31 - Graph Mood Over Time | matplotlib + emotion tracking
Q32 - Weekly Health Summary | Compile and summarize logs
Q33 - Meal & Calorie Charts | Pie and bar charts
Q34 - Sleep Pattern Visualizer | Graph sleep quality
Q35 - Export Health Report | JSON or PDF using reportlab
Q36 - Encrypt Journals | Encrypt/decrypt text logs
Q37 - Modular Data Manager | Class-based structure
Q38 - Master Settings Panel | App config + control
Q39 - Emergency Dashboard | 1-screen critical info view
Q40 - Final CuraLink Full App | Integration of all modules

=========================================================
🤖 AI INTEGRATION POINTS
=========================================================

- Q8: Symptom Checker → Rule-based or LLM-assisted diagnosis
- Q9: Mood Journal → Sentiment detection (VADER/TextBlob/GPT)
- Q31–Q35: Auto report summarizer with GPT or local LLM
- Q40: Chatbot Assistant → Natural language interface
- Optional: Voice input → `SpeechRecognition` / Whisper

Tools:

- TextBlob / VADER (Free)
- GPT API (Optional, Paid)
- spaCy / Rasa / LangChain (Free Advanced Options)

=========================================================
📦 DATA SOURCES USED
=========================================================
All data is entered by user via CLI or GUI forms:

- `medicines.json` → Logs meds taken (Q1)
- `mood.json` → Mood entries (Q2, Q9)
- `meals.json` → Food entries and calories (Q3)
- `water.json` → Daily water log (Q4)
- `sleep.json` → Sleep duration (Q5)
- `symptoms.json` → Text-based symptoms (Q8)
- `appointments.json` → Appointment list (Q11)
- `goals.json` → Long-term health goals (Q15)
- `users.json` → Profiles and preferences (Q18)
- `journal.json` → Mental health notes (Q9)

=========================================================
📁 SAMPLE FILE STRUCTURE FOR Q1: MEDICINE LOGGER
=========================================================
medicine_logger/
├── main.py ← entry point
├── menu.py ← CLI menu
├── medlog.py ← logging functions
├── data/
│ └── medicines.json ← stores logs

Each entry stored like:
{
"name": "Paracetamol",
"dose": "500mg",
"time": "20:00",
"date": "2025-06-28"
}

=========================================================
🧠 YOU CAN START RIGHT NOW!
=========================================================
You already have the skills to build Q1–Q5 fully:

- JSON read/write
- CLI input
- `datetime` handling
- File structures
- Modular Python files

We'll add AI, GUI, charts and chatbot step-by-step. This is your 40-step journey to build a real health companion.
