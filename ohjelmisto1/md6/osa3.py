def main():
    while True:
        gallona = float(input("anna galloona määrä (negatiivinen luku lopettaa): "))
        if gallona < 0:
            break
        litrat = gallona * 3.785
        print(f"{gallona} gallonaa on {litrat:.2f} litraa.")

if __name__ == "__main__":
  main()