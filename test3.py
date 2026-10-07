def main():
    x = get_int("whats's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not an integer. Please try again.")
        else:
            pass

main()