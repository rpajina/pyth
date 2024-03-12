def main (): 
    bludistaci = {
   "Božetěch": 1,
   "Želmíra": 3,
   "Andělín": 2,
   "Hvězdoslava": 1
}
    yess = input("chces vypsat vsechny bludistaky?: ")
    vsichni_bludistaci(bludistaci, yess) 


def vsichni_bludistaci(seznam, yess): 
    if yess == "ano":
        for jmeno, pocet in seznam.items():
            print(jmeno, pocet)

if __name__ == "__main__":
    main()