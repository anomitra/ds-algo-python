from collections import defaultdict


class Graph(object):

    def __init__(self, nodes, directed=False):
        self.map = defaultdict(list)
        self.size = nodes
        self._directed = directed

    def add_edge(self, source, destination):
        self.map[source].append(destination)
        if not self._directed:
            self.map[source].append(source)


class DirectedGraph(Graph):
    def __init__(self, nodes):
        super().__init__(nodes)
        self._directed = True