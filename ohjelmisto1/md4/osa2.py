while True:
    inch = float(input("tuumien määrä (negatiivinen numero sammuttaa) "))
    if inch < 0:
        break

    cm = inch * 2.54
    print(f"{inch} tuumaa on {cm:.2f} senttimetriä.")