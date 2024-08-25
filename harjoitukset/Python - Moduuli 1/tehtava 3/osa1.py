alamittaRaja = 37

kuha = float(input("Kuhan pituus: "))

alinSallittu = alamittaRaja - kuha

if kuha <= alamittaRaja:
    print(f"Heitä kuha järveen. Se on {alinSallittu:.0f}cm liian lyhyt")
else:
    print("Kuha on tarpeeksi iso")