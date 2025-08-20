"""C. Cut and Count"""

leng = int(input())
text = input()

counts = []

for x in range(1, leng):
    left = text[0:x]
    right = text[x:leng]
    leftchar = []
    rightchar = []
    for s in left:
        if not s in leftchar:
            leftchar.append(s)

    for s in right:
        if not s in rightchar:
            rightchar.append(s)

    # print(leftchar, rightchar)
    sameLetterList = []
    for s in leftchar:
        if s in rightchar:
            sameLetterList.append(s)
    counts.append(len(sameLetterList))

maxvalue = max(counts)
print(maxvalue)
