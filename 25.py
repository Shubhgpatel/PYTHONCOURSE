# Note : Instance attributes take preference over class attirbute during assignment and retrival.

class Employee: 
    age = 20  
    language = "Py" # class attribute 

e1 = Employee() 
e1.language = "Javascript" # instance attiribute
print(e1.age,e1.language)


