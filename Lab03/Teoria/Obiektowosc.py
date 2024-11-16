class Pojazd:
    def __init__(self, typ):
        self.typ = typ
    def opis(self):
        return f"{self.typ}"

class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def opis(self):
        return f"{self.marka}\t{self.model}\t{self.rok}"

samochod1 = Samochod("Toyota", "Corolla", 2024)
print(samochod1.opis())