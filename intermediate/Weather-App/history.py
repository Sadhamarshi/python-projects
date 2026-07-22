"""
history.py
-----------
Handles saving and displaying weather search history.
"""

import os

HISTORY_FILE = "history.txt"


def create_history_file():
    """
    Creates history.txt if it doesn't already exist.
    """
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8"):
            pass


def save_history(city, country):
    """
    Saves a successful weather search.
    """

    create_history_file()

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{city}, {country}\n")


def view_history():
    """
    Displays search history.
    """

    create_history_file()

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        history = file.readlines()

    if not history:
        print("\nNo search history found.")
        return

    print("\n========== SEARCH HISTORY ==========\n")

    for index, city in enumerate(history, start=1):
        print(f"{index}. {city.strip()}")

    print()


def clear_history():
    """
    Clears all search history.
    """

    create_history_file()

    with open(HISTORY_FILE, "w", encoding="utf-8"):
        pass

    print("\nSearch history cleared successfully.\n")