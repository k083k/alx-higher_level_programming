#!/usr/bin/python3
""" Base Module """
import json
import csv
import turtle


class Base:
    """
    base class to manage ID
    Attributes:
        id: int, Id of a Base object
    """
    __nr_objects = 0

    def __init__(self, id=None):
        """ Instantiation """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ serializes a list of dicts representing shapes """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """deserializes a json list represented as a string"""
        if json_string is None or json_string == "" or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objects to a json file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            temp_list = []
            if list_objs is not None:
                temp_list = [o.to_dictionary() for o in list_objs]
            f.write(cls.to_json_string(temp_list))

    @classmethod
    def create(cls, **dictionary):
        """creates an instances with all attributes set"""
        new = cls.__new__(cls)
        if cls.__name__ == "Rectangle":
            new.__init__(10, 10)
        if cls.__name__ == "Square":
            new.__init__(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """retrives a list of instances from a json file"""
        filename = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(filename, "r") as f:
                content = cls.from_json_string(f.read())
            for dict in content:
                instances.append(cls.create(**dict))
            return instances
        except FileNotFoundError:
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of objects to a csv file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as f:
            if list_objs is not None or list_objs != []:
                field_names = [key for key in list_objs[0].to_dictionary()]
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """retrives a list of instances from a csv file"""
        filename = "{}.csv".format(cls.__name__)
        instances = []
        try:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        for k in row:
                            row[k] = int(row[k])
                    except:
                        pass
                    instances.append(cls.create(**row))
            return instances
        except FileNotFoundError:
            return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws given rectangles and squares using the turtle module"""
        T = turtle.Turtle()
        T.speed(2)
        if list_rectangles is not None or list_rectangles != []:
            for rect in list_rectangles:
                temp = rect.to_dictionary()
                T.penup()
                T.goto((temp["x"], temp["y"]))
                T.pendown()
                for i in range(2):
                    T.forward(temp["width"])
                    T.right(90)
                    T.forward(temp["height"])
                    T.right(90)
        if list_squares is not None or list_squares != []:
            for square in list_squares:
                temp = square.to_dictionary()
                T.goto(temp["x"], temp["y"])
                for i in range(2):
                    T.forward(temp["size"])
                    T.right(90)
