from abc import ABC, abstractmethod

class Zwierze(ABC):
    @abstractmethod
    def dzwiek(self):
        pass

class Pies(Zwierze):
    def dzwiek(self):
        return "pies szczeka"

pies = Pies()
print(pies.dzwiek())