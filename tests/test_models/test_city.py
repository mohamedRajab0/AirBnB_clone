#!/usr/bin/python3
"""
    All the test for the city model are implemented here.
"""
from models.city import city
import models
import unittest

class Testcity(unittest.TestCase):
    """Test the city class"""
    def test_city_inheritance(self):
            """
                tests that the city class Inherits from BaseModel
            """
            new_city = City()
            self.assertIsInstance(new_city, BaseModel())

    def test_city_attrributes(self):
        """
            tests that the city attributes exists
        """

        new_city = City()
        self.assertTrue("name" in new_city.__dir__())
        self.assertTrue("state_id" in new_city.__dir__())


    def test_type_name(self):
            """
                Test the type of name
            """
            new = City()
            name = getattr(new, "name")
            self.assertIsInstance(name, str)

    def test_type_state_id(self):
        """
            Test the type of name
        """
        new = City()
        name = getattr(new, "state_id")
        self.assertIsInstance(name, str)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = City()
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
        u = City()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "city")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

    if __name__ == "__main__":
        unittest.main()


