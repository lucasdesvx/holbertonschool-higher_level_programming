#!/usr/bin/python3
"""Module pour la classe Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Représente un rectangle héritant de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise le rectangle avec validation.

        Args:
            width (int): Largeur du rectangle.
            height (int): Hauteur du rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
