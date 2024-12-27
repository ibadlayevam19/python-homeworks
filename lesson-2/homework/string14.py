first=input("Enter first string: ")
equal=True
second=input("Enter the second one: ")
if(len(first)==len(second)):
    for i in range(len(first)):
      if(first[i]!=second[i]):
        equal=False
    if equal:
      print("They are equal.")
    else:
      print("Not equal.")
else:
  print("They are not even in same length.")