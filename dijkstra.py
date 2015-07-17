import heapq

class Dijkstra:
    def __init__(self, graph, start, target):
        self._graph = graph
        self._start = start
        self._target = target

    def run(self):
        print('Dijkstra\'s shortest path')
        # Set the distance for the start node to zero
        self._start.distance = 0

        # Put tuple pair into the priority queue
        unexplored_queue = [self._start]
        heapq.heapify(unexplored_queue)

        while len(unexplored_queue):
            # Pops a vertex with the smallest distance
            current = heapq.heappop(unexplored_queue)
            current.explored = True

            for next in current.adjacent:
                if next.explored:
                    continue

                new_distance = current.distance + current.get_weight(next)

                if new_distance < next.distance:
                    next.distance = new_distance
                    next.previous = current
                    heapq.heapify(unexplored_queue) # Update priority queue
                    print('Updated:\n\tcurrent = %s\n\tnext = %s\n\tnew_distance = %s' % (current.get_id(), next.get_id(), next.distance))

                if not next.visited:
                    next.visited = True
                    heapq.heappush(unexplored_queue, next)

        path = [self._target.get_id()]
        self.shortest(self._target, path)
        print('The shortest path : %s' % (path[::-1]))

    def shortest(self, v, path):
        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous, path)
        return
