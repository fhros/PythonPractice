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

class Sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akku):
        super().__init__(rekkari, huippunopeus)
        self.akku = akku

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, tankin_koko):
        super().__init__(rekkari, huippunopeus)
        self.tankin_koko = tankin_koko

# Pääohjelma
auto1 = Sähköauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

auto1.kiihdyta(120)
auto2.kiihdyta(110)

auto1.kulje(3)
auto2.kulje(3)

print(f"{auto1.rekkari} on ajanut {auto1.matka} km.")
print(f"{auto2.rekkari} on ajanut {auto2.matka} km.")