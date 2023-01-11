#!/usr/bin/python3
"""Returns a python object represented by a JSON string"""

import json


def from_json_string(my_str):
    """Returns an object from the JSON representation

    Args:
        my_str (JSON string)
    Returns:
        Python object"""

    return json.loads(my_str)
