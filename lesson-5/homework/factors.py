def factors(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(f'{i} is a factor of {num}')
i=int(input("Enter a positive integer: "))
factors(i)
