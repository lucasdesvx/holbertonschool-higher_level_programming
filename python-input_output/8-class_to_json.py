#!/usr/bin/python3
"""Convert an object instance to a serializable dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__