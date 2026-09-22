from .graph import Graph


# =========================================================
# ADJACENCY LIST
# =========================================================

class AdjacencyListGraph(Graph):

    def __init__(self, directed=False):
        super().__init__(directed)
        self.adj = {}

    def addVertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def addEdge(self, u, v):

        self.addVertex(u)
        self.addVertex(v)

        # Avoid duplicate edges
        if v in self.adj[u]:
            return

        self.adj[u].add(v)

        if self.directed == False:
            self.adj[v].add(u)

    def hasEdge(self, u, v):
        if u not in self.adj:
            return False

        return v in self.adj[u]

    def neighbours(self, v):
        if v not in self.adj:
            return []

        return list(self.adj[v])

    def degree(self, v):
        if v not in self.adj:
            return 0

        return len(self.adj[v])

    def edges(self):

        result = []

        if self.directed:

            for u in self.adj:
                for v in self.adj[u]:
                    result.append((u, v))

        else:

            visited = set()

            for u in self.adj:

                for v in self.adj[u]:

                    edge = frozenset((u, v))

                    if edge not in visited:
                        result.append((u, v))
                        visited.add(edge)

        return result

    def vertex_count(self):
        return len(self.adj)

    def edge_count(self):
        return len(self.edges())


# =========================================================
# ADJACENCY MATRIX
# =========================================================

class AdjacencyMatrixGraph(Graph):

    def __init__(self, directed=False):

        super().__init__(directed)

        self.vertices = []
        self.matrix = []

        # Vertex -> matrix index
        self.index = {}

    def addVertex(self, v):

        if v in self.index:
            return

        self.index[v] = len(self.vertices)
        self.vertices.append(v)

        # Add new column
        for row in self.matrix:
            row.append(0)

        # Add new row
        new_row = []

        for i in range(len(self.vertices)):
            new_row.append(0)

        self.matrix.append(new_row)

    def addEdge(self, u, v):

        self.addVertex(u)
        self.addVertex(v)

        i = self.index[u]
        j = self.index[v]

        # Avoid duplicate edge
        if self.matrix[i][j] == 1:
            return

        self.matrix[i][j] = 1

        if self.directed == False:
            self.matrix[j][i] = 1

    def hasEdge(self, u, v):

        if u not in self.index or v not in self.index:
            return False

        i = self.index[u]
        j = self.index[v]

        return self.matrix[i][j] == 1

    def neighbours(self, v):

        if v not in self.index:
            return []

        i = self.index[v]

        result = []

        for j in range(len(self.vertices)):

            if self.matrix[i][j] == 1:
                result.append(self.vertices[j])

        return result

    def degree(self, v):

        if v not in self.index:
            return 0

        i = self.index[v]

        count = 0

        for value in self.matrix[i]:

            if value == 1:
                count += 1

        return count

    def edges(self):

        result = []

        n = len(self.vertices)

        if self.directed:

            for i in range(n):

                for j in range(n):

                    if self.matrix[i][j] == 1:
                        result.append(
                            (self.vertices[i], self.vertices[j])
                        )

        else:

            for i in range(n):

                for j in range(i, n):

                    if self.matrix[i][j] == 1:
                        result.append(
                            (self.vertices[i], self.vertices[j])
                        )

        return result

    def vertex_count(self):
        return len(self.vertices)

    def edge_count(self):
        return len(self.edges())


# =========================================================
# INCIDENCE MATRIX
# =========================================================

class IncidenceMatrixGraph(Graph):

    def __init__(self, directed=False):

        super().__init__(directed)

        self.vertices = []
        self.edge_list = []
        self.matrix = []

        self.index = {}

    def addVertex(self, v):

        if v in self.index:
            return

        self.index[v] = len(self.vertices)
        self.vertices.append(v)

        row = []

        for i in range(len(self.edge_list)):
            row.append(0)

        self.matrix.append(row)

    def addEdge(self, u, v):

        # Do not add duplicate edges
        if self.hasEdge(u, v):
            return

        self.addVertex(u)
        self.addVertex(v)

        self.edge_list.append((u, v))

        # Add new column
        for row in self.matrix:
            row.append(0)

        u_index = self.index[u]
        v_index = self.index[v]

        edge_index = len(self.edge_list) - 1

        if self.directed:

            # -1 = source
            # +1 = destination

            self.matrix[u_index][edge_index] = -1
            self.matrix[v_index][edge_index] = 1

        else:

            self.matrix[u_index][edge_index] = 1
            self.matrix[v_index][edge_index] = 1

    def hasEdge(self, u, v):

        for edge in self.edge_list:

            if self.directed:

                if edge[0] == u and edge[1] == v:
                    return True

            else:

                if ((edge[0] == u and edge[1] == v) or
                    (edge[0] == v and edge[1] == u)):

                    return True

        return False

    def neighbours(self, v):

        if v not in self.index:
            return []

        result = []

        for edge in self.edge_list:

            u = edge[0]
            w = edge[1]

            if self.directed:

                if u == v:
                    result.append(w)

            else:

                if u == v:
                    result.append(w)

                elif w == v:
                    result.append(u)

        return list(set(result))

    def degree(self, v):
        return len(self.neighbours(v))

    def edges(self):
        return self.edge_list.copy()

    def vertex_count(self):
        return len(self.vertices)

    def edge_count(self):
        return len(self.edge_list)