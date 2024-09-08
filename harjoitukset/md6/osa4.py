def laske_summa(lukulista):
  summa = 0
  for luku in lukulista:
    summa += luku
  return summa

def main():
  luvut = [1, 2, 3, 4, 5]

  tulos = laske_summa(luvut)

  print("lukujen summa:", tulos)

if __name__ == "__main__":
  main()