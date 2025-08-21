"""A. String Exercise"""

text = input()

# Initialize lowertext
resulttext = []
for s in text:
    c = s.lower()
    if c not in ["a", "o", "y", "e", "u", "i"]:
        resulttext.append(c)

print("." + "".join(resulttext))
