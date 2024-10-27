import random

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        self.nopeus = max(0, min(uusi_nopeus, self.huippunopeus))

    def kulje(self, tunnit):
        matka = self.nopeus * tunnit
        self.matka += matka

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:

            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailun {self.nimi} tilanne:")
        print("rekisteritunnus\t huippunopeus\t nykyinen nopeus\t kuljettu matka")
        for auto in autot:
            print(f"{auto.rekkari}\t\t{auto.huippunopeus}\t\t{auto.nopeus}\t\t{auto.matka}")

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)

if __name__ == "__main__":
    autot = []
    for i in range(1, 11):
        huippunopeus = random.randint(100, 200)
        rekisteritunnus = f"ABC-{i}"
        autot.append(Auto(rekisteritunnus, huippunopeus))

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()


    print("Kilpailu päättyi!")
    kilpailu.tulosta_tilanne()