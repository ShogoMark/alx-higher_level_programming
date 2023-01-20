#!/usr/bin/python3
"""retrieves a dictionary representation of a Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """instantiates the class attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        records = list(set(self).intersection(attrs))
        newlist = [attrs[i] for i in records]
        print(str(newlist))
