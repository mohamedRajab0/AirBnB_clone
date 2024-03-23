#!/usr/bin/python3
"""
    All the test for the amenity model are implemented here.
"""
from models.amenity import amenity
import models
import unittest

class Testamenity(unittest.TestCase):
    """Test the amenity class"""
    def test_amenity_inheritance(self):
            """
                tests that the amenity class Inherits from BaseModel
            """
            new_amenity = Amenity()
            self.assertIsInstance(new_amenity, BaseModel())

    def test_amenity_attrributes(self):
        """
            tests that the amenity attributes exists
        """

        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())


    def test_type_name(self):
            """
                Test the type of name
            """
            new = Amenity()
            name = getattr(new, "name")
            self.assertIsInstance(name, str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Amenity()
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
        u = Amenity()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    if __name__ == "__main__":
        unittest.main()


