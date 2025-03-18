# SUPER() METHOD 

class Employee():
    def __init__(self):
        print("Constructor of Employee")
   

class Programmer(Employee):
    def __init__(self):
        super().__init__()  # this calls the Employee class constructor
        print("Constructor of Programmer")
    

class Manager(Programmer):
    def __init__(self):
        super().__init__() # this calls the Programmer class constructor 
        print("Constructor of Manager")
    
a = Manager()
