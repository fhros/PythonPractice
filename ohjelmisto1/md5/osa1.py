import random

nopat = int(input("anna noppien määrä:"))
summa = 0

for _ in range(nopat):
    noppaluku = random.randint(1,6)
    summa += noppaluku

print(f"noppien summa on {summa}")