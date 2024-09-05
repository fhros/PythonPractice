luvut = []

while True:
    luku = input("anna luku (tyhjä rivi lopettaa): ")
    if not luku:
        break
    try:
        luku = float(luku)
        luvut.append(luku)
    except ValueError:
        print("virheellinen syöte anna numero")

luvut.sort(reverse=True)

print("viisi suurinta lukua:")
for i in range(min(5, len(luvut))):
    print(int(luvut[i]))