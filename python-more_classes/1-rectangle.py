#!/usr/bin/python3
"""Module pour la classe Rectangle."""


class Rectangle:
    """Définit un rectangle par sa largeur et sa hauteur."""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec validation."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur avec gestion d'erreurs."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur avec gestion d'erreurs."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
