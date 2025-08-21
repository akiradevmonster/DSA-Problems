"""A. The Fox and the Snake"""

text = input().split(" ")
n = int(text[0])
m = int(text[1])

i = 0
while i < n:
    if i % 2 == 0:
        print("#" * m)
    else:
        if i % 4 == 1:
            print("." * (m - 1) + "#")
        else:
            print("#" + "." * (m - 1))
    i += 1
