#!/usr/bin/python3

"""User class that implements the BaseModel"""
from base_model import BaseModel


class User(BaseModel):

    """
    The User class that inherits from BaseModel

    Public class attributes:
        email : string - empty string
        password : string - empty string
        first_name : string - empty string
        last_name : string - empty string
    """

    email = ""
    passsword = ""
    first_name = ""
    last_name = ""
