from graphs import Graph


def BFS(graph, source):
    visited = [False] * len(graph.map)
    queue = []
    queue.append(source)
    visited[source] = True

    while queue:
        current = queue.pop()
        print(current)

        for i in graph.map.get(current):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

BFS(g, 2)