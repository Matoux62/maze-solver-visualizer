class Labyrinthe:

    def __init__(self, grille : list[list[str]]):

        self.__entree   = None
        self.__sortie   = None

        if not self.__test_grille_valide(grille):
            return
            
        self.__grille   = grille
        self.__nb_ligne = len(grille)
        self.__nb_col   = len(grille[0])

    def __test_grille_valide(self, grille):
        if not (isinstance(grille, list) and
                len(grille) > 0 and 
                all(isinstance(ligne, list) and 
                len(ligne) > 0 for ligne in grille)):
            raise TypeError("Labyrinthe() argument grille is of type list[list[str]]")
            return False

        length = len(grille[0])
        if any(len(ligne) != length for ligne in grille):
            raise ValueError("Labyrinthe() elements of argument grille need be all the same size")
            return False

        if not self.__cherche_entree_sortie(grille):
            raise ValueError("Labyrinthe() argument grille need to contain a start('S') and an exit('E')")

        return True

    def __cherche_entree_sortie(self, grille):
        for i, ligne in enumerate(grille):
            for j, case in enumerate(ligne):
                if case == 'S':
                    if self.__entree :
                        raise ValueError("Labyrinthe() argument grille cant contain more than one start('S') and one exit('E')")
                    self.__entree = (i, j)
                elif case == 'E':
                    if self.__sortie :
                        raise ValueError("Labyrinthe() argument grille cant contain more than one start('S') and one exit('E')")
                    self.__sortie = (i, j)
        return self.__sortie and self.__entree
        

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

                