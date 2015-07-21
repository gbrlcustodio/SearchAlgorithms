from dijkstra import Dijkstra

class AStar:
    def __init__(self, graph, start, target):
        self._dijkstra = Dijkstra(graph, start, target, lambda f : f.distance + f.get_heuristic(target))
        self._comparison = 0
        self._moviments = 0

    @property
    def comparison(self):
        return self._comparison

    @property
    def moviments(self):
        return self._moviments

    def run(self):
        self._dijkstra.run()
        self._comparison = self._dijkstra.comparison
        self._moviments = self._dijkstra.moviments
