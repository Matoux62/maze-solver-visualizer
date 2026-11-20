class Pile:
    def __init__(self):
        self.__elements = []

    def est_vide(self):
        return len(self.__elements) == 0

    def empiler(self, x):
        self.__elements.append(x)

    def depiler(self):
        return self.__elements.pop()

    def sommet(self):
        return self.__elements[-1]

class File:

    def __init__(self):
        self.__elements = []

    def est_vide(self):
        return len(self.__elements) == 0

    def enfiler(self, x):
        self.__elements.append(x)

    def defiler(self):
        return self.__elements.pop(0)

    def sommet(self):
        return self.__elements[0]


class Maillon:
    def __init__(self, val, suiv=None):
        self.__val = val
        self.__suiv = suiv

class ListeChainee:
    def __init__(self):
        self.__tete = None
        