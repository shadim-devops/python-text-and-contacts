contacts = {}
next_id = 1

while True:
    print("\nContact Manager")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Search contacts")
    print("4. Delete contact")
    print("5. Edit contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("First name: ")
        surname = input("Last name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        if not phone.isdigit():
            print("Phone number must contain digits only")
            continue

        contacts[next_id] = {
            "first_name": name,
            "last_name": surname,
            "phone": phone,
            "email": email
        }

        print("Contact added")
        next_id += 1

    elif choice == "2":
        if not contacts:
            print("No contacts found")
        else:
            for cid, data in contacts.items():
                print(cid, data)

    elif choice == "3":
        search = input("Enter first or last name: ").lower()

        found = False

        for cid, data in contacts.items():
            if search in data["first_name"].lower() or search in data["last_name"].lower():
                print(cid, data)
                found = True

        if not found:
            print("Contact not found")

    elif choice == "4":
        cid = int(input("Enter contact ID to delete: "))

        if cid in contacts:
            del contacts[cid]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "5":
        cid = int(input("Enter contact ID to edit: "))

        if cid in contacts:
            name = input("New first name: ")
            surname = input("New last name: ")
            phone = input("New phone: ")
            email = input("New email: ")

            contacts[cid] = {
                "first_name": name,
                "last_name": surname,
                "phone": phone,
                "email": email
            }

            print("Contact updated")
        else:
            print("Contact not found")

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid option")