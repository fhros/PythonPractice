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
            print(f"hissi meni kerrokseen {self.nykyinen_kerros}")
        else:
            print("oot jo ylimmäs kerrokses")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"hissi meni kerrokseen {self.nykyinen_kerros}")
        else:
            print("oot jo alimmas kerrokses")

if __name__ == "__main__":
    h = Hissi(1, 10)
    h.mene_kerrokseen(5)
    h.mene_kerrokseen(1)