def main (): 
    bludistaci = {
   "Božetěch": 1,
   "Želmíra": 3,
   "Andělín": 2,
   "Hvězdoslava": 1
}
    jmeno = input("pridej studenta: ").capitalize()
    pridej_studenta(bludistaci, jmeno) 

def pridej_studenta(seznam, jmeno):
    seznam[jmeno] = 1
    print(jmeno, seznam[jmeno])

if __name__ == "__main__":
    main()