list1 = [1, 1, 2]
list2 = [2, 3, 4]
l=[]
for i in list1:
    if i not in list2:
        l.append(i)
for i in list2:
    if i not in list1:
        l.append(i)
print(l)