class Labyrinthe:

    def __init__(self, grille : list[list[str]]):
        if not (isinstance(grille, list) and
                len(grille) > 0 and 
                all(isinstance(ligne, list) and 
                len(ligne) > 0 for ligne in grille)):
            raise TypeError("Labyrinthe() argument grille is of type list[list[str]]")
        length = len(grille[0])
        if any(len(ligne) != length for ligne in grille):
            raise ValueError("Labyrinthe() elements of argument grille need be all the same size")
            
        self.__grille   = grille
        self.__nb_ligne = len(grille)
        self.__nb_col   = len(grille[0])
        self.__entree   = None
        self.__sortie   = None

        for i, ligne in enumerate(self.__grille):
            for j, case in enumerate(ligne):
                if case == 'S':
                    self.__entree = (i, j)
                elif case == 'E':
                    self.__sortie = (i, j)

    def trouve_entree(self):
        return self.__entree

    def trouve_sortie(self):
        return self.__sortie

    def afficher_labyrinthe(self):
        for ligne in self.__grille:
            ligne_to_print = ""
            for case in ligne:
                if case == ' ':
                    ligne_to_print += '.' + ' '
                else:
                    ligne_to_print += case + ' '
            print(ligne_to_print)

    def est_valide(self, i, j):
        return (0 <= i < self.__nb_ligne) and (0 <= j < self.__nb_col) and (self.__grille[i][j] != '#')

                