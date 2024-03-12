#for x in range(po kolika, do kolika, po kolika):
for x in range(5):
  print(x)

seznam = ["hrusky", "hranolky", "tortila", "ryze"]

for jidlo in seznam:
  print(jidlo,
        end="...")  #end nam urci kdyz chceme koncit necim jinym nez entrem

print()  #abychom nezacinali dalsi print hned za ...

slovo = "slovo"
print(slovo[0])

for pismeno in slovo:
  print(pismeno)

print(seznam[0][0])

for i, polozka in enumerate(
    seznam):  #enumerate nam da pristup k i jakozdo pocitadlu
  print(i + 1, polozka)  #i+1 zacneme od jednicky a ne od 0