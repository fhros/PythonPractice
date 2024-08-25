vuosi = int(input("Anna vuosi: "))

def onko_karkausvuosi(vuosi):
    if vuosi % 4 == 0:
        if vuosi % 100 == 0:
            return vuosi % 400 == 0
        else:
            return True
    else:
        return False

if onko_karkausvuosi(vuosi):
  print(f"Vuosi {vuosi} on karkausvuosi.")
else:
  print(f"Vuosi {vuosi} ei ole karkausvuosi.")