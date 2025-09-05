from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np


class Graph:
    """A class to represent a graph and compare search algorithms.

    This class provides methods to build a graph and perform Breadth-First
    Search (BFS), Depth-Limited Search (DLS), and Iterative Deepening Search
    (IDS). It also tracks the number of nodes visited by each search to
    facilitate performance comparison.

    Attributes:
        graph (defaultdict): A dictionary to store the graph's adjacency list.
        vertices (int): The total number of vertices in the graph.
        bfs_result (int): Counter for nodes visited during BFS.
        ids_result (int): Counter for nodes visited during IDS.
        dls_result (int): Counter for nodes visited during DLS.
    """
    def __init__(self, v):
        """Initializes the Graph object.

        Args:
            v (int): The number of vertices in the graph.
        """
        self.graph = defaultdict(list)
        self.vertices = v
        self.bfs_result = 0
        self.ids_result = 0
        self.dls_result = 0

    def add_edge(self, u, v):
        """Adds a directed edge to the graph.

        Args:
            u (int): The source vertex.
            v (int): The destination vertex.
        """
        self.graph[u].append(v)

    def bfs(self, s, goal):
        """Performs Breadth-First Search to find a goal node.

        Args:
            s (int): The starting node for the search.
            goal (int): The node to search for.

        Returns:
            bool: True if the goal is found, False otherwise.
        """
        chk = [False] * self.vertices
        queue = [s]
        chk[s] = True
        while queue:
            s = queue.pop(0)
            if s == goal:
                return True
            self.bfs_result += 1
            for u in self.graph[s]:
                if not chk[u]:
                    queue.append(u)
                    chk[u] = True
        return False

    def dls(self, src, goal, max_depth, called_for_dls=True):
        """Performs Depth-Limited Search.

        This is a recursive function that performs a depth-first search up to
        a specified depth limit.

        Args:
            src (int): The current node to search from.
            goal (int): The node to search for.
            max_depth (int): The maximum depth to search.
            called_for_dls (bool, optional): A flag to indicate if the call
                is for DLS or IDS, to correctly update counters. Defaults to True.

        Returns:
            bool: True if the goal is found within the depth limit, False otherwise.
        """
        if src == goal:
            return True
        self.ids_result += 1
        if called_for_dls:
            self.dls_result += 1
        if max_depth <= 0:
            return False
        for u in self.graph[src]:
            if self.dls(u, goal, max_depth - 1):
                return True
        return False

    def ids(self, src, goal, max_depth):
        """Performs Iterative Deepening Search.

        This method repeatedly calls Depth-Limited Search with increasing depth
        limits until the goal is found or the maximum depth is reached.

        Args:
            src (int): The starting node for the search.
            goal (int): The node to search for.
            max_depth (int): The maximum depth to explore.

        Returns:
            bool: True if the goal is found, False otherwise.
        """
        for i in range(max_depth):
            if self.dls(src, goal, i, False):
                return True
        return False


def main():
    """Main function to run the graph search algorithm comparison.

    This function orchestrates the comparison by:
    1. Creating a random graph.
    2. Running BFS, IDS, and DLS searches for a number of random targets.
    3. Collecting performance data (nodes visited).
    4. Plotting the results for visual comparison.
    """
    number_of_nodes = np.random.randint(100, 200)
    nodes = np.arange(number_of_nodes)

    print(number_of_nodes)
    print(nodes)

    g = Graph(number_of_nodes)

    number_of_edges = np.random.randint(1000, 2000)
    for i in range(number_of_edges):
        x = y = np.random.randint(number_of_nodes)
        while y == x:
            y = np.random.randint(number_of_nodes)
        g.add_edge(x, y)

    src = 0
    number_of_tests = 5
    x = np.arange(number_of_tests)
    y1 = []
    y2 = []
    y3 = []

    for i in range(number_of_tests):
        target = np.random.randint(0, number_of_nodes)
        print("\nthe target is: ", target)
        max_depth = 10

        g.bfs_result = 0
        g.ids_result = 0
        g.dls_result = 0

        g.bfs(src, target)
        print(g.bfs_result, " => bfs result")
        y1.append(g.bfs_result)

        g.ids(src, target, max_depth)
        print(g.ids_result, " => ids result")
        y2.append(g.ids_result)

        g.dls(src, target, max_depth)
        print(g.dls_result, " => dls result")
        y3.append(g.dls_result)

    plt.plot(x, y1, x, y2, x, y3)
    plt.legend(('bfs', 'ids', 'dls'), loc='upper left')
    plt.show()


if __name__ == "__main__":
    main()
