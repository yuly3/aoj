import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    
    if temp != 1:
        arr.append([temp, 1])
    if not arr:
        arr.append([n, 1])
    
    return arr


def solve():
    n = int(rl())
    facts = factorization(n)
    ans = []
    for fa, c in facts:
        for _ in range(c):
            ans.append(fa)
    print('{}: '.format(n), end='')
    print(*ans, sep=' ')


if __name__ == '__main__':
    solve()
