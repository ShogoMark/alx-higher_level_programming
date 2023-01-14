#!/usr/bin/python3
"""Defines a function: add_integers"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        @a (int, float): operand 1
        @b (int, float): operand 2

    Raises:
        TypeError: if either a or b is not an int or float

    """
    if not isinstance (a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance (b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

