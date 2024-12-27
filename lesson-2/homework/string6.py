string=input("Enter the main string: ")
another=input("Enter the substring: ")
if another in string:
    print(f"{another} is found in {string}")
else:
    print(f"Not found.")