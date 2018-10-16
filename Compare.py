from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.vertices = v
        self.bfs_result = 0
        self.ids_result = 0
        self.dls_result = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s, goal):
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

    def dls(self, src, goal, max_depth, called_for_dls=True):
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
        for i in range(max_depth):
            if self.dls(src, goal, i, False):
                return True
        return False


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
