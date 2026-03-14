import json
from pathlib import Path
from .contact import Contact

class ContactManager:
    def __init__(self, data_file):
        self.data_file = Path(data_file)
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if self.data_file.exists():
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(c) for c in data]
        else:
            self.contacts = []

    def save_contacts(self):
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def find_contact(self, name=None, phone=None):
        results = []
        for c in self.contacts:
            if name and name.lower() in c.name.lower():
                results.append(c)
            elif phone and phone == c.phone:
                results.append(c)
        return results

    def update_contact(self, old_name, new_contact):
        for i, c in enumerate(self.contacts):
            if c.name == old_name:
                self.contacts[i] = new_contact
                self.save_contacts()
                return True
        return False

    def delete_contact(self, name):
        for i, c in enumerate(self.contacts):
            if c.name == name:
                del self.contacts[i]
                self.save_contacts()
                return True
        return False

    def list_by_category(self, category):
        return [c for c in self.contacts if c.category.lower() == category.lower()]

    def get_all_contacts(self):
        return self.contacts
