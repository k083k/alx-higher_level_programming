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
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value < 0:
            raise ValueError('<name must be greater than 0')
