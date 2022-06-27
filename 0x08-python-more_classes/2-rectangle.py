#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    defining a Rectangle class
    Args:
        width: width of the rectangle
        height: height of the rectangle
    Raises:
        TypeError: if width/height is not an integer
        ValueError: if width/height is < 0
    """
    def __init__(self, width=0, height=0):
        """
        init metho to construct rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        width getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width setter attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height setter attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """
        area finder
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        perimeter finder
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__height * 2) + (self.__width * 2))
