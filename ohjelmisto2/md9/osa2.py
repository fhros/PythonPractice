class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        self.nopeus = max(0, min(uusi_nopeus, self.huippunopeus))

if __name__ == "__main__":
    auto1 = Auto("ABC-123", 142)

    print("rekisteritunnus:", auto1.rekkari)
    print("huippunopeus:", auto1.huippunopeus, "km/h")
    print("tämänhetkinen nopeus:", auto1.nopeus, "km/h")
    print("autolla on ajettu:", auto1.matka, "km")

    auto1.kiihdyta(30)
    auto1.kiihdyta(70)
    auto1.kiihdyta(50)
    print("nopeus kiihdytysten jälkeen:", auto1.nopeus, "km/h")

    auto1.kiihdyta(-200)
    print("nopeus hätäjarrutuksen jälkeen:", auto1.nopeus, "km/h")