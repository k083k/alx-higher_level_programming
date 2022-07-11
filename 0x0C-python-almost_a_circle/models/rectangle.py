#!/usr/bin/python3
"""Contains Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class to represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width property getter"""
        return self.__width

    @property
    def height(self):
        """height property getter"""
        return self.__height

    @property
    def x(self):
        """x property getter"""
        return self.__x

    @property
    def y(self):
        """y property getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """width property setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height property setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x property setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y property setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays rectangle using # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for z in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """formatted output"""
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                    self.__y, self.__width,
                                                    self.__height)
        return s

    def update(self, *args, **kwargs):
        """updates a rectanlge with new properties"""
        attrs = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) != 0:
            i = 0
            while i < len(attrs) and i < len(args):
                setattr(self, attrs[i], args[i])
                i += 1
        else:
            for attr in attrs:
                if attr in kwargs.keys():
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """represents a rectangle as a dict"""
        rect_dict = {}
        attrs = ["id", "width", "height", "x", "y"]
        for attr in attrs:
            rect_dict.update({attr: getattr(self, attr)})
        return rect_dict
