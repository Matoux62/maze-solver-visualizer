class Solver:

    def __init__(self, grille):
        self.__grille = grille

        self.__solving_state = "pending"
        #Valeur possible : "pending" "running" "completed"
        self.__solving_method = None
        #Valeur possible : "dfs" "bfs" "a"

        self.__current_pile = None
        self.__current_file = None
        
        self.__result = None

    def get_result(self):
        return self.__result

    def reset(self):
        self.__solving_method = "pending"
        self.__solving_method = None
        self.__current_pile = None
        self.__current_file = None
        self.__result = None

    def dfs(self):
        if self.__solving_state != "pending":
            return False

        #Future gestion thread
        self.__solving_method = "dfs"
        self.__solving_state = "running"
        is_completed = False
        while(not is_completed):
            continue

        return True

    def bfs(self):
        if self.__solving_state != "pending":
            return False

        #Future gestion thread
        self.__solving_method = "bfs"
        self.__solving_state = "running"
        is_completed = False
        while(not is_completed):
            continue

        return True

    def a(self):
        if self.__solving_state != "pending":
            return False

        #Future gestion thread
        self.__solving_method = "a"
        self.__solving_state = "running"
        is_completed = False
        while(not is_completed):
            continue

        return True