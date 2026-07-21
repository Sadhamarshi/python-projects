print("===== Python Quiz Game =====")
print()

score = 0

answer = input("1. What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Central Processing Unit.\n")

answer = input("2. Which keyword is used to define a function in Python? ").lower()

if answer == "def":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is def.\n")

answer = input("3. Which symbol is used for comments in Python? ")

if answer == "#":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is #.\n")

answer = input("4. What is the output of 5 + 3? ")

if answer == "8":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 8.\n")

answer = input("5. Which data type stores True or False values? ").lower()

if answer == "boolean" or answer == "bool":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Boolean (bool).\n")

print("=" * 30)
print(f"Your Final Score: {score}/5")
print("=" * 30)

percentage = (score / 5) * 100
print(f"Percentage: {percentage}%")

if percentage == 100:
    print("Excellent! 🎉")
elif percentage >= 80:
    print("Great Job! 😊")
elif percentage >= 60:
    print("Good! Keep Practicing.")
else:
    print("Keep Learning Python!")