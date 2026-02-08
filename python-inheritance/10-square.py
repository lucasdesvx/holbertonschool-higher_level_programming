#!/usr/bin/python3
"""Module pour la classe Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square héritant de Rectangle."""

    def __init__(self, size):
        """Initialise le carré avec size.

        Args:
            size (int): La taille du côté du carré.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcule l'aire du carré."""
        return self.__size ** 2
