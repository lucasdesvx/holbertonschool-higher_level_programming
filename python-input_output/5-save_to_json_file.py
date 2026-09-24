#!/usr/bin/python3
"""Save a Python object to a file using JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)