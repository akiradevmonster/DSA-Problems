"""Codeforces 545C : Woodcutters"""

n = int(input())
trees = []

for i in range(n):
    coordinate = input().split(" ")
    trees.append([int(coordinate[0]), int(coordinate[1])])

total_count = 0
left_side = 0
right_side = 0
for i in range(n):
    if i == 0:
        left_side = trees[i][0] - trees[i][1]
        right_side = trees[i][0]
        total_count += 1
    elif i == n - 1:
        left_side = trees[i][0]
        right_side = trees[i][0] + trees[i][1]
        total_count += 1
    else:
        if trees[i][0] - trees[i][1] > right_side:
            left_side = trees[i][0] - trees[i][1]
            right_side = trees[i][0]
        elif trees[i][0] + trees[i][1] < trees[i + 1][0]:
            left_side = trees[i][0]
            right_side = trees[i][0] + trees[i][1]
        else:
            left_side = trees[i][0]
            right_side = trees[i][0]
        if left_side != trees[i][0] or right_side != trees[i][0]:
            total_count += 1

print(total_count)
