#!/usr/bin/python3
"""Writes an object to a txt file using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file
    using JSON representation

    Arg:
        my_obj (object)
        filename (name of file to be created)"""

    with open(filename, "w") as file_name:
        json.dump(my_obj, file_name)
