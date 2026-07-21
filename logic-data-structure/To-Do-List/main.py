from task import Task

tasks = []


def add_task():
    title = input("Enter task: ")
    tasks.append(Task(title))
    print("Task added successfully.\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    print("\nTo-Do List")
    print("-" * 30)

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print()


def complete_task():
    view_tasks()

    if not tasks:
        return

    choice = int(input("Enter task number to complete: "))
    tasks[choice - 1].mark_completed()

    print("Task marked as completed.\n")


def delete_task():
    view_tasks()

    if not tasks:
        return

    choice = int(input("Enter task number to delete: "))
    tasks.pop(choice - 1)

    print("Task deleted.\n")


while True:

    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")