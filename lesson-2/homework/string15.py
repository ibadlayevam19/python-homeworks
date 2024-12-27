string=input("Enter a sentence: ")
words=string.split()
acronym=""
for i in range(len(words)):
    acronym+=words[i][0]
print(acronym)