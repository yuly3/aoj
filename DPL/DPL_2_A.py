import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    V, E = map(int, rl().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        s, t, d = map(int, rl().split())
        graph[s].append([t, d])
    
    INF = 10 ** 18
    dp = [[INF] * V for _ in range(1 << V)]
    dp[0][0] = 0
    
    for s in range(1 << V):
        for l_node in range(V):
            if dp[s][l_node] == INF:
                continue
            for to, cost in graph[l_node]:
                if s >> to & 1:
                    continue
                ns = s | (1 << to)
                dp[ns][to] = min(dp[ns][to], dp[s][l_node] + cost)
    if dp[-1][0] == INF:
        print(-1)
    else:
        print(dp[-1][0])


if __name__ == '__main__':
    solve()
