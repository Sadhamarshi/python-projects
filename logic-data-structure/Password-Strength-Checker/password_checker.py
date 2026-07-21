import re


class PasswordChecker:

    def __init__(self, password):
        self.password = password

    def check_strength(self):

        length = len(self.password) >= 8
        uppercase = bool(re.search(r"[A-Z]", self.password))
        lowercase = bool(re.search(r"[a-z]", self.password))
        digit = bool(re.search(r"\d", self.password))
        special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password))

        score = sum([length, uppercase, lowercase, digit, special])

        print("\n===== PASSWORD ANALYSIS =====")
        print(f"Length (8+)      : {'✔' if length else '✘'}")
        print(f"Uppercase Letter : {'✔' if uppercase else '✘'}")
        print(f"Lowercase Letter : {'✔' if lowercase else '✘'}")
        print(f"Digit            : {'✔' if digit else '✘'}")
        print(f"Special Character: {'✔' if special else '✘'}")

        print("\nPassword Strength:")

        if score == 5:
            print("🟢 Strong")
        elif score >= 3:
            print("🟡 Medium")
        else:
            print("🔴 Weak")