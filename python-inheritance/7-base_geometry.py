#!/usr/bin/python3
"""Module pour BaseGeometry."""


class BaseGeometry:
    """Classe BaseGeometry."""

    def area(self):
        """Lève une exception d'implémentation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide si value est un entier positif."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
