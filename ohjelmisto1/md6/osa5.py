def poista_parittomat(lukulista):

  parilliset_luvut = []
  for luku in lukulista:
    if luku % 2 == 0:
      parilliset_luvut.append(luku)
  return parilliset_luvut

def main():
  alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7]

  karsittu_lista = poista_parittomat(alkuperainen_lista)

  print("alkuperäinen lista:", alkuperainen_lista)
  print("karsittu lista:", karsittu_lista)

if __name__ == "__main__":
  main()