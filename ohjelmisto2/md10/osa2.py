class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def mene_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros != kohde_kerros:
            if self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(1, hissien_lkm + 1):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if 1 <= hissi_numero <= len(self.hissit):
            print(f"hissi {hissi_numero} meni kerrokseen {kohde_kerros}")
            self.hissit[hissi_numero - 1].mene_kerrokseen(kohde_kerros)
        else:
            print("miten sait tän lol")

if __name__ == "__main__":
    talo = Talo(1, 10, 2)

    talo.aja_hissia(2, 7)

    talo.aja_hissia(1, 4)