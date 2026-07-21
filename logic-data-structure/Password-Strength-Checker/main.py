from password_checker import PasswordChecker

print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter Password: ")

checker = PasswordChecker(password)

checker.check_strength()