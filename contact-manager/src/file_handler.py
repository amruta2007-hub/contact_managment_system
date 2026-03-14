import json
import csv
from pathlib import Path
from .contact import Contact

def export_to_json(contacts, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([c.to_dict() for c in contacts], f, indent=2)

def import_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [Contact.from_dict(c) for c in data]

def export_to_csv(contacts, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email', 'address', 'category', 'date_added'])
        writer.writeheader()
        for c in contacts:
            writer.writerow(c.to_dict())

def import_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [Contact.from_dict(row) for row in reader]
