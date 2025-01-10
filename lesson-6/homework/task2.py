

def option1():
    file=open("employees.txt", 'a')
    ID=input("Employee ID: ")
    Name=input("Name: ")
    Position=input("Position: ")
    Salary=input("Salary: ")
    t=(ID,Name,Position,Salary)
    for i in t:
       file.write(i)
       file.write(' ')
    file.write("\n")
    print("Record has been added successfully!")
    file.close()
def option2():
    file=open("employees.txt", 'r')
    for line in file:
        print(line, end='')
    file.close()
def option3():
    id=input("Enter Employee ID to search: ")
    file=open("employees.txt", 'r+')
    l=file.readlines()
    for i in l:
        if id==i.split()[0]:
            print(f"Name: {i.split()[1]}\nPosition: {i.split()[2]}\nSalary: {i.split()[3]}")
            break
    else:
        print("ID doesn't exist.")
    file.close()
def option4():
    try:
        id=input("Enter Employee ID to update: ")
    except ValueError:
        print("Enter the id.")
    file=open("employees.txt", 'r')
    l=file.readlines()
    file.close()
    with open("employees.txt",'w') as file:
        for i in l:
            if id==i.split()[0]:
                updated=input("Updated salary: ")
                file.write(f"{i.split()[0]} {i.split()[1]} {i.split()[2]} {updated}\n")
            else:
                file.write(i)
        print("Employee salary has been updated successfully!")   

def option5():
    try:
        id=input("Enter Employee ID to delete: ")
    except ValueError:
        print("Enter the id.")
    file=open("employees.txt", 'r')
    l=file.readlines()
    file.close()
    with open("employees.txt",'w') as file:
        for i in l:
            if i.strip() and id!=i.split()[0]:
                file.write(i)
        print("Employee record has been deleted successfully!")
while True:
    print("1. Add new employee record\n\
2. View all employee records\n\
3. Search for an employee by Employee ID\n\
4. Update an employee's information\n\
5. Delete an employee record\n\
6. Exit")
    c=int(input("Choose: "))
    if(c==1):
        option1()
    elif(c==2):
        option2()
    elif(c==3):
        option3()
    elif(c==4):
        option4()
    elif(c==5):
        option5()
    else:
        print("Exited program.")
        break






