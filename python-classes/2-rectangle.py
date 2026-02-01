#!/usr/bin/python3
"""Définit une classe Rectangle"""


class Rectangle:
    """Représente un rectangle"""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire"""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
