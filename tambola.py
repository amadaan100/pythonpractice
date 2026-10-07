import random

numbers = list(range(1, 91))

print("🎉 Welcome to Tambola! 🎉")
print("Numbers will be called randomly from 1 to 90.")
print("Type 'q' to stop the game.\n")

called_numbers = []

while len(called_numbers) < 90:

    user_input = input("Press Enter to call the next number: ")

    if user_input.lower() == "q":
        print("Game ended!")
        break

    number = random.choice(numbers)

    numbers.remove(number)
    called_numbers.append(number)

    print("🎱 Number called:", number)
    print("Numbers called so far:", called_numbers)
    print()
    
if len(called_numbers) == 90:
    print("All 90 numbers have been called!")