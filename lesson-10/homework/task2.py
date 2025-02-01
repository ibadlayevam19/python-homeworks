import csv
import json


def read_grades(file_name):
    grades = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

def calculate_average(grades):
    subjects = {}
    for entry in grades:
        subject = entry['Subject']
        if subject not in subjects:
            subjects[subject] = []
        subjects[subject].append(entry['Grade'])
    averages = {subject: sum(scores)/len(scores) for subject, scores in subjects.items()}
    return averages

def write_average_grades(averages, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])

grades = read_grades('grades.csv')
averages = calculate_average(grades)
write_average_grades(averages, 'average_grades.csv')