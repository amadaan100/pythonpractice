#name = input("What is your name? ")

#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

#file = open("names.txt" , "a")
#file.write(f"{name}\n")
#file.close()

#with open("names.txt", "r") as file:
#    names = file.readlines()

#for name in names:
#    print(name.rstrip())

with open("names.txt", "r") as file:
    for line in file:
        print(line.rstrip())

#with open("names.txt", "r") as file:
#    for line in sorted(file):
#        print(line.rstrip())