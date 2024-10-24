lentoasemat = {}

while True:
    valinta = input("1 = uusi, 2= haku, 3 = lopeta: ")

    if valinta == "1":
        icao = input("anna icao koodi: ")
        nimi = input("anna nimi: ")
        lentoasemat[icao] = nimi
        print("succces")

    elif valinta == "2":
        haku = input("anna icao hkoodi: ")
        if haku in lentoasemat:
            print(f"nimi on {lentoasemat[icao]}")
        else:
            print(f'Tämä kyseinen "{haku}" ICAO-Koodi ei ole databasessa.')

    elif valinta == "3":
        print("Goodbye.")
        break

    else:
        print("wrong")