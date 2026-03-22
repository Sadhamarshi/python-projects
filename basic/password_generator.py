import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Random Password Generator")

    while True:
        user_input = input("\nEnter password length (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting program.")
            break

        try:
            length = int(user_input)
            if length <= 0:
                print("Length must be positive.")
                continue

            password = generate_password(length)
            print("Generated Password:", password)

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()