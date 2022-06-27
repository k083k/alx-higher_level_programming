#!/usr/bin/python3
"""
Rectangle module
"""

class Rectangle:
    """
    class that defines a Rectangle
    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    Raises:
        TypeError: if width or height is not an integer
        ValueError: if width or height is less than zero
    """

    def __init__(self, width, height):
        """
        init method to construct a rectangle
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """
        width getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
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
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


