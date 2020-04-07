import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    n, m = map(int, rl().split())
    c = list(map(int, rl().split()))
    
    dp = [10 ** 5] * (n + 1)
    dp[0] = 0
    
    for ci in c:
        for j in range(ci, n + 1):
            dp[j] = min(dp[j], dp[j - ci] + 1)
    print(dp[n])


if __name__ == '__main__':
    solve()
