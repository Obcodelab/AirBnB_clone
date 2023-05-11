#!/usr/bin/python3
""" Testing the City class """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class """

    def test_instance(self):
        """ Testing instance of City class """

        city = City()
        self.assertIsInstance(city, City)

    def test_attr(self):
        """ Testing the attributes """

        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_inheritance(self):
        """ Testing inheritance of City class """

        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_str(self):
        """ Testing __str__ method of City class """

        city = City()
        string = city.__str__()
        self.assertIsInstance(string, str)

    def test_save(self):
        """ Testing save method of City class """

        city = City()
        old_updated_at = city.updated_at
        city.save()
        new_updated_at = city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """ Testing to_dict method of City class """

        city = City()
        city.state_id = "1456"
        city.name = "Houston"

        c_dict = city.to_dict()

        self.assertIsInstance(c_dict, dict)
        self.assertIn("id", c_dict)
        self.assertIn("created_at", c_dict)
        self.assertIn("updated_at", c_dict)
        self.assertIn("__class__", c_dict)

        self.assertEqual(c_dict["state_id"], "1456")
        self.assertEqual(c_dict["name"], "Houston")
        self.assertEqual(c_dict["__class__"], "City")


if __name__ == '__main__':
    unittest.main()
