from graphs import DirectedGraph


def topo_sort_kahn(graph):
    in_degrees = [0] * graph.size
    topo_sort = []
    queue = []
    visited = 0
    for i in graph.map:
        outgoing_edges = graph.map[i]
        for v in outgoing_edges:
            in_degrees[v] += 1
    for index, d in enumerate(in_degrees):
        if d == 0:
            queue.append(index)

    while queue:
        current = queue.pop(0)
        topo_sort.append(current)
        outgoing_edges = graph.map[current]
        for v in outgoing_edges:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                queue.append(v)

    print(topo_sort)


g = DirectedGraph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

topo_sort_kahn(g)
