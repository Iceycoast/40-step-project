from mood_utils import log_mood, view_logs, search_logs, clear_logs
from colorama import init, Fore, Style

# 🎨 Initialize colorama
init(autoreset=True)

def show_menu():
    while True:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}📋 Mood Tracker Menu")
        print(f"{Fore.YELLOW}[1]{Style.RESET_ALL} 😊 Log Mood")
        print(f"{Fore.YELLOW}[2]{Style.RESET_ALL} 📖 View All Logs")
        print(f"{Fore.YELLOW}[3]{Style.RESET_ALL} 🔍 Search Logs")
        print(f"{Fore.YELLOW}[4]{Style.RESET_ALL} 🧹 Clear All Logs")
        print(f"{Fore.YELLOW}[5]{Style.RESET_ALL} ❌ Exit")

        choice = input(f"\n{Fore.GREEN}📥 Select an option (1–5): {Style.RESET_ALL}").strip()

        if choice == "1":
            log_mood()
        elif choice == "2":
            print("\n" + view_logs())
        elif choice == "3":
            print("\n" + search_logs())
        elif choice == "4":
            clear_logs()
        elif choice == "5":
            print(f"\n{Fore.MAGENTA}👋 Exiting Mood Tracker. Stay emotionally aware! 💚")
            break
        else:
            print(f"{Fore.RED}❌ Invalid option. Please choose 1–5.")


