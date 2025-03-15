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


# Function with arguments

def GoodMorning(name):
    print("Good Morning", name)

GoodMorning("Shubh")


# this function will return the factorial of the number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


num = int(input("Enter the number :"))
print("The facttorial of the number is :", factorial(num))


# this function will return the sum of the numbers
def sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum(n-1)

num = int(input("Enter the number : "))
print("The sum of the numbers is :", sum(num))
    

# this function will convert the inches to cm
def inch_cm(inch):
    return inch * 2.54

n = int(input("Enter the number in inches : "))
print(f"The number in cm is : {inch_cm(n)} cm")


# this function will remove the word and also strip the word from the list
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Shubh","Rohan","Shubham","an"]
print(rem(l, "an"))
