import math

def laske_hinta(halkaisija, hinta):

  sade = halkaisija / 200
  pinta_ala = math.pi * sade**2
  yksikkohinta = hinta / pinta_ala
  return yksikkohinta

def main():
  halkaisija1 = float(input("ekan pizzan halkaisija (cm): "))
  hinta1 = float(input("ekan pizzan hinta (€): "))
  halkaisija2 = float(input("tokan pizzan hinta halkaisija (cm): "))
  hinta2 = float(input("tokan pizzan hinta (€): "))

  yksikkohinta1 = laske_hinta(halkaisija1, hinta1)
  yksikkohinta2 = laske_hinta(halkaisija2, hinta2)

  if yksikkohinta1 < yksikkohinta2:
    print("eka pizza on halvempi")
  elif yksikkohinta1 > yksikkohinta2:
    print("toka pizza on halvempi")
  else:
    print("pizzat ovat yhtä kalliita")

if __name__ == "__main__":
  main()