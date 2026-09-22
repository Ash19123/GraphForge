from src.representations import (
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    IncidenceMatrixGraph
)


def create_graph(graph_class, directed=False):

    graph = graph_class(directed)

    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")

    graph.addEdge("A", "B")
    graph.addEdge("A", "C")
    graph.addEdge("B", "D")

    return graph


def create_disconnected_graph(graph_class):

    graph = graph_class(False)

    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")

    graph.addEdge("A", "B")
    graph.addEdge("C", "D")

    return graph