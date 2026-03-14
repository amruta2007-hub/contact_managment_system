import sys
from src.manager import ContactManager
from src.contact import Contact
from src.validator import is_valid_phone, is_valid_email, is_duplicate, required_fields_filled
from src.file_handler import export_to_json, import_from_json, export_to_csv, import_from_csv
from pathlib import Path

def print_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. List by Category")
    print("7. Export Contacts")
    print("8. Import Contacts")
    print("9. Exit")

def get_contact_input():
    data = {}
    data['name'] = input("Name: ").strip()
    data['phone'] = input("Phone: ").strip()
    data['email'] = input("Email: ").strip()
    data['address'] = input("Address: ").strip()
    data['category'] = input("Category (Personal/Professional/Family): ").strip()
    return data

def main():
    data_file = Path('data/contacts.json')
    manager = ContactManager(data_file)
    while True:
        print_menu()
        choice = input("Select an option: ").strip()
        if choice == '1':
            data = get_contact_input()
            if not required_fields_filled(data):
                print("All fields are required.")
                continue
            if not is_valid_phone(data['phone']):
                print("Invalid phone format.")
                continue
            if not is_valid_email(data['email']):
                print("Invalid email format.")
                continue
            if is_duplicate(manager.contacts, data['name'], data['phone']):
                print("Duplicate contact.")
                continue
            contact = Contact(**data)
            manager.add_contact(contact)
            print("Contact added.")
        elif choice == '2':
            contacts = manager.get_all_contacts()
            for c in contacts:
                print(c.to_dict())
        elif choice == '3':
            q = input("Search by name or phone: ").strip()
            results = manager.find_contact(name=q) or manager.find_contact(phone=q)
            if results:
                for c in results:
                    print(c.to_dict())
            else:
                print("No contact found.")
        elif choice == '4':
            old_name = input("Enter name of contact to update: ").strip()
            found = manager.find_contact(name=old_name)
            if not found:
                print("Contact not found.")
                continue
            data = get_contact_input()
            if not required_fields_filled(data):
                print("All fields are required.")
                continue
            if not is_valid_phone(data['phone']):
                print("Invalid phone format.")
                continue
            if not is_valid_email(data['email']):
                print("Invalid email format.")
                continue
            new_contact = Contact(**data)
            if manager.update_contact(old_name, new_contact):
                print("Contact updated.")
            else:
                print("Update failed.")
        elif choice == '5':
            name = input("Enter name of contact to delete: ").strip()
            confirm = input(f"Are you sure you want to delete {name}? (y/n): ").strip().lower()
            if confirm == 'y':
                if manager.delete_contact(name):
                    print("Contact deleted.")
                else:
                    print("Contact not found.")
        elif choice == '6':
            category = input("Enter category: ").strip()
            contacts = manager.list_by_category(category)
            for c in contacts:
                print(c.to_dict())
        elif choice == '7':
            fmt = input("Export format (json/csv): ").strip().lower()
            path = input("Export file path: ").strip()
            contacts = manager.get_all_contacts()
            try:
                if fmt == 'json':
                    export_to_json(contacts, path)
                elif fmt == 'csv':
                    export_to_csv(contacts, path)
                else:
                    print("Invalid format.")
                    continue
                print("Exported successfully.")
            except Exception as e:
                print(f"Export failed: {e}")
        elif choice == '8':
            fmt = input("Import format (json/csv): ").strip().lower()
            path = input("Import file path: ").strip()
            try:
                if fmt == 'json':
                    contacts = import_from_json(path)
                elif fmt == 'csv':
                    contacts = import_from_csv(path)
                else:
                    print("Invalid format.")
                    continue
                for c in contacts:
                    if not is_duplicate(manager.contacts, c.name, c.phone):
                        manager.add_contact(c)
                print("Imported successfully.")
            except Exception as e:
                print(f"Import failed: {e}")
        elif choice == '9':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
