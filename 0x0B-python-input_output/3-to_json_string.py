#!/usr/bin/python3
"""Contains function that returns JSON rep of an obj"""

import json


def to_json_string(my_obj):
    """returns JSON format of object"""

    return json.dumps(my_obj)
