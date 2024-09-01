import random

ihme_luku = random.randint(1, 10)

print("arvaa luku 1-10.")

while True:
    arvaus = int(input("anna numero: "))

    if arvaus < ihme_luku:
        print("liian pieni arvaus")
    elif arvaus > ihme_luku:
        print("liian suuri arvaus")
    else:
        print("voitit pelin!")
        break