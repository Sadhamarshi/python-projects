"""
main.py
--------
Main entry point for the Weather App.
"""

from weather import get_weather
from history import (
    save_history,
    view_history,
    clear_history
)
from utils import (
    print_weather,
    title
)


def choose_unit():
    """
    Allows the user to choose Celsius or Fahrenheit.
    """

    while True:
        print("\nChoose Temperature Unit")
        print("1. Celsius (°C)")
        print("2. Fahrenheit (°F)")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            return "metric"

        elif choice == "2":
            return "imperial"

        else:
            print("Invalid choice. Try again.")


def search_weather():
    """
    Handles weather search.
    """

    city = input("\nEnter City Name: ").strip()

    if city == "":
        print("City name cannot be empty.")
        return

    unit = choose_unit()

    success, result = get_weather(city, unit)

    if success:
        print_weather(result, unit)
        save_history(result["name"], result["sys"]["country"])

    else:
        print(f"\nError: {result}")


def menu():
    """
    Displays the main menu.
    """

    while True:

        title("WEATHER APP")

        print("1. Search Weather")
        print("2. View Search History")
        print("3. Clear Search History")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            search_weather()

        elif choice == "2":
            view_history()

        elif choice == "3":

            confirm = input(
                "\nAre you sure you want to clear history? (y/n): "
            ).lower()

            if confirm == "y":
                clear_history()

        elif choice == "4":
            print("\nThank you for using Weather App!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    menu()