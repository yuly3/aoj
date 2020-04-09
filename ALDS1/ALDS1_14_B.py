import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


class RollingHash:
    def __init__(self, s: str, base, mod):
        self.mod = mod
        length = len(s)
        self.pw = [1] * (length + 1)
        self.h = [0] * (length + 1)
        
        v = 0
        for i in range(length):
            self.h[i + 1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(length):
            self.pw[i + 1] = v = v * base % mod
    
    def query(self, left, right):
        return (self.h[right] - self.h[left] * self.pw[right - left]) % self.mod


def solve():
    T = input()
    P = input()
    
    rh_t = RollingHash(T, 1007, 10 ** 9 + 7)
    rh_p = RollingHash(P, 1007, 10 ** 9 + 7)
    len_p = len(P)
    tgt = rh_p.query(0, len_p)
    
    ans = []
    for i in range(len(T) - len_p + 1):
        a = rh_t.query(i, i + len_p)
        if a == tgt:
            ans.append(i)
    if ans:
        print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
