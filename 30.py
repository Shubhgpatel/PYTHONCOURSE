# Inheritance in python 

class Employee: # Base class
    company = "Google"

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee): # Derived class
    company = "Microsoft"


a = Employee("Shubh",120000)
b = Programmer("het",120000)

a.show()
b.show()