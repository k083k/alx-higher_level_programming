#!/usr/bin/python3
"""
base_geometry module
"""


class BaseGeometry:
    """
    BaseGeometry Class
    """

    def area(self):
        """
        Raises Exception with the message
        'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
            - checks if value is an integer(Raises TypeError otherwise)
            - cheack if value is positive(Raises ValueError otherwise)
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
