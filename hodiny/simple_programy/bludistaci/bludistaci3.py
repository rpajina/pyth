def main (): 
    bludistaci = {
   "Božetěch": 1,
   "Želmíra": 3,
   "Andělín": 2,
   "Hvězdoslava": 1
}
    jmeno = input("komu ches pridat bludistaka?: ").capitalize()
    pridej_bludistaka(bludistaci, jmeno) 


def pridej_bludistaka(seznam, jmeno): 
    if jmeno in seznam:
        seznam[jmeno] += 1
        print(jmeno, seznam[jmeno])

if __name__ == "__main__":
    main()
