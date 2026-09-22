import sys
import os
import time
import random
import tracemalloc

sys.path.append(os.path.abspath("."))

from src.representations import (
    AdjacencyListGraph,
    AdjacencyMatrixGraph,
    IncidenceMatrixGraph
)

from src.algorithms import bfs


# =========================================================
# GRAPH CREATION
# =========================================================

def create_sparse_graph(GraphClass, n=50000):

    graph = GraphClass(False)

    # Add vertices
    for i in range(n):
        graph.addVertex(i)

    # Create approximately average degree 4
    # Edges: (i, i+1) and (i, i+2)
    for i in range(n - 1):

        graph.addEdge(i, i + 1)

        if i + 2 < n:
            graph.addEdge(i, i + 2)

    return graph


def create_small_sparse_graph(GraphClass, n=2000):

    graph = GraphClass(False)

    for i in range(n):
        graph.addVertex(i)

    for i in range(n - 1):

        graph.addEdge(i, i + 1)

        if i + 2 < n:
            graph.addEdge(i, i + 2)

    return graph


def create_dense_bipartite_graph(GraphClass):

    graph = GraphClass(False)

    users = 1000
    items = 1000

    # Add vertices
    for i in range(users):
        graph.addVertex("U" + str(i))

    for i in range(items):
        graph.addVertex("I" + str(i))

    # Use a fixed seed so results are reproducible
    random.seed(42)

    for i in range(users):

        for j in range(items):

            if random.random() < 0.40:

                graph.addEdge(
                    "U" + str(i),
                    "I" + str(j)
                )

    return graph


# =========================================================
# MEASUREMENTS
# =========================================================

def measure_construction(GraphClass, create_function):

    start = time.perf_counter()

    graph = create_function(GraphClass)

    end = time.perf_counter()

    return graph, (end - start) * 1000


def measure_memory(GraphClass, create_function):

    tracemalloc.start()

    graph = create_function(GraphClass)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return graph, peak / (1024 * 1024)


def measure_operation(graph, operation):

    start = time.perf_counter()

    operation()

    end = time.perf_counter()

    return (end - start) * 1000


# =========================================================
# SPARSE GRAPH BENCHMARK
# =========================================================

def sparse_benchmark():

    print()
    print("=" * 70)
    print("SPARSE GRAPH BENCHMARK")
    print("=" * 70)

    print("Vertices: 50,000")
    print("Target average degree: approximately 4")
    print()

    classes = [
        ("Adjacency List", AdjacencyListGraph),
        ("Incidence Matrix", IncidenceMatrixGraph)
    ]

    for name, GraphClass in classes:

        print("-" * 70)
        print(name)

        graph, construction_time = measure_construction(
            GraphClass,
            create_sparse_graph
        )

        print("Vertices:", graph.vertex_count())
        print("Edges:", graph.edge_count())

        actual_average_degree = (
            2 * graph.edge_count() / graph.vertex_count()
        )

        print(
            "Average degree:",
            round(actual_average_degree, 2)
        )

        print(
            "Construction time:",
            round(construction_time, 2),
            "ms"
        )

        has_edge_time = measure_operation(
            graph,
            lambda: graph.hasEdge(100, 101)
        )

        neighbour_time = measure_operation(
            graph,
            lambda: graph.neighbours(100)
        )

        bfs_time = measure_operation(
            graph,
            lambda: bfs(graph, 0)
        )

        print(
            "hasEdge:",
            round(has_edge_time, 6),
            "ms"
        )

        print(
            "neighbours:",
            round(neighbour_time, 6),
            "ms"
        )

        print(
            "BFS:",
            round(bfs_time, 2),
            "ms"
        )

        del graph

    print()
    print("Adjacency Matrix:")
    print(
        "Skipped at 50,000 vertices because a full",
        "50,000 x 50,000 matrix is impractical"
    )

    print(
        "Number of matrix cells would be:",
        50000 * 50000
    )

    print(
        "This scaling limitation is discussed in the report."
    )


# =========================================================
# DENSE BIPARTITE BENCHMARK
# =========================================================

def dense_benchmark():

    print()
    print("=" * 70)
    print("DENSE BIPARTITE GRAPH BENCHMARK")
    print("=" * 70)

    print("Vertices: 2,000")
    print("Partitions: 1,000 + 1,000")
    print("Target density: approximately 40%")
    print()

    # Actual dense benchmark for list and matrix
    classes = [
        ("Adjacency List", AdjacencyListGraph),
        ("Adjacency Matrix", AdjacencyMatrixGraph)
    ]

    for name, GraphClass in classes:

        print("-" * 70)
        print(name)

        graph, construction_time = measure_construction(
            GraphClass,
            create_dense_bipartite_graph
        )

        print("Vertices:", graph.vertex_count())
        print("Edges:", graph.edge_count())

        possible_edges = 1000 * 1000

        density = (
            graph.edge_count() / possible_edges
        ) * 100

        print(
            "Density:",
            round(density, 2),
            "%"
        )

        print(
            "Construction time:",
            round(construction_time, 2),
            "ms"
        )

        # Only use integer vertex IDs for the BFS benchmark
        # with a smaller graph below.
        del graph

    print()
    print("Incidence Matrix:")

    print(
        "Skipped for the full 2,000-vertex / 40% graph."
    )

    print(
        "Approximately 800,000 edges would be required."
    )

    print(
        "Incidence matrix cells would be approximately:"
    )

    print(
        "2,000 x 800,000 =",
        2000 * 800000
    )

    print(
        "This is impractical with a Python list-based matrix."
    )


# =========================================================
# SMALL COMMON BENCHMARK
# =========================================================

def common_benchmark():

    print()
    print("=" * 70)
    print("COMMON-SIZE OPERATION BENCHMARK")
    print("=" * 70)

    print("Vertices: 2,000")
    print("Sparse graph")
    print()

    classes = [
        ("Adjacency List", AdjacencyListGraph),
        ("Adjacency Matrix", AdjacencyMatrixGraph),
        ("Incidence Matrix", IncidenceMatrixGraph)
    ]

    for name, GraphClass in classes:

        print("-" * 70)
        print(name)

        graph, construction_time = measure_construction(
            GraphClass,
            create_small_sparse_graph
        )

        print(
            "Construction:",
            round(construction_time, 2),
            "ms"
        )

        has_edge_time = measure_operation(
            graph,
            lambda: graph.hasEdge(100, 101)
        )

        neighbour_time = measure_operation(
            graph,
            lambda: graph.neighbours(100)
        )

        bfs_time = measure_operation(
            graph,
            lambda: bfs(graph, 0)
        )

        print(
            "hasEdge:",
            round(has_edge_time, 6),
            "ms"
        )

        print(
            "neighbours:",
            round(neighbour_time, 6),
            "ms"
        )

        print(
            "BFS:",
            round(bfs_time, 2),
            "ms"
        )

        del graph


# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 70)
    print("GRAPH REPRESENTATION BENCHMARK")
    print("=" * 70)

    sparse_benchmark()

    dense_benchmark()

    common_benchmark()

    print()
    print("=" * 70)
    print("BENCHMARK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()