from os import system

system("cls")

# 4.feladat prog_alapf.5

elsoSzam = int(input("Kérem az első számot: "))
masodikSzam = int(input("Kérem az második számot: "))

logikaikifejezes_1 = elsoSzam < masodikSzam
logikaikifejezes_2 = masodikSzam < masodikSzam

if logikaikifejezes_1:
    kiir =f"A második szám: {masodikSzam} a nagyobb."
    print(kiir)
elif logikaikifejezes_2:
    kiir =f"Az első szám: {elsoSzam} a nagyobb."
    print(kiir)
else:
    kiir = "A kétszám egyenlő"
    print(kiir)