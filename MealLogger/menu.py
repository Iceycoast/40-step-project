from meal_logger import Meal    
from meal_logger import MealLogger
from datetime import datetime

logger = MealLogger()

def menu():
    while True:
        print("\nStarting Meal logger")
        print("-" * 20)
        print("1. Add Meals")
        print("2. View Meals")
        print("3. Total calories")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Meal name: ")
            try:
                calories = int(input("Calories: "))
            except ValueError:
                print("Please enter a valid number for calories.\n")
                continue
            mealtype = input("Meal Type (Breakfast/Lunch/Dinner/Snack): ").lower()
            time = datetime.now()

            meal = Meal(name, calories, mealtype, time)
            logger.add_meal(meal)
            
            suggestion = logger.ai_suggest_healthier(meal)
            print(f"\nAI Suggestion: {suggestion}\n")

        elif choice == "2":
            meals = logger.view_today_meals()
            if not meals:
                print("\nNo meals logged for today.\n")
            else:
                print("\nToday's Meals:")
                for idx, meal in enumerate(meals, 1):
                    print(f"{idx}. {meal['name']} | {meal['calories']} cal | {meal['meal type'].capitalize()} | {meal['time']}")
                print()

        elif choice == "3":
            total = logger.total_calories()
            print(f"\nTotal calories consumed today: {total}\n")

        elif choice == "4":
            print("Exiting Meal Logger. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    menu()