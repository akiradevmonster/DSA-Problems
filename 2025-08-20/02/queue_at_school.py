"""Codeforces 266B : Queue at the School"""

text = input().split(" ")
total_count = int(text[0])
time = int(text[1])
queue = list(input())

t = 0
while t < time:
    i = 0
    while i < total_count - 1:
        if queue[i] == "B" and queue[i + 1] == "G":
            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i += 2
        else:
            i += 1
    t += 1

print("".join(queue))
