students =[
    {"name": "John", "score": 95,"house": "Gryffindor" },
    {"name": "Alice", "score": 88,"house": "Slytherin" },
    {"name": "Bob", "score": 76,"house": "Hufflepuff" },
    {"name": "Charlie", "score": 92,"house": None }
]

for student in students:
    print(student["name"], student["score"], student["house"], sep=": ")
