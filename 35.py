a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero") # this way you can also raise an error 
else:
    print(f"The division a/b is {a/b}")