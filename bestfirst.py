from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def greedy_search(self, start, goal):
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, start))

        while not priority_queue.empty():
            cost, current_node = priority_queue.get()
            print(current_node, end=" ")

            if current_node == goal:
                print("\nGoal Reached!")
                return True

            visited.add(current_node)

            for neighbor, neighbor_cost in self.graph[current_node]:
                if neighbor not in visited:
                    priority_queue.put((neighbor_cost, neighbor))

        print("\nGoal Not Reached!")
        return False

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', [('B', 5), ('C', 8)])
    g.add_edge('B', [('D', 12), ('E', 15)])
    g.add_edge('C', [('F', 6)])
    g.add_edge('D', [])
    g.add_edge('E', [('G', 7)])
    g.add_edge('F', [('H', 9)])
    g.add_edge('G', [])
    g.add_edge('H', [])

    start_node = 'A'
    goal_node = 'G'

    print(f"Greedy Best-First Search from {start_node} to {goal_node}:")
    g.greedy_search(start_node, goal_node)
