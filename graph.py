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
        self.vertex_dict[to].add_neighbor(self.vertex_dict[frm], cost)

    def get_vertices(self):
        return self.vertex_dict.keys()

    def print_data(self):
        print('Graph data:')
        for v in self:
            for w in v.connections():
                vid = v.get_id()
                wid = w.get_id()
                print('(%s, %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, value):
        self._previous = value
