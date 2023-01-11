#!/usr/bin/python3
"""Writes a string to a text file and returns
 number of characters"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file(UTF-8)
    and returns the number of character written

    Args:
        filename (str): name of the file
        text (str): text to be written to file
    Returns:
        The number of written characters
    """

    with open(filename, "w", encoding="utf-8") as file_name:
        return file_name.write(text)
