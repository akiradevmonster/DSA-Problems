"""B. Fence"""

inputstr = input().split(" ")
planks = int(inputstr[0])
width = int(inputstr[1])

inputstr2 = input().split(" ")
heights = []
for i in range(planks):
    heights.append(i)
    heights[i] = int(inputstr2[i])

totalsum = []
index = []

# Real calculatin section
for x in range(planks - width):
    temp = sum(heights[x : x + width])
    totalsum.append(temp)
    index.append(x + 1)

min_value = min(totalsum)
min_index = totalsum.index(min_value)

print(min_index + 1)
