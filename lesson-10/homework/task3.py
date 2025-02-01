import csv
import json


def load_tasks(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def save_tasks(tasks, file_name):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks
    return total_tasks, completed_tasks, pending_tasks, avg_priority

def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

tasks = load_tasks('tasks.json')
display_tasks(tasks)
print(calculate_task_stats(tasks))
convert_json_to_csv('tasks.json', 'tasks.csv')