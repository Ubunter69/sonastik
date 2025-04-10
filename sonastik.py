import random

# Algne sõnastik
sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

# Funktsioon 1: Tõlge eesti -> vene
def tolgi_est_rus():
    sona = input("Sisesta sõna eesti keeles: ")
    if sona in sonastik:
        print("Tõlge vene keelde:", sonastik[sona])
    else:
        print("Sõna ei leitud sõnastikust.")

# Funktsioon 2: Tõlge vene -> eesti
def tolgi_rus_est():
    sona = input("Sisesta sõna vene keeles: ")
    leitud = False
    for est, rus in sonastik.items():
        if rus == sona:
            print("Tõlge eesti keelde:", est)
            leitud = True
            break
    if not leitud:
        print("Sõna ei leitud sõnastikust.")

# Funktsioon 3: Lisa uus sõna
def lisa_sona():
    est = input("Sisesta uus sõna eesti keeles: ")
    rus = input("Sisesta selle sõna vene tõlge: ")
    if est not in sonastik:
        sonastik[est] = rus
        print("Sõna lisatud!")
    else:
        print("Sõna on juba olemas.")

# Funktsioon 4: Paranda sõna
def paranda_sona():
    vana = input("Sisesta parandatav sõna (eesti keeles): ")
    if vana in sonastik:
        uus = input("Sisesta uus sõna eesti keeles: ")
        uus_tolge = input("Sisesta uus tõlge vene keeles: ")
        del sonastik[vana]
        sonastik[uus] = uus_tolge
        print("Sõna parandatud!")
    else:
        print("Sõna ei leitud.")

# Funktsioon 5: Testi teadmisi
def testi_teadmisi():
    print("Testi teadmisi alustatakse!")
    sonad = list(sonastik.items())
    random.shuffle(sonad)
    oige = 0
    koguarv = len(sonad)

    for est, rus in sonad:
        vastus = input(f"Sisesta vene tõlge sõnale '{est}': ")
        if vastus.strip().lower() == rus.lower():
            print("Õige!")
            oige += 1
        else:
            print(f"Vale! Õige vastus: {rus}")

    protsent = round((oige / koguarv) * 100)
    print(f"Test lõppenud! Sinu tulemus: {protsent}%")

# Peamenüü
def peamenyy():
    while True:
        print("Tere tulemast eesti-vene sõnastikku!")
        print("Valikud:")
        print("1 - Tõlgi eesti -> vene")
        print("2 - Tõlgi vene -> eesti")
        print("3 - Lisa uus sõna")
        print("4 - Paranda sõna")
        print("5 - Testi teadmisi")
        print("6 - Välju")
        valik = input("Tee oma valik: ")

        if valik == "1":
            tolgi_est_rus()
        elif valik == "2":
            tolgi_rus_est()
        elif valik == "3":
            lisa_sona()
        elif valik == "4":
            paranda_sona()
        elif valik == "5":
            testi_teadmisi()
        elif valik == "6":
            print("Head aega!")
            break
        else:
            print("Tundmatu valik. Proovi uuesti.")

