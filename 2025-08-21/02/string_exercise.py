"""A. String Exercise"""

text = input()

# Initialize lowertext
resulttext = []
lowertext = []
voweltext = ["a", "o", "y", "e", "u", "i"]
for s in text:
    c = s.lower()
    if c not in voweltext:
        lowertext.append(c)
        resulttext.append(c)

print("." + "".join(resulttext))
