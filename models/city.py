#!/usr/bin/python3

"""City class that implements the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):

    """
    The City class that inherits from BaseModel

    Public class attributes:
        name : string - empty string
        state_id: string - empty string: it will be the State.id
    """

    name = ""
    state_id = ""
