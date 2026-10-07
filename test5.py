import random

#number = random.randint(1, 100)
#print(number)

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)
