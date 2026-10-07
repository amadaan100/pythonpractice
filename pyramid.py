def main():
    height = int(input("Enter the height of the triangle: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(i, end=" ")
        print("#" * (i + 1))

main()        