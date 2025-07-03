from aggregator import get_aggregated_data
from ai_summary import generate_summary

def display_dates(dates: list):
    print("\n📅 Available Dates:")
    for i, date in enumerate(sorted(dates), 1):
        print(f"{i}. {date}")

def menu():
    data_by_date = get_aggregated_data()

    while True:
        print("\n🩺 Health Summary Menu")
        print("1. View all available dates")
        print("2. Get AI health summary for a specific date")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            display_dates(list(data_by_date.keys()))

        elif choice == '2':
            display_dates(list(data_by_date.keys()))
            date = input("\nEnter the date (DD-MM-YYYY): ").strip()
            data = data_by_date.get(date)
            if data:
                summary = generate_summary(date, data)
                print(f"\n🧠 AI Summary for {date}:\n{summary}")
            else:
                print("⚠️ No data found for that date.")

        elif choice == '3':
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    menu()
