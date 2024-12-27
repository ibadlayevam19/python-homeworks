string=input("Input: ")
start=input("Starts with: ")
end=input("Ends with: ")
if string.startswith(start) and string.endswith(end):
    print("Yes, it starts and ends with those words you entered.")
else:
    print("No, it doen't start ad end with those words you entered.")

