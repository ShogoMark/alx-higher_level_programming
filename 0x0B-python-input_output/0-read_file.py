#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Reads a text file"""
    doc = input("")
    with open(doc) as f:
        for line in f:
            file = f.read()
    print(file)
