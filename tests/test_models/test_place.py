#!/usr/bin/python3
""" Testing the Place class """
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_instance(self):
        """Testing instance of Place class"""

        place = Place()
        self.assertIsInstance(place, Place)

    def test_attr(self):
        """Testing the attributes of Place class"""

        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_inheritance(self):
        """Testing inheritance of Place class"""

        place1 = Place()
        self.assertIsInstance(place1, BaseModel)
        self.assertTrue(hasattr(place1, "id"))
        self.assertTrue(hasattr(place1, "created_at"))
        self.assertTrue(hasattr(place1, "updated_at"))

    def test_str(self):
        """Testing __str__ method of Place class"""

        place2 = Place()
        string = place2.__str__()
        self.assertIsInstance(string, str)

    def test_save(self):
        """Testing save method of Place class"""

        place3 = Place()
        self.assertTrue(hasattr(place3, "updated_at"))
        old_updated = place3.updated_at
        place3.save()
        self.assertTrue(hasattr(place3, "updated_at"))
        self.assertNotEqual(old_updated, place3.updated_at)

    def test_to_dict(self):
        """Testing to_dict method of Place class"""

        place4 = Place()
        place4.city_id = "Ede"
        place4.user_id = "001"
        place4.name = "John Smith"
        place4.description = "A lawyer"
        place4.number_rooms = 2
        place4.number_bathrooms = 1
        place4.max_guest = 3
        place4.price_by_night = 4500
        place4.latitude = 30.0
        place4.longitude = 120.0
        place4.amenity_ids = ["wifi", "soap", "towels"]
        p_dict = place4.to_dict()

        self.assertIsInstance(p_dict, dict)
        self.assertIn("id", p_dict)
        self.assertIn("created_at", p_dict)
        self.assertIn("updated_at", p_dict)
        self.assertIn("__class__", p_dict)

        self.assertEqual(p_dict["city_id"], "Ede")
        self.assertEqual(p_dict["user_id"], "001")
        self.assertEqual(p_dict["name"], "John Smith")
        self.assertEqual(p_dict["description"], "A lawyer")
        self.assertEqual(p_dict["number_rooms"], 2)
        self.assertEqual(p_dict["number_bathrooms"], 1)
        self.assertEqual(p_dict["max_guest"], 3)
        self.assertEqual(p_dict["price_by_night"], 4500)
        self.assertEqual(p_dict["latitude"], 30.0)
        self.assertEqual(p_dict["longitude"], 120.0)
        self.assertEqual(p_dict["amenity_ids"], ["wifi", "soap", "towels"])
        self.assertEqual(p_dict["__class__"], "Place")


if __name__ == "__main__":
    unittest.main()
