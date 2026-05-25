#!/usr/bin/env python3

"""Module that contains the write_file function"""


from fileinput import filename
from pydoc import text


def write_file(filename="", text=""):

    """Writes a string to a text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)