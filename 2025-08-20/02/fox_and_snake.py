"""A. The Fox and the Snake"""

text = input().split(" ")
n = int(text[0])
m = int(text[1])

for i in range(n):
    snake = ""
    if i % 2 == 0:
        print("#" * m)
    else:
        if i % 4 == 1:
            snake = "." * (m - 1) + "#"
        else:
            snake = "#" + "." * (m - 1)
        print(snake)
