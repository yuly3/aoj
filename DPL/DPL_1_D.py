import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    n = int(rl())
    lis = [int(rl())]
    for _ in range(n - 1):
        a = int(rl())
        if lis[-1] < a:
            lis.append(a)
        else:
            idx = bisect_left(lis, a)
            lis[idx] = a
    print(len(lis))


if __name__ == '__main__':
    solve()
