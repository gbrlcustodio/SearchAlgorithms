class Dijkstra:
    def __init__(self, graph, start, target, f = lambda f : f.distance):
        self._graph = graph
        self._start = start
        self._target = target
        self._f = f
        self._comparison = 0
        self._moviments = 0
        self._iterations = 0

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

    @property
    def iterations(self):
        return self._iterations

    def run(self):
        self._comparison = 0
        self._moviments = 0
        self._iterations = 0

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
            self._iterations += 1
            # Pops a vertex with the smallest distance
            current = self._smaller(unexplored_queue)
            current.explored = True
            self._moviments += 2

            if current == self._target:
                break

            for next in current.adjacent:
                self._comparison += 2

                if next.explored:
                    continue

                new_distance = current.distance + current.get_weight(next)
                self._moviments += 1

                self._comparison += 1
                if new_distance < next.distance:
                    next.distance = new_distance
                    next.previous = current
                    self._moviments += 2
                    #print('Updated:\n\tcurrent = %s\n\tnext = %s\n\tnew_distance = %s' % (current.get_id(), next.get_id(), next.distance))

                self._comparison += 1
                if not next.visited:
                    next.visited = True
                    unexplored_queue.append(next)
                    self._moviments += 2

            self._comparison += 1
        self._comparison += 1
        self.shortest()

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

        #print('%s: %d' % (smaller.get_id(), self.function(smaller)))

        return smaller

    def shortest(self):
        if self._target != self._start and self._target.previous is None:
            print('There is no path to %s, from %s.' % (self._target, self._start))
            return

        path = [self._target.get_id()]
        self._shortest(self._target, path)
        print('The shortest path : %s' % (path[::-1]))

    def _shortest(self, v, path):
        if v.previous:
            path.append(v.previous.get_id())
            self._shortest(v.previous, path)
        return
