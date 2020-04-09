import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    m, n = map(int, rl().split())
    MOD = 10 ** 9 + 7
    ans = pow(m, n, MOD)
    print(ans)


if __name__ == '__main__':
    solve()
