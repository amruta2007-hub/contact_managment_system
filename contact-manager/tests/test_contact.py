import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.contact import Contact

class TestContact(unittest.TestCase):
    def test_to_dict_and_from_dict(self):
        c = Contact('Alice', '1234567890', 'alice@example.com', '123 St', 'Personal')
        d = c.to_dict()
        c2 = Contact.from_dict(d)
        self.assertEqual(c.name, c2.name)
        self.assertEqual(c.phone, c2.phone)
        self.assertEqual(c.email, c2.email)
        self.assertEqual(c.address, c2.address)
        self.assertEqual(c.category, c2.category)

if __name__ == '__main__':
    unittest.main()
