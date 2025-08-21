"""Codeforces 136A : Presents"""

p = list(map(int, input().split(" ")))

result = []

for i in range(len(p)):
    for j, val in enumerate(p):
        if val == i + 1:
            result.append(j + 1)
            break

print(" ".join(map(str, result)))
