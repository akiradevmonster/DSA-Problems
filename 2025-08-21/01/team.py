"""A. Team"""

count = int(input())
problem = []

totalcount = 0

for index in range(count):
    solution = input()
    solutions = solution.split(" ")
    result = 0
    for sol in solutions:
        if int(sol) == 1:
            result += 1
    if result >= 2:
        totalcount += 1

print(totalcount)
