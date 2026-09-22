from .representations import (
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    IncidenceMatrixGraph
)


def list_to_matrix(graph):

    new_graph = AdjacencyMatrixGraph(graph.directed)

    for v in graph.adj:
        new_graph.addVertex(v)

    for u in graph.adj:

        for v in graph.adj[u]:
            new_graph.addEdge(u, v)

    return new_graph


def matrix_to_list(graph):

    new_graph = AdjacencyListGraph(graph.directed)

    for v in graph.vertices:
        new_graph.addVertex(v)

    for u, v in graph.edges():
        new_graph.addEdge(u, v)

    return new_graph


def list_to_incidence(graph):

    new_graph = IncidenceMatrixGraph(graph.directed)

    for v in graph.adj:
        new_graph.addVertex(v)

    for u, v in graph.edges():
        new_graph.addEdge(u, v)

    return new_graph


def incidence_to_list(graph):

    new_graph = AdjacencyListGraph(graph.directed)

    for v in graph.vertices:
        new_graph.addVertex(v)

    for u, v in graph.edge_list:
        new_graph.addEdge(u, v)

    return new_graph


def matrix_to_incidence(graph):

    new_graph = IncidenceMatrixGraph(graph.directed)

    for v in graph.vertices:
        new_graph.addVertex(v)

    for u, v in graph.edges():
        new_graph.addEdge(u, v)

    return new_graph


def incidence_to_matrix(graph):

    new_graph = AdjacencyMatrixGraph(graph.directed)

    for v in graph.vertices:
        new_graph.addVertex(v)

    for u, v in graph.edge_list:
        new_graph.addEdge(u, v)

    return new_graph