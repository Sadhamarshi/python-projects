import random


def roll_dice(num_dice):
    rolls = []

    for _ in range(num_dice):
        rolls.append(random.randint(1, 6))

    total = sum(rolls)
    return rolls, total


def main():
    print("Dynamic Dice Rolling Simulator 🎲")

    while True:
        user_input = input("\nEnter number of dice (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting simulator.")
            break

        try:
            num_dice = int(user_input)

            if num_dice <= 0:
                print("Number must be greater than 0.")
                continue

            rolls, total = roll_dice(num_dice)

            print(f"Rolled Dice: {rolls}")
            print(f"Total: {total}")

        except ValueError:
            print("Invalid input. Enter a valid number.")


if __name__ == "__main__":
    main()