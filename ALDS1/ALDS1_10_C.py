import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def lcs(x, y):
    n = len(x)
    m = len(y)
    dp = [0] * (m + 1)
    
    for i in range(1, n + 1):
        xi = x[i - 1]
        tmp = dp[:]
        for j in range(1, m + 1):
            if xi == y[j - 1]:
                dp[j] = tmp[j - 1] + 1
            elif dp[j] < dp[j - 1]:
                dp[j] = dp[j - 1]
    return dp[m]


def solve():
    q = int(rl())
    ans_ls = []
    for _ in range(q):
        x = input()
        y = input()
        ans = lcs(x, y)
        ans_ls.append(ans)
    print(*ans_ls, sep='\n')


if __name__ == '__main__':
    solve()
