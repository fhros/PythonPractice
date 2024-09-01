import random

iterator = 0
N = float(input("pisteiden määrä:"))
n = 0
while iterator < N:
    iterator += 1
    x = random.random() * 2 - 1
    y = random.uniform(-1, 1)
    print(f"{x}, {y}")
    if x**2 + y**2 < 1:
        print("sisällä")
        n = n + 1
    else:
        print("ulkona")
print(f"{N} pisteestä {n} osui")
result = 4 * n / N
print(f"likiarvo on {result:.2f}")