class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"julkaisu: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjoittaja: {self.kirjoittaja}")
        print(f"sivuja: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittaja: {self.toimittaja}")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_n6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
print()
hytti_n6.tulosta_tiedot()