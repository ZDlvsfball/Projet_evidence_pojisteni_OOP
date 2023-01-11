from info import *


seznam_pojistenych = []















def nacti_cislo(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo = float(input(text_zadani))
            if cislo > 4:
                print(text_chyba)
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo

def nacti_vek_a_telefon(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo =int(input(text_zadani))

            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo


def pridani_uzivatele():

        # jméno
        jmeno_zad_uzi = input("Zadejte jméno pojištěného:\n")
        nove_jmeno = jmeno_zad_uzi.lower().capitalize().strip()
        # příjmení
        prijmeni_zad_uzi = input("Zadejte přijmení:\n")
        nove_prijmeni = prijmeni_zad_uzi.lower().capitalize().strip()
        # věk
        nove_vek = nacti_vek_a_telefon("Zadejte váš věk:\n","Špatný formát!")
        # telefon
        nove_telefon = nacti_vek_a_telefon("Zadejte vaše telefoní číslo bez + 420:\n", "Špatný formát")

        print("Data byla uložena, děkujeme.")
        novy_pojistenec=Pojistenec(nove_jmeno,nove_prijmeni,nove_vek,nove_telefon)
        print(novy_pojistenec)
        seznam_pojistenych.append(novy_pojistenec)

def vyhledavac():

    x = input("Zadejte jméno hledané osoby:\n")
    hledane_jmeno = x.lower().capitalize().strip()
    y = input("Zadejte přijmení:\n")
    hledane_prijmeni = y.lower().capitalize().strip()
    result = next(obj for obj in seznam_pojistenych if obj.jmeno == hledane_jmeno)
    print(result)




def vypis():
    for i in seznam_pojistenych:
        print(i)
