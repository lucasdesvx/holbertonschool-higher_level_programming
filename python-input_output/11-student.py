#!/usr/bin/python3
"""Define a Student class that can be serialized and reloaded."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return all attributes or only the requested attributes."""
        if isinstance(attrs, list):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the student's attributes with values from a dictionary."""
        self.__dict__.update(json)