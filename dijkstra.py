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
        unvisited_queue = [(vertex.distance, vertex) for vertex in self._graph]
        heapq.heapify(unvisited_queue)

        while len(unvisited_queue):
            # Pops a vertex with the smallest distance
            unvisited = heapq.heappop(unvisited_queue)
            current = unvisited[1]
            current.visited = True

            for next in current.adjacent:
                if next.visited:
                    continue

                new_distance = current.distance + current.get_weight(next)

                if new_distance < next.distance:
                    next.distance = new_distance
                    next.previous = current
                    print('Updated:\n\tcurrent = %s\n\tnext = %s\n\tnew_distance = %s' % (current.get_id, next.get_id, next.distance))

            # Rebuild heap
            # Pop the first element
            while len(unvisited_queue):
                heapq.heappop(unvisited_queue)

            # Put all not visited vertices into the queue
            unvisited_queue = [(vertex.distance, vertex) for vertex in self._graph if not vertex.visited]
            heapq.heapify(unvisited_queue)
