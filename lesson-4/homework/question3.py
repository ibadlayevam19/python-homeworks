txt=input("Word: ")
l=list(txt)
vowels='AEIOUaeiou'
used=[]
i=2
def check(str):
    if(str not in vowels) and (str not in used):
        return True
while(i<len(l)-1):
    if(check(l[i])):
        l.insert(i+1,'_')
        used.append(l[i])
        i+=4
    else:
        i+=1
result=''.join(l)
print(result)