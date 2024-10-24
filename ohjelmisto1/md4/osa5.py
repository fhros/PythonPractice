oikea_kayttajatunnus = "python"
oikea_salasana = "rules"
yritykset = 0

while yritykset < 5:
    kayttaja = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset += 1

    if kayttaja == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")

if yritykset == 5:
    print("Pääsy evätty.")