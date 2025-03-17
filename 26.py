# Self Parameter

# self refers to the instance of the class. It is automatically passed with a function call form an object.



class Employee: 
    age = 20  
    language = "Python"

    def getInfo(self):
        print(f"The language is {self.language} and The age is {self.age}")

    @staticmethod # decorator to mark greet as a static method 
    def greet():
        print("Good Morning")

e1 = Employee()   
e1.getInfo()
e1.greet()
