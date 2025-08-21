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
        realvalue[i:j] = [1 - x for x in realvalue[i:j]]
        totalArray.append(realvalue.count(1))

maxval = max(totalArray)
print(maxval)
