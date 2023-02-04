#!/usr/bin/python3
"""A function that appends on a txt file"""


def append_write(filename="", text=""):
    """appends to a file"""

    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
