#use of csv import
import csv

students = []
with open('students.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({ 'name': row['name'], 'job': row['job']})

for student in sorted(students, key=lambda student: student['name']):
    print(student)