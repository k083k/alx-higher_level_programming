#!/usr/bin/python3
"""
Rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    creates a class called Rectangle
    Private instance attributes
        - width
        - height
    Inherits from BaseGeometry
    """

    def _init__(self, width, height):
        """ Initializes an instance.

        Args:
            - width: width of the rectangle
            - height: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
