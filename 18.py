# Functions in python are defined using the keyword def, followed by a function name, a signature within parentheses (), and a colon :. The following code, with one additional level of indentation, is the function body.

# When a program gets bigger in size and its compelxity grows, functions are used to make the code more readable and manageable.

# Functions are used to perform a specific task. You can use the same function many times in your program. You can also pass data, known as parameters, into a function.

def avg():
    a = int(input("Enter the number 1 : "))
    b = int(input("Enter the number 2 : "))
    c = int(input("Enter the number 3 : "))

    average = (a+b+c)/3
    print("The average of the numbers is : ", average)

avg()