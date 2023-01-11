#!/usr/bin/python3
"""Creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename: name of file to be written"""

    with open(filename) as file_name:
        return json.load(file_name)
