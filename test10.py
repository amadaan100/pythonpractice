names = []

for i in range(5):
    names.append(input("Enter a name: "))

for name in sorted(names , reverse=True):
    print(f"hello {name}")