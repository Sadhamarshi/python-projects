from contact import Contact

contacts = {}


def add_contact():
    name = input("Enter Name: ")

    if name in contacts:
        print("Contact already exists.\n")
        return

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = Contact(name, phone, email)

    print("Contact added successfully.\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n===== CONTACT LIST =====")

    for contact in contacts.values():
        print(contact)
        print("-" * 25)


def search_contact():
    name = input("Enter Name to Search: ")

    if name in contacts:
        print()
        print(contacts[name])
    else:
        print("Contact not found.")

    print()


def update_contact():
    name = input("Enter Contact Name: ")

    if name not in contacts:
        print("Contact not found.\n")
        return

    phone = input("Enter New Phone Number: ")
    email = input("Enter New Email: ")

    contacts[name].phone = phone
    contacts[name].email = email

    print("Contact updated successfully.\n")


def delete_contact():
    name = input("Enter Contact Name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")


while True:

    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.\n")