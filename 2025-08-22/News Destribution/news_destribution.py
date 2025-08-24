"""Codeforces 1167C : News Distribution"""

import sys


def find(x):
    """Which connected component x belongs to"""
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    """Unites the connected components of a and b"""
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]


n, m = map(int, input().split())

parent = list(range(n))
size = [1] * n


for _ in range(m):
    data = list(map(int, input().split()))
    k = data[0]
    if k <= 1:
        continue
    members = [x - 1 for x in data[1:]]
    base = members[0]
    for u in members[1:]:
        union(base, u)

ans = [0] * n
for i in range(n):
    ans[i] = size[find(i)]
print(*ans)
