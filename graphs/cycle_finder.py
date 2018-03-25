from graphs import Graph


def is_cycle_undirected(graph):
    visited = [False] * graph.size
    for i in range(graph.size):
        if not visited[i]:
            if _unicycle_util(graph, i, visited, -1):
                return True
    return False


def _unicycle_util(graph, current, visited, parent):
    neighbours = graph.map[current]
    visited[current] = True
    for neighbour in neighbours:
        if not visited[neighbour]:
            if _unicycle_util(graph, neighbour, visited, current):
                return True
        elif parent != neighbour:
            return True

    return False

g = Graph(3)
g.add_edge(1, 0)
g.add_edge(0, 2)

print(is_cycle_undirected(g))
