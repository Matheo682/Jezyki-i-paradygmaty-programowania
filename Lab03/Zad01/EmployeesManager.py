from Employee import Employee

class EmployeesManager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)


    def info(self):
        super().info()

