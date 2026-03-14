import re

def is_valid_phone(phone):
    return re.fullmatch(r"\+?\d{10,15}", phone) is not None

def is_valid_email(email):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+", email) is not None

def is_duplicate(contacts, name, phone):
    for c in contacts:
        if c.name.lower() == name.lower() or c.phone == phone:
            return True
    return False

def required_fields_filled(data):
    return all(data.get(field) for field in ['name', 'phone', 'email', 'address', 'category'])
