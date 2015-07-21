from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0
        self._previous = None

    def __iter__(self):
        return iter(self.vertex_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vertex_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, vertex):
        if vertex in self.vertex_dict:
            return self.vertex_dict[vertex]
        else:
            return None

    def add_edge(self, edge):
        frm, to, cost = edge

        try:
            cost = int(cost)
        except ValueError:
            print('The edge cost isn\'t a numerical value')

        if frm not in self.vertex_dict:
            self.add_vertex(frm)
        if to not in self.vertex_dict:
            selt.add_vertex(to)

        self.vertex_dict[frm].add_neighbor(self.vertex_dict[to], cost)

    def add_heuristic(self, heuristic):
        frm, to, h = heuristic

        try:
            h = int(h)
        except ValueError:
            print('The heuristic value isn\'t a numerical value')

        if frm not in self.vertex_dict:
            self.add_vertex(frm)
        if to not in self.vertex_dict:
            self.add_vertex(to)

        self.vertex_dict[frm].add_heuristic(self.vertex_dict[to], h)

    def get_vertices(self):
        return self.vertex_dict.keys()

    def print_data(self):
        print('Graph data:')
        for v in self:
            for w in v.connections():
                vid = v.get_id()
                wid = w.get_id()
                print('(%s, %s, weight = %3d)' % (vid, wid, v.get_weight(w)))
            for h in v.heuristics():
                vid = v.get_id()
                hid = h.get_id()
                print('(%s, %s, heuris = %3d)' % (vid, hid, v.get_heuristic(h)))

    def build(self, vertices, edges, heuristics):
        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            self.add_edge(edge)

        for heuristic in heuristics:
            self.add_heuristic(heuristic)

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, value):
        self._previous = value
