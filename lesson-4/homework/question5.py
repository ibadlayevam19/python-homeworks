string=input("Enter a password: ")
if(len(string)>8):
    if any(char.isupper() for char in string):
        print("Password is strong.")
    else:
        print("Password must contain an uppercase letter.")
else:
    print("Password is too short.")