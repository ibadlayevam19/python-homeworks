import json
import csv
import os
from datetime import datetime

class Task:
    """Represents a single task."""
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data.get("due_date"), data["status"])

class FileHandler:
    """Abstract class for file handling."""
    def save(self, tasks, filename):
        raise NotImplementedError

    def load(self, filename):
        raise NotImplementedError

class CSVFileHandler(FileHandler):
    """Handles CSV file operations."""
    def save(self, tasks, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["task_id", "title", "description", "due_date", "status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        tasks = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return tasks

class JSONFileHandler(FileHandler):
    """Handles JSON file operations."""
    def save(self, tasks, filename):
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            return [Task.from_dict(task) for task in json.load(file)]

class TaskManager:
    """Manages task operations."""
    def __init__(self, file_handler, filename):
        self.file_handler = file_handler
        self.filename = filename
        self.tasks = self.file_handler.load(filename)

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ") or task.title
                task.description = input("Enter new Description: ") or task.description
                task.due_date = input("Enter new Due Date (YYYY-MM-DD, optional): ") or task.due_date
                task.status = input("Enter new Status (Pending/In Progress/Completed): ") or task.status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered_tasks:
            print("No tasks found with that status.")
            return
        for task in filtered_tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self):
        self.file_handler.save(self.tasks, self.filename)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.file_handler.load(self.filename)
        print("Tasks loaded successfully!")


def main():
    print("Select file format:")
    print("1. CSV")
    print("2. JSON")
    choice = input("Enter choice: ")
    
    file_handler = CSVFileHandler() if choice == "1" else JSONFileHandler()
    filename = "tasks.csv" if choice == "1" else "tasks.json"
    
    manager = TaskManager(file_handler, filename)
    
    while True:
        print("\nTo-Do Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.update_task()
        elif choice == "4":
            manager.delete_task()
        elif choice == "5":
            manager.filter_tasks()
        elif choice == "6":
            manager.save_tasks()
        elif choice == "7":
            manager.load_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()