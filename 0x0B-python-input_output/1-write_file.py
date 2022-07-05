#!/usr/bin/python3
"""
write file Module
"""


def write_file(filename="", text=""):
    """
    write file function
    Args:
        - filename(string): the given filename
        - text(string): the contents of the file
    """
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(text)
        return len(text)
