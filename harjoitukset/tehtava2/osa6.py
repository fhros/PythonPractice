# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia

import random

kolminumeroinen_koodi = "".join([str(random.randint(0, 9)) for _ in range(3)])

nelinumeroinen_koodi = "".join([str(random.randint(1, 6)) for _ in range(4)])

print("Kolminumeroinen koodi:", kolminumeroinen_koodi)
print("Nelinumeroinen koodi:", nelinumeroinen_koodi)