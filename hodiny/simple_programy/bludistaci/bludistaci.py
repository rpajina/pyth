import csv, sys


def main():
    bludistaci = {}

    nacist_data(bludistaci)

    print("ahoj")
    print("zvol si moznost:")
    print("pro vypsani vsech bludistaku zvol 1")
    print("pro vypsani jednoho studenta zvol 2")
    print("pro pridani bludistaka zvol 3")
    print("pro odebrani bludistaka zvol 4")
    print("pro pridani studenta zvol 5")
    print("pro ukonceni programu zvol 6")

    while True:
        try:
            zvolena_moznost = int(input())
            break
        except ValueError:
            print("zadej cislo blbecku")

    match zvolena_moznost:
        case 1:
            vsichni_bludistaci(bludistaci)
        case 2:
            kolik_bludistaku(bludistaci)
        case 3:
            pridej_bludistaka(bludistaci)
        case 4:
            odeber_bludistaka(bludistaci)
        case 5:
            pridej_studenta(bludistaci)
        case 6:
            print("papa")
            sys.exit()
        case _:
            print("vypis cislo mezi 1-6")


def kolik_bludistaku(bludistaci):
    jmeno = input("napis jmeno: ").capitalize()
    print(jmeno, bludistaci[jmeno])


def vsichni_bludistaci(bludistaci):
    yess = input("chces vypsat vsechny bludistaky?: ")
    if yess == "ano":
        for jmeno, pocet in bludistaci.items():
            print(jmeno, pocet)


def pridej_bludistaka(bludistaci):
    jmeno = input("komu ches pridat bludistaka?: ").capitalize()
    if jmeno in bludistaci:
        bludistaci[jmeno] += 1
        print(jmeno, bludistaci[jmeno])


def odeber_bludistaka(bludistaci):
    jmeno = input("komu ches odebrat bludistaka?: ").capitalize()
    if jmeno in bludistaci:
        bludistaci[jmeno] -= 1
        print(jmeno, bludistaci[jmeno])


def pridej_studenta(bludistaci):
    jmeno = input("pridej studenta: ").capitalize()
    bludistaci[jmeno] = 1
    print(jmeno, bludistaci[jmeno])


def ulozit_data(bludistaci):
    with open("H:\\python\\ukoly\\bludistaci\\data_b.csv", "r", newline="") as file:
        writer = csv.writer(file, delimiter=";")

        for name, number in bludistaci.items():
            writer.writerow([name, number])


def nacist_data(bludistaci):
    with open("H:\\python\\ukoly\\bludistaci\\data_b.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")

        for lines in reader:
            bludistaci[lines[0]] = int(lines[1])


if __name__ == "__main__":
    main()
