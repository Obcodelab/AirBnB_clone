#!/usr/bin/python3
""" Testing the State class """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class """

    def test_instance(self):
        """ Testing instance of State class """

        state = State()
        self.assertIsInstance(state, State)

    def test_attr(self):
        """Testing the attributes of State class """

        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertIsInstance(state.name, str)

    def test_inheritance(self):
        """Testing inheritance of State class """

        state1 = State()
        self.assertIsInstance(state1, BaseModel)
        self.assertTrue(hasattr(state1, "id"))
        self.assertTrue(hasattr(state1, "created_at"))
        self.assertTrue(hasattr(state1, "updated_at"))

    def test_str(self):
        """Testing  __str__ method of State class """

        state2 = State()
        string = state2.__str__()
        self.assertIsInstance(string, str)

    def test_save(self):
        """ Testing save method of State class """

        state3 = State()
        self.assertTrue(hasattr(state3, 'updated_at'))
        old_updated = state3.updated_at
        state3.save()
        self.assertTrue(hasattr(state3, 'updated_at'))
        self.assertNotEqual(old_updated, state3.updated_at)

    def test_to_dict(self):
        """Testing to_dict method of State class """

        state4 = State()
        state4.name = "Texas"
        s_dict = state4.to_dict()

        self.assertIsInstance(s_dict, dict)
        self.assertIn("id", s_dict)
        self.assertIn("created_at", s_dict)
        self.assertIn("updated_at", s_dict)
        self.assertIn("__class__", s_dict)

        self.assertEqual(s_dict["name"], "Texas")
        self.assertEqual(s_dict["__class__"], "State")


if __name__ == '__main__':
    unittest.main()
