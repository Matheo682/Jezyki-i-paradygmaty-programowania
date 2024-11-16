from EmployeesManager import EmployeesManager

class frontendManager(EmployeesManager):


    name = input("Podaj imię i nazwisko pracownika: ")
    age = int(input("Podaj wiek pracownika: "))
    salary = int(input("Podaj pensję pracownika: "))

    employeesManager = EmployeesManager(name, age, salary)

    employeesManager.info()