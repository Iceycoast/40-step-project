from tracker import BMITracker
from bmi import BMI
from analyzer import generate_summary

def menu():
    tracker = BMITracker()

    while True:
        print("\n📘 BMI Tracker Menu")
        print("1. Add new BMI entry")
        print("2. View entries")
        print("3. Delete entries for a user")
        print("4. Generate AI health summary")
        print("5. Show log count for a user")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            age = int(input("Age: ").strip())
            gender = input("Gender (Male/Female): ").strip()
            height = float(input("Height (cm): ").strip())
            weight = float(input("Weight (kg): ").strip())
            bmi_entry = BMI(name, age, gender, height, weight)
            print(tracker.add_data(bmi_entry))

        elif choice == "2":
            print("\n📂 View Options:")
            print("1. View all entries")
            print("2. View entries for a specific user")

            sub_choice = input("Enter choice (1 or 2): ").strip()

            if sub_choice == "1":
                print(tracker.view_data())

            elif sub_choice == "2":
                name = input("Enter user name: ").strip()
                print(tracker.view_logs_by_name(name))

            else:
                print("❌ Invalid sub-choice. Returning to main menu.")


        elif choice == "3":
            name = input("Enter the user's name: ").strip()
            entries = tracker.get_entries_for(name)

            if not entries:
                print(f"No entries found for {name}.")
            else:
                print("\nWhat do you want to delete?")
                print("1. Delete all entries for this user")
                print("2. Delete a specific entry by index")

                sub_choice = input("Enter choice (1 or 2): ").strip()

                if sub_choice == "1":
                    print(tracker.delete_all_by_name(name))

                elif sub_choice == "2":
                    for idx, entry in enumerate(entries, 1):
                        print(f"{idx}. {entry['date']} - BMI: {entry['bmi']} - {entry['category']}")
                    index = int(input("Enter the index of the entry to delete: ").strip())
                    print(tracker.delete_entry_by_index(name, index))

                else:
                    print("❌ Invalid sub-choice. Returning to main menu.")

        elif choice == "4":
            name = input("Enter name to generate summary: ").strip()
            print(generate_summary(name))

        elif choice == "5":
            name = input("Enter name: ").strip()
            count = tracker.get_user_log_count(name)
            print(f"{name} has {count} entr{'y' if count == 1 else 'ies'}.")

        elif choice == "6":
            print("👋 Exiting BMI Tracker. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a number from 1 to 6.")
