# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

kanta_str = input("Suorakulmion kanta: ")
korkeus_str = input("Suorakulmion korkeus: ")
kanta = float(kanta_str)
korkeus = float(korkeus_str)

piiri = (kanta+korkeus)*2
print("Suorakulmion piiri on: " + str(piiri))
pintaAla = kanta*korkeus
print("Suorakulmion pinta ala on: " + str(pintaAla))