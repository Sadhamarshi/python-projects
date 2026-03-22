def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    print("Even or Odd Checker")

    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting program.")
            break

        try:
            num = int(user_input)
            result = check_even_odd(num)
            print(f"{num} is {result}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()