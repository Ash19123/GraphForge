# Assignment 1 - Graph Representations

## Requirements

Python 3.x

Pytest is required for running the test cases.

Install pytest using:

pip install pytest

## Project

This project implements three graph representations:

1. Adjacency Matrix
2. Adjacency List
3. Incidence Matrix

Both directed and undirected graphs are supported.

## Common Operations

The following operations are supported:

- addVertex()
- addEdge()
- hasEdge()
- neighbours()
- degree()
- edges()

## Algorithms

The following algorithms are implemented:

- Breadth First Search (BFS)
- Connected Components

## Conversions

Conversions are implemented between all three representations:

- Adjacency Matrix -> Adjacency List
- Adjacency List -> Adjacency Matrix
- Adjacency Matrix -> Incidence Matrix
- Incidence Matrix -> Adjacency Matrix
- Adjacency List -> Incidence Matrix
- Incidence Matrix -> Adjacency List

Round-trip conversion tests are also included.

## Running Tests

From the project root:

python -m pytest -v

## Running Benchmark

From the project root:

python benchmark/benchmark.py

## Environment

Python 3.x
pytest