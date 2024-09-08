import random

def heita_noppaa(tahkot):
  return random.randint(1, tahkot)

def main():
  maksimi_silmaluku = int(input("anna maksimisilmäluku: "))
  while True:
    silmaluku = heita_noppaa(maksimi_silmaluku)
    print(silmaluku)
    if silmaluku == maksimi_silmaluku:
      print(f"sait maksimisilmäluvun {maksimi_silmaluku}!")
      break

if __name__ == "__main__":
  main()