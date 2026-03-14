from datetime import datetime

class Contact:
    def __init__(self, name, phone, email, address, category, date_added=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.category = category
        self.date_added = date_added or datetime.now().isoformat()

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'category': self.category,
            'date_added': self.date_added
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            name=data['name'],
            phone=data['phone'],
            email=data['email'],
            address=data['address'],
            category=data['category'],
            date_added=data.get('date_added')
        )
