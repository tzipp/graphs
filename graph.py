class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def from_input(self, txt):
        pass

    def V(self):
        return len(self.vertices)

    def E(self):
        return len(self.edges)

    def add_edge(self, v, w):
        pass

    def adj(self, v):
        pass

    def __str__(self):
        pass


class GraphClient:
    def __init__(self, graph):
        self.graph = graph

    def degree(self, v):
        return len(self.graph.adj(v))

    def max_degree(self):
        degrees = list(map(self.degree, self.graph.vertices))
        return max(degrees)

    def avg_degree(self):
        return 2 * self.graph.E() / self.graph.V()

    def count_self_loops(self):
        count = 0
        for i in range(0, len(self.graph.V())):
            for j in range(0, self.graph.adj(i)):
                if i == j:
                    count += 1

    def __str__(self):
        V = self.graph.V()
        E = self.graph.E()

        s = V + " vertices, " + E + " edges\n"
        for v in range(0, len(V)):
            s += v + ": ";
            for w in range(self.graph.adj(v)):
                s += w + " "
            s += "\n"

