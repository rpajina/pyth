kocka = {"barva": "cerna",
         "jméno": "cici",
         "oblibene_jidlo": ["granulky","broucci"],
         "povaha":"spici",
         "pocet_nohou": 4,
         "zije": True, #klic musi byt string, to druhy cokoliv
         }
print(kocka["jméno"]) #vypise jméno za dvojteckou ze slovniku kocka
print(kocka["oblibene_jidlo"] [1])

for jidlo in kocka["oblibene_jidlo"]:
    print(jidlo)

telefonni_seznam = {
    "hvezdoslava": "159 357 852",
    "kamil": "254 652 987",
    "jarmilka": "+39 025 468 917",
}