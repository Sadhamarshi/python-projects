def generate_table(number, limit):
    print(f"\nMultiplication Table for {number}:\n")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


def main():
    print("Multiplication Table Generator")

    while True:
        user_input = input("\nEnter a number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting program.")
            break

        try:
            num = int(user_input)
            limit = int(input("Enter range limit (e.g., 10): "))
            generate_table(num, limit)
        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()