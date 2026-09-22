from src.representations import (
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    IncidenceMatrixGraph
)


GRAPH_CLASSES = [
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    IncidenceMatrixGraph
]


def test_undirected_graph():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass(False)

        graph.addEdge("A", "B")

        assert graph.hasEdge("A", "B")
        assert graph.hasEdge("B", "A")


def test_directed_graph():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass(True)

        graph.addEdge("A", "B")

        assert graph.hasEdge("A", "B")
        assert graph.hasEdge("B", "A") == False


def test_undirected_degree():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass(False)

        graph.addEdge("A", "B")
        graph.addEdge("A", "C")

        assert graph.degree("A") == 2


def test_directed_degree():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass(True)

        graph.addEdge("A", "B")
        graph.addEdge("A", "C")

        assert graph.degree("A") == 2