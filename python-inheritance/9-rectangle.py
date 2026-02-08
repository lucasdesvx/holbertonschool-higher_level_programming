#!/usr/bin/python3
"""Module pour la classe Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle héritant de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise et valide width et height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calcule l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Représentation informelle du rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
