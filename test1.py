#practice dictionary
students = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Charlie": 88,
}

for number, student in enumerate(students, start=1):
    print(number, student, students[student], sep=": ")
#for student in students:
#    print(student, students[student], sep=": ")

