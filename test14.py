students = []

with open("students.csv") as file:
    for line in file:
        name, job = line.strip().split(',')
        students.append({'name': name, 'job': job})

for student in sorted(students, key=lambda student: student['job']):
    print(student)