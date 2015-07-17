class Dijkstra:
    def __init__(self, graph, start, target, f = lambda f : f.distance):
        self._graph = graph
        self._start = start
        self._target = target
        self._f = f

    @property
    def function(self):
        return self._f

    @function.setter
    def function(self, value):
        self._f = value

    def run(self):
        # Set all distances to infinite
        for vertex in self._graph:
            vertex.initialize()

        # Set the distance for the start node to zero
        self._start.distance = 0

        # Put tuple pair into the priority queue
        unexplored_queue = [self._start]

        while len(unexplored_queue):
            # Pops a vertex with the smallest distance
            current = self._smaller(unexplored_queue)
            current.explored = True

            for next in current.adjacent:
                if next.explored:
                    continue

                new_distance = current.distance + current.get_weight(next)

                if new_distance < next.distance:
                    next.distance = new_distance
                    next.previous = current
                    print('Updated:\n\tcurrent = %s\n\tnext = %s\n\tnew_distance = %s' % (current.get_id(), next.get_id(), next.distance))

                if not next.visited:
                    next.visited = True
                    unexplored_queue.append(next)

        path = [self._target.get_id()]
        self.shortest(self._target, path)
        print('The shortest path : %s' % (path[::-1]))

    def _smaller(self, queue):
        smaller = queue[0]
        for vertex in queue[1:]:
            if self.function(vertex) < self.function(smaller):
                smaller = vertex
        queue.remove(smaller)

        return smaller

    def shortest(self, v, path):
        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous, path)
        return
