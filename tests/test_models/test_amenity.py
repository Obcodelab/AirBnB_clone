#!/usr/bin/python3
""" Testing the Amenity class """
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def test_instance(self):
        """Testing instance of Amenity class"""

        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attr(self):
        """Testing the attributes of Amenity class"""

        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertIsInstance(amenity.name, str)

    def test_inheritance(self):
        """Testing inheritance of Amenity class"""

        amenity1 = Amenity()
        self.assertIsInstance(amenity1, BaseModel)
        self.assertTrue(hasattr(amenity1, "id"))
        self.assertTrue(hasattr(amenity1, "created_at"))
        self.assertTrue(hasattr(amenity1, "updated_at"))

    def test_str(self):
        """Testing __str__ method of Amenity class"""

        amenity2 = Amenity()
        string = amenity2.__str__()
        self.assertIsInstance(string, str)

    def test_save(self):
        """Testing save method of Amenity class"""

        amenity3 = Amenity()
        self.assertTrue(hasattr(amenity3, "updated_at"))
        old_updated = amenity3.updated_at
        amenity3.save()
        self.assertTrue(hasattr(amenity3, "updated_at"))
        self.assertNotEqual(old_updated, amenity3.updated_at)

    def test_to_dict(self):
        """Testing to_dict method of Amenity class"""

        amenity4 = Amenity()
        amenity4.name = "Wifi"
        a_dict = amenity4.to_dict()

        self.assertIsInstance(a_dict, dict)
        self.assertIn("id", a_dict)
        self.assertIn("created_at", a_dict)
        self.assertIn("updated_at", a_dict)
        self.assertIn("__class__", a_dict)

        self.assertEqual(a_dict["name"], "Wifi")
        self.assertEqual(a_dict["__class__"], "Amenity")


if __name__ == "__main__":
    unittest.main()
