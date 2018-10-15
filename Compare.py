from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))

        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def dls(self, src, target, maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        for i in self.graph[src]:
            if self.dls(i, target, maxDepth - 1):
                return True
        return False

    def ids(self, src, target, maxDepth):
        for i in range(maxDepth):
            if self.dls(src, target, i):
                return True
        return False


g = Graph(7);
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

target = 6;
maxDepth = 3;
src = 0

g.BFS(2)

if g.ids(src, target, maxDepth):
    print ("Target is reachable from source " +
           "within max depth")
else:
    print ("Target is NOT reachable from source " +
           "within max depth")