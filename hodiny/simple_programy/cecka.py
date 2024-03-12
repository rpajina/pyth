def main (): #oznacime si s ni zacatek programu
    cecka = {
        "Kuba": 3,
        "Vasek": 2,
        "Emka": 0 #za posledni nedavame ,
    }
    jmeno = input("napis jmeno: ").capitalize() #prevede prvni pismeno z inputu vzdycky na velky, aby to vzalo i Emka i emka
    kolik_cecek(cecka, jmeno) #posle do funkcec kolik_cecek dictionary cecka


def kolik_cecek(seznam, jmeno): #ten seznam slouzi jako placeholder cuz ne vzdy tam musi jit ty cecka, definujeme hore
    if jmeno in seznam:
        print(seznam[jmeno])

def pridej_studenta(seznam, jmeno):# jmeno by mohlo byt taky jiny, stejne jako cecka a seznam
    seznam[jmeno] = 1

if __name__ == "__main__": #pousti main jen kdyz je to hlavni kod, abychom mohli kdyztak importovat
    main()