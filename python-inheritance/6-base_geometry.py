#!/usr/bin/python3
"""
Module pour la classe BaseGeometry
"""


class BaseGeometry:
    """
    Classe BaseGeometry avec une méthode area
    """

    def area(self):
        """
        Lève une Exception car area n'est pas implémentée
        """
        raise Exception("area() is not implemented")
