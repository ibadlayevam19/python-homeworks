#as we didn't cover the lists yet
num=int(input("How many words are you going to join? "))
mylist=[]
out_str=""
for i in range(num):
    word=input("Enter a word: ")
    mylist.append(word)
for i in range(num-1):
    out_str+=f"{mylist[i]}-"
out_str+=mylist[-1]
print(out_str)
