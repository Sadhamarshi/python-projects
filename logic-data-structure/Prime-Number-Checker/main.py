from prime_checker import PrimeChecker

print("===== PRIME NUMBER CHECKER =====")

try:
    number = int(input("Enter a number: "))

    checker = PrimeChecker(number)

    if checker.is_prime():
        print(f"\n{number} is a Prime Number.")
    else:
        print(f"\n{number} is NOT a Prime Number.")

except ValueError:
    print("Please enter a valid integer.")