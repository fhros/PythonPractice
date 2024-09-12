nimi_joukko = set()

while True:
    nimi = input("nimi laita(tyhjä lopettaa): ")
    if not nimi:
        break

    if nimi in nimi_joukko:
        print("oot laittanu tän jo")
    else:
        nimi_joukko.add(nimi)
        print("uus nimi lisätty")

print("\nnimet:")
for nimi in nimi_joukko:
    print(nimi)