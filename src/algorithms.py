from collections import deque


def bfs(graph, start):

    if start not in get_vertices(graph):
        return []

    visited = set()
    queue = deque()
    result = []

    visited.add(start)
    queue.append(start)

    while queue:

        current = queue.popleft()

        result.append(current)

        for neighbour in graph.neighbours(current):

            if neighbour not in visited:

                visited.add(neighbour)
                queue.append(neighbour)

    return result


def connected_components(graph):

    vertices = get_vertices(graph)

    visited = set()
    components = []

    for vertex in vertices:

        if vertex not in visited:

            component = []

            queue = deque()

            queue.append(vertex)
            visited.add(vertex)

            while queue:

                current = queue.popleft()

                component.append(current)

                for neighbour in graph.neighbours(current):

                    if neighbour not in visited:

                        visited.add(neighbour)
                        queue.append(neighbour)

            components.append(component)

    return components


def get_vertices(graph):

    if hasattr(graph, "vertices"):
        return graph.vertices

    if hasattr(graph, "adj"):
        return list(graph.adj.keys())

    return []