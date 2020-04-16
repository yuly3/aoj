import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2 + N0 + N1
        self.graph = [[] for _ in range(N)]
        self.level = None
        self.it = None
        for i in range(N0):
            forward = [2 + i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.graph[0].append(forward)
            self.graph[2 + i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2 + N0 + i, 0, forward]
            bs.append(backward)
            self.graph[2 + N0 + i].append(forward)
            self.graph[1].append(backward)
    
    def add_edge(self, fr, to):
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.graph[v0].append(forward)
        self.graph[v1].append(backward)
    
    def bfs(self):
        graph = self.graph
        level = [-1] * self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in graph[v]:
                if cap and level[w] == -1:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] != -1
    
    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0
    
    def flow(self):
        flow = 0
        graph = self.graph
        bfs = self.bfs
        dfs = self.dfs
        while bfs():
            *self.it, = map(iter, graph)
            while dfs(0, 1):
                flow += 1
        return flow
    
    def matching(self):
        return [cap for _, cap, _ in self.backwards]


def solve():
    X, Y, E = map(int, rl().split())
    hck = HopcroftKarp(X, Y)
    for _ in range(E):
        x, y = map(int, rl().split())
        hck.add_edge(x, y)
    
    ans = hck.flow()
    print(ans)


if __name__ == '__main__':
    solve()
