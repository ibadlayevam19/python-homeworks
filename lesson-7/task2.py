import os

class Employee:
    """Represents an individual employee."""
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        """Return a string representation of the employee."""
        return f"{self.employee_id} {self.name} {self.position} {self.salary}"


class EmployeeManager:
    """Manages employee records using a file."""
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee():
        """Adds a new employee record."""
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(EmployeeManager.FILE_NAME, 'a') as file:
            file.write(f"{employee_id} {name} {position} {salary}\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        """Displays all employee records."""
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        
        with open(EmployeeManager.FILE_NAME, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No records found.")
                return
            
            print("\nEmployee Records:")
            for line in lines:
                print(line.strip())

    @staticmethod
    def search_employee():
        """Search for an employee by Employee ID."""
        emp_id = input("Enter Employee ID to search: ")
        with open(EmployeeManager.FILE_NAME, 'r') as file:
            for line in file:
                if line.startswith(emp_id + " "):  # Ensure exact match for ID
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("Employee ID not found.")

    @staticmethod
    def update_employee():
        """Updates an employee's salary."""
        emp_id = input("Enter Employee ID to update: ")
        updated_salary = input("Enter new salary: ")
        
        if not updated_salary.isdigit():
            print("Invalid salary input. Please enter a valid number.")
            return
        
        updated = False
        with open(EmployeeManager.FILE_NAME, 'r') as file:
            lines = file.readlines()

        with open(EmployeeManager.FILE_NAME, 'w') as file:
            for line in lines:
                parts = line.strip().split()
                if parts[0] == emp_id:
                    parts[3] = updated_salary  # Update salary
                    file.write(" ".join(parts) + "\n")
                    updated = True
                else:
                    file.write(line)
        
        if updated:
            print("Employee salary updated successfully!")
        else:
            print("Employee ID not found.")

    @staticmethod
    def delete_employee():
        """Deletes an employee record."""
        emp_id = input("Enter Employee ID to delete: ")
        deleted = False

        with open(EmployeeManager.FILE_NAME, 'r') as file:
            lines = file.readlines()

        with open(EmployeeManager.FILE_NAME, 'w') as file:
            for line in lines:
                if not line.startswith(emp_id + " "):  # Keep only other records
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("Employee record deleted successfully!")
        else:
            print("Employee ID not found.")


def main():
    """Runs the menu-based Employee Management System."""
    while True:
        print("\nWelcome to Employee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            EmployeeManager.add_employee()
        elif choice == "2":
            EmployeeManager.view_all_employees()
        elif choice == "3":
            EmployeeManager.search_employee()
        elif choice == "4":
            EmployeeManager.update_employee()
        elif choice == "5":
            EmployeeManager.delete_employee()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
