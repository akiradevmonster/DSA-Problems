"""B. Faktor"""

temp = input()
temps = temp.split(" ")
totalArticle = int(temps[0])
totalAnswer = int(temps[1])

print(totalArticle * (totalAnswer - 1) + 1)
