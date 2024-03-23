#!/usr/bin/python3
"""
    All the test for the user model are implemented here.
"""
import datetime
import time
from models.user import User
import models
import unittest
import os

class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_User_inheritance(self):
            """
                tests that the User class Inherits from BaseModel
            """
            new_user = User()
            self.assertIsInstance(new_user, BaseModel())

    def test_User_attrributes(self):
        """
            tests that the User attributes exists
        """

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_type_email(self):
            """
                Test the type of name
            """
            new = User()
            name = getattr(new, "email")
            self.assertIsInstance(name, str)

    def test_type_first_name(self):
        """
            Test the type of name
        """
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        """
        Test the type of last_name
        """
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        """
            Test the type of password
        """
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
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
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    if __name__ == "__main__":
        unittest.main()


