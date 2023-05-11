#!/usr/bin/python3
""" Testing the BaseModel class """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_init(self):
        """Testing initialization of BaseModel."""

        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_init_kwargs(self):
        """ Testing initialization of BaseModel with kwargs """

        k_dict = {
            "id": "26d43177-cc3f-4d6c-a0c1-e167f8c27335",
            "created_at": "2023-05-01T00:00:00.000000",
            "updated_at": "2023-05-01T00:00:00.000000",
            "name": "base",
            'my_number': 4
        }
        bm2 = BaseModel(**k_dict)
        self.assertIsInstance(bm2, BaseModel)
        self.assertTrue(hasattr(bm2, "id"))
        self.assertTrue(hasattr(bm2, "created_at"))
        self.assertTrue(hasattr(bm2, "updated_at"))
        self.assertIsInstance(bm2.id, str)
        self.assertEqual(bm2.id, "26d43177-cc3f-4d6c-a0c1-e167f8c27335")
        self.assertEqual(bm2.name, "base")
        self.assertEqual(bm2.my_number, 4)
        self.assertIsInstance(bm2.created_at, datetime)
        self.assertIsInstance(bm2.updated_at, datetime)

    def test_str(self):
        """ Testing the  __str__ method of BaseModel """

        bm3 = BaseModel()
        string = bm3.__str__()
        self.assertIsInstance(string, str)

    def test_save(self):
        """ Testing save method of BaseModel """

        bm4 = BaseModel()
        self.assertTrue(hasattr(bm4, 'updated_at'))
        old_updated = bm4.updated_at
        bm4.save()
        self.assertTrue(hasattr(bm4, 'updated_at'))
        self.assertNotEqual(old_updated, bm4.updated_at)

    def test_to_dict(self):
        """ Testing to_dict method of BaseModel """

        bm5 = BaseModel()
        b_dict = bm5.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertIn("id", b_dict)
        self.assertIn("created_at", b_dict)
        self.assertIn("updated_at", b_dict)
        self.assertIn("__class__", b_dict)


if __name__ == '__main__':
    unittest.main()
