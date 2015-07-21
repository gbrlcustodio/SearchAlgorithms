class Dijkstra:
    def __init__(self, graph, start, target, f = lambda f : f.distance):
        self._graph = graph
        self._start = start
        self._target = target
        self._f = f
        self._comparison = 0
        self._moviments = 0

    @property
    def function(self):
        return self._f

    @function.setter
    def function(self, value):
        self._f = value

    @property
    def comparison(self):
        return self._comparison

    @property
    def moviments(self):
        return self._moviments

    def run(self):
        self._comparison = 0
        self._moviments = 0

        # Set all distances to infinite
        for vertex in self._graph:
            self._comparison += 1
            self._moviments += 4
            vertex.initialize()

        self._comparison += 1

        # Set the distance for the start node to zero
        self._start.distance = 0
        self._moviments += 1

        # Put tuple pair into the priority queue
        unexplored_queue = [self._start]
        self._moviments += 1

        while len(unexplored_queue):
            self._comparison += 1
            # Pops a vertex with the smallest distance
            current = self._smaller(unexplored_queue)
            current.explored = True
            self._moviments += 2

            for next in current.adjacent:
                self._comparison += 1

                if next.explored:
                    self._comparison += 1
                    continue

                new_distance = current.distance + current.get_weight(next)
                self._moviments += 1

                if new_distance < next.distance:
                    self._comparison += 1
                    next.distance = new_distance
                    next.previous = current
                    self._moviments += 2
                    print('Updated:\n\tcurrent = %s\n\tnext = %s\n\tnew_distance = %s' % (current.get_id(), next.get_id(), next.distance))

                if not next.visited:
                    self._comparison += 1
                    next.visited = True
                    unexplored_queue.append(next)
                    self._moviments += 2

            self._comparison += 1
        self._comparison += 1

        path = [self._target.get_id()]
        self.shortest(self._target, path)
        print('The shortest path : %s' % (path[::-1]))

    def _smaller(self, queue):
        smaller = queue[0]
        self._moviments += 1

        for vertex in queue[1:]:
            self._comparison += 2
            if self.function(vertex) < self.function(smaller):
                smaller = vertex
                self._moviments += 1

        self._comparison += 1

        queue.remove(smaller)
        self._moviments += 1

        return smaller

    def shortest(self, v, path):
        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous, path)
        return
