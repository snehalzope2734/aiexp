class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, max_depth):
        if src == target:
            return True
        if max_depth <= 0:
            return False

        for neighbor in self.graph[src]:
            if self.DLS(neighbor, target, max_depth - 1):
                return True
        return False

    def IDDFS(self, src, target, max_depth):
        for depth in range(max_depth):
            if self.DLS(src, target, depth):
                return True
        return False

# Example usage:
if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    src = 0
    target = 6
    max_depth = 3

    if g.IDDFS(src, target, max_depth):
        print(f"Path from {src} to {target} exists within depth {max_depth}")
    else:
        print(f"No path found from {src} to {target} within depth {max_depth}")
