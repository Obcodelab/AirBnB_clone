#!/usr/bin/python3
""" Testing the Review class """
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_instance(self):
        """Testing instance of Review class"""

        review = Review()
        self.assertIsInstance(review, Review)

    def test_attr(self):
        """Testing the attributes of Review class"""

        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_inheritance(self):
        """Testing inheritance of Review class"""

        review1 = Review()
        self.assertIsInstance(review1, BaseModel)
        self.assertTrue(hasattr(review1, "id"))
        self.assertTrue(hasattr(review1, "created_at"))
        self.assertTrue(hasattr(review1, "updated_at"))

    def test_str(self):
        """Testing __str__ method of Amenity class"""

        review2 = Review()
        string = review2.__str__()
        self.assertIsInstance(string, str)

    def test_save(self):
        """Testing save method of Amenity class"""

        review3 = Review()
        self.assertTrue(hasattr(review3, "updated_at"))
        old_updated = review3.updated_at
        review3.save()
        self.assertTrue(hasattr(review3, "updated_at"))
        self.assertNotEqual(old_updated, review3.updated_at)

    def test_to_dict(self):
        """Testing to_dict method of Review class"""

        review4 = Review()
        review4.place_id = "Oke"
        review4.user_id = "002"
        review4.text = "Good"
        r_dict = review4.to_dict()

        self.assertIsInstance(r_dict, dict)
        self.assertIn("id", r_dict)
        self.assertIn("created_at", r_dict)
        self.assertIn("updated_at", r_dict)
        self.assertIn("__class__", r_dict)

        self.assertEqual(r_dict["place_id"], "Oke")
        self.assertEqual(r_dict["user_id"], "002")
        self.assertEqual(r_dict["text"], "Good")
        self.assertEqual(r_dict["__class__"], "Review")


if __name__ == "__main__":
    unittest.main()
