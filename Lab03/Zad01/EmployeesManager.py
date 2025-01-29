import json
from Employee import Employee

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for employee in self.employees:
            employee.info()

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [employee for employee in self.employees if not (min_age <= employee.age <= max_age)]

    def find_employee_by_name(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def update_salary_by_name(self, name, new_salary):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary

    def save_to_file(self, filename="employees.json"):
        with open(filename, 'w') as file:
            json.dump([employee.__dict__ for employee in self.employees], file)

    def load_from_file(self, filename="employees.json"):
        try:
            with open(filename, 'r') as file:
                employees_data = json.load(file)
                self.employees = [Employee(**data) for data in employees_data]
        except FileNotFoundError:
            self.employees = []