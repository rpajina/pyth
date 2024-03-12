with open("H:\\python\\hodiny\\basics\\data.txt", "r") as file:
    print(file.read()) # .read() nam vypise soubor
 # cestu muzeme ulozit i pod promennou
# potrebuje co ma otevrit (cesta cela, v uvozovkach, zdvojeny lomitka u windowsu + co chceme "r" read)

with open("H:\\python\\hodiny\\basics\\data.txt", "a") as file:
    # "w" prepise cely soubor, "a" prida na posledni radek
    text = "\nBye" #\n nam to odradkuje
    file.write(text) # .write(text) zapise (text) do souboru