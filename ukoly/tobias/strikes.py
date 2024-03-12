import csv

strikes = {
    "Božetěch": 1,
    "Želmíra": 3,
    "Andělín": 2,
    "Hvězdoslava": 1
}

path = "H:\\python\\ukoly\\tobias\\data.csv"
with open(path, "a", newline="") as file:
    file.write(strikes)