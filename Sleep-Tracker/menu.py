from tracker import Sleep, SleepTracker

if __name__ == "__main__":
    tracker = SleepTracker()

    while True:
        print("\n🌙 Sleep Tracker Menu")
        print("=" * 30)
        print("1. Log Sleep & Wake Time")
        print("2. View All Sleep Logs")
        print("3. Analyze Sleep (Last 7 Days)")
        print("4. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            sleep_time = input("Enter sleep time (e.g. 11:00 PM): ").strip()
            wake_time = input("Enter wake time (e.g. 7:00 AM): ").strip()
            result = tracker.log_sleep_wake_time(sleep_time, wake_time)
            print(result)

        elif choice == "2":
            print("\n" + tracker.view_logs())

        elif choice == "3":
            print("Analyzing Data...")
            print("\n" + tracker.ai_sleep_analyzer())

        elif choice == "4":
            print("👋 Exiting Sleep Tracker. Stay healthy!")
            break

        else:
            print("❌ Invalid choice. Please enter 1-4.")
