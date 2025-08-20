"""B. Fence"""

input1 = input()
inputstr = input1.split(" ")
planks = int(inputstr[0])
width = int(inputstr[1])

input2 = input()
inputstr2 = input2.split(" ")
heights = []
for i in range(planks):
    heights.append(i)
    heights[i] = int(inputstr2[i])

totalsum = []
index = []

for x in range(planks - width):
    temp = 0
    for i in range(x, x + width):
        temp += heights[i]

    totalsum.append(temp)
    index.append(x + 1)

min_value = min(totalsum)
min_index = totalsum.index(min_value)

print(min_index + 1)
