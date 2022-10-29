#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    a user class attribute with empty strings
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
