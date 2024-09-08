import random

def main():
  while True:
    silmaluku = random.randint(1, 6)
    print(silmaluku)
    if silmaluku == 6:
      print("sait kuusi")
      break

if __name__ == "__main__":
  main()