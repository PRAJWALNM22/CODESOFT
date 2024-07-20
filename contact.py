class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Enter new details for the contact:")
                contact.name = input("Name: ")
                contact.phone = input("Phone: ")
                contact.email = input("Email: ")
                contact.address = input("Address: ")
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

contact_book = ContactBook()

while True:
    display_menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contact = Contact(name, phone, email, address)
        contact_book.add_contact(contact)
    elif choice == "2":
        contact_book.view_contacts()
    elif choice == "3":
        search_term = input("Enter name or phone number to search: ")
        contact_book.search_contact(search_term)
    elif choice == "4":
        name = input("Enter the name of the contact to update: ")
        contact_book.update_contact(name)
    elif choice == "5":
        name = input("Enter the name of the contact to delete: ")
        contact_book.delete_contact(name)
    elif choice == "6":
        print("Exiting the contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

