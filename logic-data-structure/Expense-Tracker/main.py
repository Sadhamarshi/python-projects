from expense import Expense

expenses = []


def add_expense():
    title = input("Enter Expense Title: ")
    amount = float(input("Enter Amount: ₹"))
    category = input("Enter Category: ")

    expenses.append(Expense(title, amount, category))

    print("\nExpense Added Successfully!\n")


def view_expenses():
    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n===== EXPENSES =====")

    total = 0

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(expense)
        total += expense.amount

    print("\n--------------------------")
    print(f"Total Expenses : ₹{total:.2f}\n")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    choice = int(input("Enter Expense Number to Delete: "))

    if 1 <= choice <= len(expenses):
        expenses.pop(choice - 1)
        print("Expense Deleted Successfully!\n")
    else:
        print("Invalid Choice.\n")


def search_category():
    category = input("Enter Category: ")

    found = False

    print()

    for expense in expenses:
        if expense.category.lower() == category.lower():
            print(expense)
            print("-" * 25)
            found = True

    if not found:
        print("No expenses found.\n")


while True:

    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_category()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")