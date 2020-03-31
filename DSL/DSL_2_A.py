import sys

rl = sys.stdin.readline


class SegmentTree:
    def __init__(self, n, init_value, segfunc, ide_ele):
        self.N0 = 2 ** (n - 1).bit_length()
        self.ide_ele = ide_ele
        self.data = [ide_ele] * (2 * self.N0)
        self.segfunc = segfunc
        
        for i in range(n):
            self.data[i + self.N0 - 1] = init_value[i]
        for i in range(self.N0 - 2, -1, -1):
            self.data[i] = self.segfunc(self.data[2 * i + 1], self.data[2 * i + 2])
    
    def update(self, _k, x):
        k = _k + self.N0 - 1
        self.data[k] = x
        while k:
            k = (k - 1) // 2
            self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])
    
    def query(self, left, right):
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
        a, b = [], []
        
        while L < R:
            if L & 1:
                a.append(L - 1)
                L += 1
            if R & 1:
                R -= 1
                b.append(R - 1)
            L >>= 1
            R >>= 1
        for i in a + (b[::-1]):
            res = self.segfunc(res, self.data[i])
        
        return res


def solve():
    n, q = map(int, rl().split())
    INF = 2 ** 31 - 1
    init_val = [INF] * n
    seg_tree = SegmentTree(n, init_val, min, INF)
    
    for _ in range(q):
        com, x, y = map(int, rl().split())
        if com:
            print(seg_tree.query(x, y + 1))
        else:
            seg_tree.update(x, y)


if __name__ == '__main__':
    solve()
