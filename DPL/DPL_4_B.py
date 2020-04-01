from bisect import bisect_right, bisect_left


def make_sums(items, limit):
    n = len(items)
    res = [[] for _ in range(limit + 1)]
    for s in range(1 << n):
        sum_a, cnt = 0, 0
        for i in range(n):
            if s >> i & 1:
                sum_a += items[i]
                cnt += 1
        if cnt <= limit:
            res[cnt].append(sum_a)
    return res


def solve():
    N, K, L, R = map(int, input().split())
    a = list(map(int, input().split()))
    
    fi_a = a[:N // 2]
    se_a = a[N // 2:]
    fi_sum_a = make_sums(fi_a, K)
    se_sum_a = make_sums(se_a, K)
    for items in se_sum_a:
        items.sort()
    
    ans = 0
    for i, items in enumerate(fi_sum_a):
        for item in items:
            left = bisect_left(se_sum_a[K - i], L - item)
            right = bisect_right(se_sum_a[K - i], R - item)
            ans += right - left
    print(ans)


if __name__ == '__main__':
    solve()
