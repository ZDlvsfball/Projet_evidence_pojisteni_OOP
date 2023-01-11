from data import *


class Pojistenec:
    """Trída definující informace o pojištěnci"""
    def __init__(self,jmeno,prijmeni,vek,telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return str(f">>> {self.jmeno} {self.prijmeni}, {self.vek}, {self.telefon} <<<")

    def hledac(self,jmeno,prijmeni):
        self.jmeno = input("Zadejte jméno:\n")
        self.prijmeni = input("Zadejte příjmení")
        if self.jmeno in seznam_pojistenych:
            print("Je tu")
        else:
            print("Není tu")

