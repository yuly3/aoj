import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, W = map(int, rl().split())
    vw = [list(map(int, rl().split())) for _ in range(N)]
    
    dp = [0] * (W + 1)
    
    for i in range(N):
        v, w = vw[i]
        for j in range(w, W + 1):
            dp[j] = max(dp[j], dp[j - w] + v)
    print(dp[W])


if __name__ == '__main__':
    solve()
