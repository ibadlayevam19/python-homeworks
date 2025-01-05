prime=True
print(2)
for i in range(3,101,2):
    prime=True
    for j in range(3,int(i**(1/2)+1),2):
        if(i%j==0):
            prime=False
            break
    if(prime):
        print(i)


