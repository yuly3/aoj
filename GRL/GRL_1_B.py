import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline
INF = 10 ** 18


def bellman_ford(n, edges, s):
    dists = [INF] * n
    dists[s] = 0
    for cnt in range(n):
        for u, v, cost in edges:
            if dists[u] != INF and dists[u] + cost < dists[v]:
                if cnt == n - 1:
                    return -1
                dists[v] = dists[u] + cost
    return dists


def solve():
    V, E, r = map(int, rl().split())
    edges = [tuple(map(int, rl().split())) for _ in range(E)]
    
    ans = bellman_ford(V, edges, r)
    for num in ans:
        print(num if num != INF else 'INF')


if __name__ == '__main__':
    solve()
