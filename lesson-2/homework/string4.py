a=input("Enter a string to check if palindrome: ")
length=len(a)
for i in range(length//2):
    if (a[i]==a[length-1-i]):
        print("It is a palindrome.")
    else:
        print("Not palindrome.")

