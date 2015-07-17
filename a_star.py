from dijkstra import Dijkstra

class AStar:
    def __init__(self, graph, start, target):
        Dijkstra(graph, start, target, lambda f : f.distance + f.get_heuristic(target)).run()
