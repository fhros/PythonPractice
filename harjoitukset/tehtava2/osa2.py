# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

sade_str = input("Ympyrän säde: ")
sade = float(sade_str)
pintaAla = 3.14*sade**2
print("Ympyrän pinta-ala on " + str(pintaAla) + "")