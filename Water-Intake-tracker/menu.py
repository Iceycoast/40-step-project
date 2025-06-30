from datetime import datetime
from tracker import Water, IntakeTracker  

def input_time():
    while True:
        try:
            time_str = input("Enter time (HH:MM): ")
            return datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            print("❌ Invalid time format. Please use HH:MM (24-hour format).")

def input_quantity():
    while True:
        try:
            return int(input("Enter water quantity in ml: "))
        except ValueError:
            print("❌ Please enter a valid number.")

def input_date():
    while True:
        try:
            date_str = input("Enter date (DD-MM-YYYY): ")
            datetime.strptime(date_str, "%d-%m-%Y")  # Validate format
            return date_str
        except ValueError:
            print("❌ Invalid date format. Use DD-MM-YYYY.")

def run_menu():
    tracker = IntakeTracker()

    while True:
        print("\n💧 Water Intake Tracker")
        print("1. Add new water log")
        print("2. View today's logs")
        print("3. View total intake today")
        print("4. View logs for a specific date")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            time = input_time()
            qty = input_quantity()
            water = Water(time, qty)
            tracker.add_log(water)
            print("✅ Log added.")

            print("\n🤖 Fetching AI hydration tip...")
            suggestion = tracker.ai_goal()
            print(f"💡 AI tip: {suggestion}")

        elif choice == '2':
            logs = tracker.view_daily_logs()
            if logs:
                print(f"\n📅 Logs for {datetime.now().strftime('%d-%m-%Y')}:")
                for log in logs:
                    print(f"🕒 {log['time']} - {log['quantity']} ml")
            else:
                print("📭 No logs found for today.")

        elif choice == '3':
            total = tracker.total_water_intake()
            print(f"💧 Total water intake today: {total} ml")

        elif choice == '4':
            date = input_date()
            logs = tracker.view_daily_logs(date)
            if logs:
                print(f"\n📅 Logs for {date}:")
                for log in logs:
                    print(f"🕒 {log['time']} - {log['quantity']} ml")
            else:
                print("📭 No logs found for that date.")

        elif choice == '5':
            print("👋 Exiting. Stay hydrated, Brother!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    run_menu()
