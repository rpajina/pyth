import random  ##choosneme z knihovny kod pro random

##random cislo vybere v rozsahu 1-10
"""
odpoved = random.randint(1, 7)

if odpoved == 1:
  print("Ano")
elif odpoved == 2:
  print("stopro")
elif odpoved == 3:
  print("no jiste")
elif odpoved == 4:
  print("mozna")
elif odpoved == 5:
  print("nemyslim si")
elif odpoved == 6:
  print("ne")
elif odpoved == 7:
  print("zkus to znovu")
"""
while True:
  odpoved = random.randint(0, 6)
  otazka = input("Jaká je tvá otázka?\n")
  if input == "konec":
    break
  odpovedi = [
      "ano", "ne", "mozna", "no jiste", "stopro", "nemyslim si",
      "zkus to znova"
  ]
  print(odpovedi[odpoved])
  if input == "konec":
    break
