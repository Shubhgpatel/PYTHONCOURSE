print("Shubh is a good boy\nand also he is a good programmer")
#\n is used to print the next line in the output.
# \t is used to print the tab space in the output.
name = input("Enter your name: ")
print(f"Good Afternoon, {name}") # this is called f-string.
# f-string is used to print the value of the variable inside the string.
letter = '''Dear <|NAME|> 
You are selected!
<|Date|>'''
print(letter.replace("<|NAME|>", "Shubh").replace("<|Date|>", "20-07-2021")) # replace function is used to replace the given string with the given string this is called chaining of functions.
