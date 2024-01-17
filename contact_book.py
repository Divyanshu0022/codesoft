class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self):
        name = input("Enter name to search: ")
        for contact in self.contacts:
            if contact.name == name:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                return
        print("Contact not found.")

    def update_contact(self):
        name = input("Enter name to update: ")
        phone = input("Enter new phone (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        for contact in self.contacts:
            if contact.name == name:
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                print(f"Contact {name} updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter name to delete: ")
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact {name} deleted successfully!")
                return
        print("Contact not found.")

# Create a new contact book
my_contacts = ContactBook()

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        my_contacts.add_contact()
    elif choice == '2':
        my_contacts.view_contacts()
    elif choice == '3':
        my_contacts.search_contact()
    elif choice == '4':
        my_contacts.update_contact()
    elif choice == '5':
        my_contacts.delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
