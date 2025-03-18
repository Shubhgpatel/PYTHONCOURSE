# Multiple Inheritance 

class Employee: # Base class
    company = "Google"

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language {self.language}")


class Programmer(Employee,Coder): # Derived class
    company = "Microsoft"
    def showLanguages(self):
        print(f"The company name is {self.company} and he good with {self.language} language")

a = Employee("Shubh",120000)
b = Programmer("Het",120000)

a.show()
b.show()
b.printLanguages()
b.showLanguages()

