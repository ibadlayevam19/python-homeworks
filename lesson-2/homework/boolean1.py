username=input("Enter a username: ")
password=input("Enter a password: ")
if bool(username.strip()) and bool(password.strip()):
    print("They are not empty.")
else:
    print("Enter both.")