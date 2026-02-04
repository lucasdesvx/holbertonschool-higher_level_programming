#!/usr/bin/python3
"""
Ce module définit la classe MyList qui hérite de la classe intégrée list.
"""


class MyList(list):
    """
    Classe enfant de list avec des fonctionnalités de tri supplémentaires.
    """

    def print_sorted(self):
        """
        Affiche la liste triée par ordre croissant sans modifier
        la liste d'origine.
        """
        print(sorted(self))
