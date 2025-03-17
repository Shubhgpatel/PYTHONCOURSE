# __init__() constructor 
# __init__() is a special method which is first run as soon as the object is created.

class Employee: 
    age = 20  
    language = "Python"

    # Dunder Methods are methods that start and end with double underscores (__).
    # They are automatically called by Python in specific situations.
    def __init__(self, name , age , language):
        self.name = name
        self.age = age
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language} and The age is {self.age}")

    @staticmethod # decorator to mark greet as a static method 
    def greet():
        print("Good Morning")

e1 = Employee("Shubh",30,"Java") 
print(e1.name,e1.age,e1.language)
e1.getInfo()
e1.greet()