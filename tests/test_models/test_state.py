#!/usr/bin/python3
"""
    All the test for the state model are implemented here.
"""
import datetime
import time
from models.state import state
import models
import unittest
import os
class Teststate(unittest.TestCase):
    """Test the State class"""

    def test_state_inheritance(self):
            """
                tests that the state class Inherits from BaseModel
            """
            new_state = state()
            self.assertIsInstance(new_state, BaseModel())

    def test_state_attrributes(self):
        """
            tests that the state attributes exists
        """

        new_state = state()
        self.assertTrue("email" in new_state.__dir__())
        self.assertTrue("first_name" in new_state.__dir__())
        self.assertTrue("last_name" in new_state.__dir__())
        self.assertTrue("password" in new_state.__dir__())

    def test_type_name(self):
            """
                Test the type of name
            """
            new = state()
            name = getattr(new, "name")
            self.assertIsInstance(name, str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = state()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = state()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "state")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        state = state()
        string = "[state] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

    if __name__ == "__main__":
        unittest.main()


