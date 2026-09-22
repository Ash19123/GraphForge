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


def test_add_vertex():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addVertex("A")

        assert graph.vertex_count() == 1


def test_add_multiple_vertices():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")

        assert graph.vertex_count() == 3


def test_add_edge():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addEdge("A", "B")

        assert graph.hasEdge("A", "B")


def test_has_edge_false():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addEdge("A", "B")

        assert graph.hasEdge("A", "C") == False


def test_neighbours():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addEdge("A", "B")
        graph.addEdge("A", "C")

        neighbours = graph.neighbours("A")

        assert set(neighbours) == {"B", "C"}


def test_degree():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addEdge("A", "B")
        graph.addEdge("A", "C")

        assert graph.degree("A") == 2


def test_edges():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addEdge("A", "B")
        graph.addEdge("B", "C")

        assert graph.edge_count() == 2