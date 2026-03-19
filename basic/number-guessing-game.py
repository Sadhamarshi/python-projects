# file: number_guessing_basic.py

import random


def get_valid_input() -> int:
    """Return a valid integer input from user."""
    while True:
        user_input = input("Enter your guess (1-100): ").strip()
        if not user_input:
            print("Input cannot be empty.")
            continue
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)
        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
            continue

        return guess


def play_game() -> None:
    """Main game loop."""
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_valid_input()
        attempts += 1

        if guess == target_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low.")
        else:
            print("Too high.")


if __name__ == "__main__":
    print("Welcome to Number Guessing Game!")
    play_game()