#!/usr/bin/python3
"""
function that prints a square with the # character
"""

def print_square(size):
    """
    function that prints squares with the '#' character
    Args:
        size: size of the square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer
    Returns:
        a square with hashes
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise valueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print('#', end="")
        print()

