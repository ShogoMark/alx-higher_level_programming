#!/usr/bin/python3
"""A function that creates object from JSON file"""

import json


def load_from_json_file(filename):
    """create object from a JSON file"""

    with open(filename, encoding='utf=8'):
        obj = json.loads(filename)

    return obj
