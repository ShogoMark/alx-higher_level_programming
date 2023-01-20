#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Reads a text file"""

    with open(filename, "r",) as f:
        print(f.read())
