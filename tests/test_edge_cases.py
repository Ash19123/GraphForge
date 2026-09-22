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


# =========================================================
# EMPTY GRAPH
# =========================================================

def test_empty_graph():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        assert graph.vertex_count() == 0
        assert graph.edge_count() == 0


# =========================================================
# SINGLE VERTEX
# =========================================================

def test_single_vertex():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addVertex("A")

        assert graph.vertex_count() == 1
        assert graph.degree("A") == 0


# =========================================================
# DUPLICATE VERTEX
# =========================================================

def test_duplicate_vertex():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addVertex("A")
        graph.addVertex("A")

        assert graph.vertex_count() == 1


# =========================================================
# DUPLICATE EDGE
# =========================================================

def test_duplicate_edge():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addEdge("A", "B")
        graph.addEdge("A", "B")

        assert graph.edge_count() == 1


# =========================================================
# NON EXISTING EDGE
# =========================================================

def test_non_existing_edge():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addEdge("A", "B")

        assert graph.hasEdge("A", "C") == False


# =========================================================
# NON EXISTING VERTEX
# =========================================================

def test_non_existing_vertex():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addVertex("A")

        assert graph.neighbours("B") == []
        assert graph.degree("B") == 0


# =========================================================
# GRAPH WITH NO EDGES
# =========================================================

def test_no_edges():

    for GraphClass in GRAPH_CLASSES:

        graph = GraphClass()

        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")

        assert graph.edge_count() == 0