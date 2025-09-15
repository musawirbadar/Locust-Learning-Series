#Defining a Function
def greet(): # Keyword "def" is used to define a function
    print("Hello, Welcome to Python Functions")
greet() # Call it with the function name 

# Functions with Single Parameter
def greet_user(name): # name is the function parameter here
    print("Hello",name) # Passing parameter to print

greet_user("Syed") # Function call with argument Syed
greet_user("Musawir") # Function call with argument Musawir
greet_user("Badar") # Functiona call with argumen Badar

# Function with multi Parameters
def add (a,b):
    sum = a+b
    print("Sum of two numbers are:",sum)

add(5,7)
add(9,8)
add(234,67)

# Function with Return Values
def addition(a,b):
    return a+b # returns 99 after adding
result = addition(23,76) # Added value 99 stored in the result because of return
print("Addition of these two numbers will be",result) 
print("Double of added numbers will be: ",result * 2) 

# result have the added value 99 just becasue of return so it can be use multiple times
# Return send value back to caller so you can store it, reuse it, do further things.
# But in Parameter, results are being shown directly through print. You can't use add somewhere else
# Or you can't store "add" in variable like total = add(5,12) and then reuse total.

