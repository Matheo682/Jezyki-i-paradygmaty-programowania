import json
from EmployeesManager import EmployeesManager
from Employee import Employee

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()
        self.logged_in = False

    def login(self):
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        if username == "admin" and password == "admin":
            self.logged_in = True
            print("Zalogowano pomyślnie.")
        else:
            print("Nieprawidłowa nazwa użytkownika lub hasło.")

    def add_employee(self):
        if not self.logged_in:
            print("Musisz się zalogować, aby dodać pracownika.")
            return
        name = input("Podaj imię i nazwisko pracownika: ")
        try:
            age = int(input("Podaj wiek pracownika: "))
            salary = int(input("Podaj pensję pracownika: "))
            if age < 0 or salary < 0:
                raise ValueError("Wiek i pensja muszą być nieujemne.")
        except ValueError as e:
            print(f"Błąd walidacji danych: {e}")
            return
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)
        self.manager.save_to_file()

    def list_employees(self):
        if not self.logged_in:
            print("Musisz się zalogować, aby wyświetlić listę pracowników.")
            return
        self.manager.load_from_file()
        self.manager.list_employees()

    def remove_employees_by_age_range(self):
        if not self.logged_in:
            print("Musisz się zalogować, aby usunąć pracowników.")
            return
        try:
            min_age = int(input("Podaj minimalny wiek: "))
            max_age = int(input("Podaj maksymalny wiek: "))
            if min_age < 0 or max_age < 0:
                raise ValueError("Wiek musi być nieujemny.")
        except ValueError as e:
            print(f"Błąd walidacji danych: {e}")
            return
        self.manager.remove_employees_by_age_range(min_age, max_age)
        self.manager.save_to_file()

    def update_salary_by_name(self):
        if not self.logged_in:
            print("Musisz się zalogować, aby zaktualizować wynagrodzenie pracownika.")
            return
        name = input("Podaj imię i nazwisko pracownika: ")
        try:
            new_salary = int(input("Podaj nowe wynagrodzenie: "))
            if new_salary < 0:
                raise ValueError("Wynagrodzenie musi być nieujemne.")
        except ValueError as e:
            print(f"Błąd walidacji danych: {e}")
            return
        self.manager.update_salary_by_name(name, new_salary)
        self.manager.save_to_file()

if __name__ == "__main__":
    frontend = FrontendManager()
    while True:
        print("\n1. Zaloguj się")
        print("2. Dodaj pracownika")
        print("3. Wyświetl listę pracowników")
        print("4. Usuń pracowników w przedziale wiekowym")
        print("5. Zaktualizuj wynagrodzenie pracownika")
        print("6. Wyjdź")
        choice = input("Wybierz opcję: ")
        if choice == '1':
            frontend.login()
        elif choice == '2':
            frontend.add_employee()
        elif choice == '3':
            frontend.list_employees()
        elif choice == '4':
            frontend.remove_employees_by_age_range()
        elif choice == '5':
            frontend.update_salary_by_name()
        elif choice == '6':
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")