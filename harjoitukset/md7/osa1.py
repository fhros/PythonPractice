vuodenajat = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

kuukausi = int(input("anna kuukauden numero (1-12): "))

for i in range(len(vuodenajat)):
  if kuukausi in vuodenajat[i]:
    vuodenaika = ["talvi", "kevät", "kesä", "syksy"][i]
    break

print(f"kuukausi {kuukausi} on {vuodenaika}.")