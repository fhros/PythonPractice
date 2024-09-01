numerot = []


while True:
    inputnumberthing = input("anna numero (älä laita mitään ja paina enter niin ohjelma loppuu): ")
    if not inputnumberthing:
        break
    try:
        luku = float(inputnumberthing)
        numerot.append(luku)
    except ValueError:
        print("outo numero tai jtn")
if numerot:
    pienin = min(numerot)
    suurin = max(numerot)
    print(f"pienin luku: {pienin}")
    print(f"suurin luku: {suurin}")
else:
    print("ei numero")