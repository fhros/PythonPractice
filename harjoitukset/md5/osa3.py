def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("anna numero: "))
if is_prime(num):
    print(f"{num} on alkuluku.")
else:
    print(f"{num} ei ole alkuluku.")