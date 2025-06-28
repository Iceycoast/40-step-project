from medlog import MedicineLog
from datetime import datetime

log = MedicineLog()

def main_menu():
    while True:
        print("\n💊 Medicine Intake Logger")
        print("🩺----------------------------🩺")
        print("1️⃣  Add New Medicine")
        print("2️⃣  View All Entries")
        print("3️⃣  Exit")
        print("🩺----------------------------🩺")

        choice = input("\n👉 Choose an option (1-3): ")

        if choice == "1":
            name = input("\n💊 Enter the name of the Medicine: ")
            dose = input("\n💉 Enter the dosage you took (e.g. 500mg): ")
            time_str = input("\n⏰ Enter the time (HH:MM): ")
            date_str = input("\n📅 Enter the date (DD-MM-YYYY): ")

            try:
                time_taken = datetime.strptime(time_str, "%H:%M")
                date_taken = datetime.strptime(date_str, "%d-%m-%Y")
                result = log.add_medicine(name, dose, time_taken, date_taken)
                print(result)
            except ValueError:
                print("\n❌ Invalid date or time format. Please try again.")
                
        elif choice == "2":
            result = log.view_medicines()
            print("\n📋 Medicine Log Entries:")
            print(result)

        elif choice == "3":
            print("\n👋 Exiting... Stay healthy! 💚")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")