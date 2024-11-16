class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print(f"{self.name}\nWiek: {self.age}\nWynagrodzenie: {self.salary}")
