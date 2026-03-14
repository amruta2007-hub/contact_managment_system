import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.validator import is_valid_phone, is_valid_email, is_duplicate
from src.contact import Contact

class TestValidator(unittest.TestCase):
    def test_valid_phone(self):
        self.assertTrue(is_valid_phone('1234567890'))
        self.assertFalse(is_valid_phone('12345'))

    def test_valid_email(self):
        self.assertTrue(is_valid_email('test@example.com'))
        self.assertFalse(is_valid_email('test@com'))

    def test_duplicate(self):
        contacts = [Contact('Alice', '1234567890', 'a@b.com', 'x', 'Personal')]
        self.assertTrue(is_duplicate(contacts, 'Alice', '1234567890'))
        self.assertFalse(is_duplicate(contacts, 'Bob', '0987654321'))

if __name__ == '__main__':
    unittest.main()
