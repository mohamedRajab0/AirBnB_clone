#!/usr/bin/python3
"""
    All the test for the review model are implemented here.
"""
import datetime
import time
from models.review import review
import models
import unittest
import os

class Testreview(unittest.TestCase):
    """Test the review class"""
    def test_review_inheritance(self):
            """
                tests that the review class Inherits from BaseModel
            """
            new_review = review()
            self.assertIsInstance(new_review, BaseModel())

    def test_review_attrributes(self):
        """
            tests that the review attributes exists
        """

        new_review = review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())
        self.assertTrue("password" in new_review.__dir__())

    def test_type_place_id(self):
            """
                Test the type of name
            """
            new = review()
            name = getattr(new, "place_id")
            self.assertIsInstance(name, str)

    def test_type_user_id(self):
        """
            Test the type of name
        """
        new = review()
        name = getattr(new, "user_id")
        self.assertIsInstance(name, str)

    def test_type_text(self):
        """
        Test the type of text
        """
        new = review()
        name = getattr(new, "text")
        self.assertIsInstance(name, str)

    
        self.assertIsInstance(name, str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = review()
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
        u = review()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        review = review()
        string = "[review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

    if __name__ == "__main__":
        unittest.main()


