first=int(input("Enter the first integer: "))
second=int(input("Enter the second integer: "))
third=int(input("Enter the third integer: "))
if (first!=second) and second!=third and third!=first:
    print("They all are different.")
else:
    print("Two or more equal numbers.")