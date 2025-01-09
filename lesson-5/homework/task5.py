def is_prime(num):
    prime=True
    for i in range(2,int(num**0.5)+1,1):
        if num%i==0:
            prime=False
            break
    return prime
i=int(input("Enter a positive integer: "))

if is_prime(i):
    print(f'{i} is prime.')
else:
    print("Not prime.")
