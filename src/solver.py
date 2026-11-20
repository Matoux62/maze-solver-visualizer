from enum import Enum, auto
from structures import *

class SolvingState(Enum):
    IDLE = auto()
    RUNNING = auto()
    COMPLETED = auto()
    IMPOSSIBLE = auto()

class SolvingMethod(Enum):
    DFS = auto()
    BFS = auto()
    A_STAR = auto()

class Solver:

    def __init__(self, labyrinthe):
        self.__labyrinthe = labyrinthe

        self.__solving_state = SolvingState.IDLE
        self.__solving_method = None

        self.__current_pile = Pile()
        self.__current_file = File()
        self.__visited = []
        
        self.__result = None

    def get_result(self):
        return self.__result

    def reset(self):
        self.__solving_state = SolvingState.IDLE
        self.__solving_method = None
        self.__current_pile = None
        self.__current_file = None
        self.__result = None
        self.__visited = []

    def dfs(self):
        if self.__solving_state != SolvingState.IDLE:
            return False

        #Future gestion thread
        self.__solving_method = SolvingMethod.DFS
        self.__solving_state = SolvingState.RUNNING

        entree = self.__labyrinthe.trouve_entree()
        sortie = self.__labyrinthe.trouve_sortie()
        self.__current_pile.empiler(entree)

        while not self.__current_pile.est_vide():
            flag = False
            case = self.__current_pile.sommet()
            self.__visited.append(case)
            if case == sortie:
                self.__result = self.__current_pile.format_tab()
                break
            for voisin in self.__labyrinthe.voisins(case[0], case[1]):
                if voisin not in self.__visited:
                    self.__current_pile.empiler(voisin)
                    flag = True
                    break
            if not flag:
                self.__current_pile.depiler()

        if self.__current_pile.format_tab() == []:
            self.__result = SolvingState.IMPOSSIBLE
            
        self.__solving_state = SolvingState.COMPLETED

        return True

    def bfs(self):
        if self.__solving_state != SolvingState.IDLE:
            return False

        #Future gestion thread
        self.__solving_method = SolvingMethod.BFS
        self.__solving_state = SolvingState.RUNNING
        is_completed = False
        while(not is_completed):
            continue

        return True

    def a(self):
        if self.__solving_state != SolvingState.IDLE:
            return False

        #Future gestion thread
        self.__solving_method = SolvingMethod.A_STAR
        self.__solving_state = SolvingState.RUNNING
        is_completed = False
        while(not is_completed):
            continue

        return True