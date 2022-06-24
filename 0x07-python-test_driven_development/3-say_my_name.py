#!/usr/bin/python3
"""
function that prints my First Name and Last Name
"""

def say_my_name(first_name, last_name=""):
    """
    function that prints full name.
    Args:
        first_name: string
        last_name: string
    Raises:
        TypeError:
            first_name must be a string
            last_name must be a string

    Returns:
        <first name> <last name>
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
