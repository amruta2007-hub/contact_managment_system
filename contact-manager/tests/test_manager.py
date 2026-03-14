import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.manager import ContactManager
from src.contact import Contact

test_file = 'data/test_contacts.json'

class TestContactManager(unittest.TestCase):
    def setUp(self):
        os.makedirs(os.path.dirname(test_file), exist_ok=True)
        self.manager = ContactManager(test_file)
        self.manager.contacts = []
        self.manager.save_contacts()

    def tearDown(self):
        if os.path.exists(test_file):
            os.remove(test_file)

    def test_add_and_find_contact(self):
        c = Contact('Bob', '9876543210', 'bob@example.com', '456 Ave', 'Professional')
        self.manager.add_contact(c)
        found = self.manager.find_contact(name='Bob')
        self.assertTrue(found)
        self.assertEqual(found[0].name, 'Bob')

if __name__ == '__main__':
    unittest.main()
