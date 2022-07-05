#!/usr/bin/python3
"""
Append to file Module
"""


def append_write(filename="", text=""):
    """
    append to file Function
    Args:
        - filename(string): file name
        - text(string): content of file
    Returns:
    numbe rof characters added
    """
    with open(filename, 'a', encoding="UTF8") as f:
        f.append(text)
        return len(text)
