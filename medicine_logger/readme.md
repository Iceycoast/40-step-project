# 💊 Medicine Intake Logger (CLI)

A sleek and efficient Python-based CLI application designed to help users log and manage daily medicine intake. Built for simplicity and usability, it's ideal for personal tracking or caregiving situations.

## ⚙️ Features

- ✍️ Add new medicine entries with name, dose, date, and time
- 📅 Entries automatically sorted by date and time
- 🚫 Duplicate prevention for accurate logging
- 📖 Chronological display of logs
- 💾 Local data storage using JSON
- 🧩 Lightweight and easy to use, perfect for beginners

## 🗂️ Project Structure

MedicineLogger/
├── data/
│ └── medicines.json – stores all logs
├── medlog.py – defines core classes
├── menu.py – handles user interaction
└── main.py – entry point to launch the app

## 🚀 How to Run

1. Ensure Python 3 is installed on your system
2. Open terminal and navigate to the project folder
3. Run the application with:

   ```bash
   python main.py
   ```

## 🧠 Technologies Used

- 🐍 Python 3
- 📄 JSON for structured data storage
- ⏰ datetime module for formatting and sorting
- 🖥️ CLI for intuitive terminal interaction

## 🔒 Sample Log Entry

```json
{
  "name": "Paracetamol",
  "dose": "500mg",
  "time taken": "08:00",
  "date taken": "28-06-2025"
}
```

## ✅ Future Enhancements

- 🪟 GUI version using `tkinter`
- 🤖 AI-powered intake summaries
- 🔗 API integration with health tracking services
- 🔔 Notifications and medicine reminders

## 👤 Author

**Iceycoast** – Python Developer on the Road to Mega Project 1
