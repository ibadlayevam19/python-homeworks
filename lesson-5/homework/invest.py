def invest(amount, rate, years):
    for i in range(1,years+1,1):
        amount=amount+rate*amount
        print(f'year {i}: ${amount:.2f}')
a=input("The principal amount: ")
r=input("An annual rate: ")
y=input("For how many years: ")
invest(float(a),float(r),int(y))