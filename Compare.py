from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.verts = v

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        chk = [False] * self.verts
        queue = [s]
        chk[s] = True
        while queue:
            s = queue.pop(0)
            print("*", s)
            for u in self.graph[s]:
                if not chk[u]:
                    queue.append(u)
                    chk[u] = True

    def dls(self, src, goal, maxDepth):
        if src == goal:
            return True
        if maxDepth <= 0:
            return False
        for u in self.graph[src]:
            if self.dls(u, goal, maxDepth - 1):
                return True
        return False

    def ids(self, src, goal, maxDepth):
        for i in range(maxDepth):
            if self.dls(src, goal, i):
                return True
        return False


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

target = 6
maxDepth = 3
src = 0

g.bfs(0)

if g.ids(src, target, maxDepth):
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")
