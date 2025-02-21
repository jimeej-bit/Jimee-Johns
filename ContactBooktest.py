# Simple Contact Book

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Contact {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            print(f"Contact {name} updated.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

def menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contact_book = ContactBook()

    while True:
        menu()
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number: ")
            contact_book.update_contact(name, phone)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
