class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

if __name__ == "__main__":
    auto1 = Auto("ABC-123", 142)

    print("rekisteritunnus:", auto1.rekkari)
    print("huippunopeus:", auto1.huippunopeus, "km/h")
    print("tämänhetkinen nopeus:", auto1.nopeus, "km/h")
    print("autolla on ajettu:", auto1.matka, "km")