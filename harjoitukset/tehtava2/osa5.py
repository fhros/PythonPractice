# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3

kilogrammat = grammat // 1000
grammat = grammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat:.0f} kilogrammaa ja {grammat:.2f} grammaa.")