#!/usr/bin/python3
"""Test User"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest


class Testuser(unittest.TestCase):
    """
    Unittests for the User class.
    """

    def test_pep8_conformance_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """
        Tests if class is named correctly.
        """
        user1 = User()
        self.assertEqual(user1.__class__.__name__, "User")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        user1 = User()
        self.assertTrue(issubclass(user1.__class__, BaseModel))
