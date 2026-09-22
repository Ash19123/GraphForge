from src.representations import (
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    IncidenceMatrixGraph
)

from src.algorithms import (
    bfs,
    connected_components
)


GRAPH_CLASSES = [
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    IncidenceMatrixGraph
]


def make_graph(GraphClass):

    graph = GraphClass(False)

    graph.addEdge("A", "B")
    graph.addEdge("A", "C")
    graph.addEdge("B", "D")

    return graph


# =========================================================
# BFS
# =========================================================

def test_bfs():

    for GraphClass in GRAPH_CLASSES:

        graph = make_graph(GraphClass)

        result = bfs(graph, "A")

        assert result[0] == "A"
        assert set(result) == {"A", "B", "C", "D"}


def test_bfs_single_vertex():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addVertex("A")

        result = bfs(graph, "A")

        assert result == ["A"]


# =========================================================
# CONNECTED COMPONENTS
# =========================================================

def test_one_connected_component():

    for GraphClass in GRAPH_CLASSES:

        graph = make_graph(GraphClass)

        components = connected_components(graph)

        assert len(components) == 1


def test_two_connected_components():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass(False)

        graph.addEdge("A", "B")
        graph.addEdge("C", "D")

        components = connected_components(graph)

        assert len(components) == 2


def test_three_components():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass(False)

        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")

        components = connected_components(graph)

        assert len(components) == 3