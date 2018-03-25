from graphs import Graph


def DFS(graph, source, visited):
    visited[source] = True
    print(source)
    neighbours = graph.map[source]
    for i in neighbours:
        if not visited[i]:
            DFS(graph, i, visited)

# Doesn't work for disjoint graphs, call DFS on all nodes to achieve that

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

visited = [False] * len(g.map)
DFS(g, 2, visited)
