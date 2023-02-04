#!/usr/bin/python3
"""Contains function that returns obj in JSON format"""

import json


def from_json_string(my_str):
    """returns objects as JSON format"""

    return json.loads(my_str)
