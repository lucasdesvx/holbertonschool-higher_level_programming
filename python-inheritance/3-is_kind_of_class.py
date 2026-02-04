#!/usr/bin/python3
"""
Module pour la fonction is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si l'objet est une instance de a_class ou d'une classe héritée
    """
    return isinstance(obj, a_class)
