"""B. Flipping Game"""

count = int(input())
values = input()
value = values.split(" ")
orgvalue = []
for x in value:
    orgvalue.append(int(x))

totalArray = []

for i in range(count):
    for j in range(i, count):
        realvalue = orgvalue.copy()
        for x in range(i, j + 1):
            realvalue[x] = 1 - realvalue[x]

        totalCount = 0
        for x in range(0, count):
            if realvalue[x] == 1:
                totalCount += 1
        totalArray.append(totalCount)


maxval = max(totalArray)
print(maxval)
