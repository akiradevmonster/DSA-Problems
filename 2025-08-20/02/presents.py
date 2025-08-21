"""Codeforces 136A : Presents"""

p = list(map(int, input().split(" ")))

result = []
for i in range(len(p)):
    result.append(p.index(i + 1) + 1)

print(" ".join(map(str, result)))
