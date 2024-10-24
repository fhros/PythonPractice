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

def main():
    autot = []
    for i in range(1, 11):
        huippunopeus = random.randint(100, 200)
        rekisteritunnus = f"ABC-{i}"
        autot.append(Auto(rekisteritunnus, huippunopeus))

    kilpailu_keskeytyy = False
    tunnit = 0
    while not kilpailu_keskeytyy:
        tunnit += 1
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

        kilpailu_keskeytyy = any(auto.matka >= 10000 for auto in autot)

    print("tulokset:")
    print("rekisteritunnus\t huippunopeus\t nykyinen nopeus\t kuljettu matka")
    for auto in autot:
        print(f"{auto.rekkari}\t\t{auto.huippunopeus}\t\t{auto.nopeus}\t\t{auto.matka}")

if __name__ == "__main__":
    main()