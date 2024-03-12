def main (): 
    bludistaci = {
   "Božetěch": 1,
   "Želmíra": 3,
   "Andělín": 2,
   "Hvězdoslava": 1
}
    jmeno = input("napis jmeno: ").capitalize()
    kolik_bludistaku(bludistaci, jmeno) 


def kolik_bludistaku(seznam, jmeno): 
    if jmeno in seznam:
        print(seznam[jmeno])


if __name__ == "__main__":
    main()