string= input("Enter a string: ")
length=len(string)
reversed=""
for i in range(length):
    reversed+=string[length-1-i]
print(reversed)