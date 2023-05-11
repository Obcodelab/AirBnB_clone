#!/usr/bin/python3
""" Testing ther User class """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_attr(self):
        """Testing the attributes of User class """

        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_inherit_BaseModel(self):
        """Testing for inheritance of User class """

        user1 = User()
        self.assertIsInstance(user1, BaseModel)
        self.assertTrue(hasattr(user1, "id"))
        self.assertTrue(hasattr(user1, "created_at"))
        self.assertTrue(hasattr(user1, "updated_at"))

    def test_str(self):
        """Testing the  __str__ method of User class """

        user2 = User()

        self.assertIsInstance(str(user2), str)

    def test_save(self):
        """ Testing save method of User """

        user3 = User()
        self.assertTrue(hasattr(user3, 'updated_at'))
        old_updated = user3.updated_at
        user3.save()
        self.assertTrue(hasattr(user3, 'updated_at'))
        self.assertNotEqual(old_updated, user3.updated_at)

    def test_to_dict(self):
        """Testing to_dict method of User class"""

        user = User()
        user.email = "user@123.com"
        user.password = "456"
        user.first_name = "Mary"
        user.last_name = "Jane"

        u_dict = user.to_dict()

        self.assertIsInstance(u_dict, dict)
        self.assertIn("id", u_dict)
        self.assertIn("created_at", u_dict)
        self.assertIn("updated_at", u_dict)
        self.assertIn("__class__", u_dict)

        self.assertEqual(u_dict["email"], "user@123.com")
        self.assertEqual(u_dict["password"], "456")
        self.assertEqual(u_dict["first_name"], "Mary")
        self.assertEqual(u_dict["last_name"], "Jane")
        self.assertEqual(u_dict["__class__"], "User")


if __name__ == '__main__':
    unittest.main()
