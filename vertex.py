import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self._adjacent = {}
        self._heuristic = {}
        self.initialize()

    def initialize(self):
        # Set distance to infinity to all nodes
        self._distance = sys.maxsize
        # Mark all nodes unexplored
        self._explored = False
        # Mark all nodes unvisited
        self._visited = False
        # Predecessor
        self._previous = None

    def add_neighbor(self, neighbor, weigth = 0):
        self._adjacent[neighbor] = weigth

    def connections(self):
        return self._adjacent.keys()

    def get_weight(self, neighbor):
        return self._adjacent[neighbor]

    def add_heuristic(self, target, value):
        self._heuristic[target] = value

    def heuristics(self):
        return self._heuristic.keys()

    def get_heuristic(self, target):
        return self._heuristic[target] if target in self._heuristic else sys.maxsize

    @property
    def adjacent(self):
        return self._adjacent

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value):
        self._visited = value

    @property
    def explored(self):
        return self._explored

    @explored.setter
    def explored(self, value):
        self._explored = value

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, value):
        self._previous = value

    def get_id(self):
        return self.id

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self._adjacent])
