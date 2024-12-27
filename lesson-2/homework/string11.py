string=input("Enter a string: ")
digits="0123456789"
count=0
for i in range(len(string)):
    if string[i] in digits:
        count+=1
print(f"The number of digits is {count}")
