with open("students.csv",'r') as file:
    for line in sorted(file):
        name, job = line.rstrip().split(",")
        print(f"Name: {name}, job:{job}")

#        print(f"Name: {row[0]}, job:{row[1]}")
#        print(line.rstrip().split(","))
        