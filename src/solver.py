from enum import Enum, auto
from structures import *

class SolvingState(Enum):
    IDLE = auto()
    RUNNING = auto()
    COMPLETED = auto()

class SolvingMethod(Enum):
    DFS = auto()
    BFS = auto()
    A_STAR = auto()

class Solver:

    def __init__(self, grille):
        self.__grille = grille

        self.__solving_state = SolvingState.IDLE
        self.__solving_method = None

        self.__current_pile = Pile()
        self.__current_file = File()
        
        self.__result = None

    def get_result(self):
        return self.__result

    def reset(self):
        self.__solving_state = SolvingState.IDLE
        self.__solving_method = None
        self.__current_pile = None
        self.__current_file = None
        self.__result = None

    def dfs(self):
        if self.__solving_state != SolvingState.IDLE:
            return False

        #Future gestion thread
        self.__solving_method = SolvingMethod.DFS
        self.__solving_state = SolvingState.RUNNING
        is_completed = False
        while(not is_completed):
            continue

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