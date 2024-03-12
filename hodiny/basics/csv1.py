import csv #abychom mohli pracovat s csvckem
#path = "H:\\python\\hodiny\\basics\\data.csv"
#with open(path, "r") as f:
    #reader = csv.reader(f, delimiter=";")
    #volame reader z imprtu csv, ze cteme to f, delimiterem dame cim oddelujeme takze ";"
    #for x in reader:
        #print(x)

path = "H:\\python\\hodiny\\basics\\data.csv"
with open(path, "a", newline="") as f:
     # "a" prida novy radek, nic jinyho kdyztak nemenime, muzeme i w zas newline je pro hezky radkovani
    jmeno = input("zadej jmeno: ")
    pocet = int(input("zadej pocet: "))
    writer = csv.writer(f, delimiter=";")
    writer.writerow([jmeno, pocet])
