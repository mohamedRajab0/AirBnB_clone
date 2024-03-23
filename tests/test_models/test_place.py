#!/usr/bin/python3
"""
    All the test for the place model are implemented here.
"""
import datetime
import time
from models.place import place
import models
import unittest
import os

class Testplace(unittest.TestCase):
    """Test the place class"""
    def test_place_inheritance(self):
            """
                tests that the place class Inherits from BaseModel
            """
            new_place = Place()
            self.assertIsInstance(new_place, BaseModel())

    def test_place_attrributes(self):
        """
            tests that the place attributes exists
        """

        new_place = Place()
        self.assertTrue("email" in new_place.__dir__())
        self.assertTrue("first_name" in new_place.__dir__())
        self.assertTrue("last_name" in new_place.__dir__())
        self.assertTrue("password" in new_place.__dir__())

    def test_type_email(self):
            """
                Test the type of name
            """
            new = Place()
            name = getattr(new, "email")
            self.assertIsInstance(name, str)

    def test_type_first_name(self):
        """
            Test the type of name
        """
        new = Place()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        """
        Test the type of last_name
        """
        new = Place()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        """
            Test the type of password
        """
        new = Place()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Place()
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
        u = Place()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        place = place()
        string = "[Place] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    if __name__ == "__main__":
        unittest.main()


