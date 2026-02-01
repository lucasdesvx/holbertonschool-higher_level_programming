#!/usr/bin/python3
"""Module Square : définit une classe Square"""


class Square:
    """Classe Square qui définit un carré"""

    def __init__(self, size=0):
        """Initialisation du carré"""
        self.size = size

    @property
    def size(self):
        """Récupère la valeur de size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la valeur de size avec vérifications"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire actuelle du carré"""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère #"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
