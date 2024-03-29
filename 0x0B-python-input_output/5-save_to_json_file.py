#!/usr/bin/python3
"""A function that writes an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """writes to a file in JSON format"""

    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(json.dumps(my_obj))
