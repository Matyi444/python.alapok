








# 2.feladat prog_alapf.3

#explicit típuskonverzió
szam = (input("Kérek egy számot: "))
kiir = f"A szám: {szam} és kétszerese: {2 * szam}"

print(kiir)

# 3.feladat prog_alapf.4

elsoSzam = int(input("Kérem az eső számot: "))
masodikSzam = int(input("Kérem az második számot: "))

osszeg = elsoSzam + masodikSzam
kulonbseg = elsoSzam - masodikSzam
szorzat = elsoSzam * masodikSzam 
hanyados = elsoSzam / masodikSzam

kiir = f"Két szám: {elsoSzam}, {masodikSzam}"
kiir = kiir + f"\nösszeg: {osszeg}"
kiir = kiir + f"\nkülönbség: {kulonbseg}"
kiir = kiir + f"\nszorzat: {szorzat}"
kiir = kiir + f"\nhányados: {hanyados}"

print(kiir)