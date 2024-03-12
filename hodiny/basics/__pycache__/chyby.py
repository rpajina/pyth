
import sys #importujeme nejakej sys co nam to umozni lip ovladat
def kladne_zaporne(x):
    if x > 0:
        print("cislo je kladne")
    elif x < 0:
        print("cislo je zaporne")
    else:
        print("cislo je 0")

while True: #opakuje try dokud ja to nezadam sprave
    try: #zkousime tim ci to facha, dame sem vse co by nam mohlo hazet chyby
        number = int(input("zadej cislo: ")) #kdyz najde chybu, nepokracuje dal v try a jde na except
        kladne_zaporne(number) #kdyz facha, program bezi normalne
    except KeyboardInterrupt:
        print("program manualne ukoncen")
        sys.exit() #kdyz error KeyboardInterrupt tak se pomoci toho sys.exit() ukonci program
    except ValueError: #kdyz to nefacha (konkretne kdyz chyba ValueError), vypise ze je "chceme cislo vole"
                       #musi se tam davat ten konkretni error bo to nebere pak ctrl+c ^C a hodi nam to tu chybovou hlasku
        print("chceme cislo vole") #tuto muzeme dat i to aby nas to vratilo na "zadej cislo", uzivatelovi to rekne co je blbe
    else: #provede se, kdyz to funguje bez chyby, nefunguje ve while kdyz to breakneme pred tim
        print("yep facha to")
        break #kdyz se kod vykona dobre tak se to zastavi 
              #muzeme ho dat i k try ale to se pak neudela else bo se to zastavi uz predtim
    finally:
        print("nejako to probehlo") #finally se vypise upe pokazdy