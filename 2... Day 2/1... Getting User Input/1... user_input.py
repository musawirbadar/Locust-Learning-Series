print("Name print with Concatination +")
name = input("Enter your name: ")
print("Hello, " + name ) # The + tells Python to join the two parts into a single string.

"""
"Hello, " is a string.
name is a variable that holds a string (e.g., "Musawir").
Using + combines both into one message.
"""
print("Another example of print name with concatination +")
name = input("Enter your name: ")
print("Hello, " + name + "!" ) # the + operator is used for string concatenation, meaning it joins multiple strings together into one.

"""
"Hello, " → A string
name → A variable containing a string (e.g., "Musawir")
"!" → Another string
"""
print("Print name with recommended method f-string")
name = input("Enter your name: ")
print(f"Hello, {name} !") #using f-strings (Recommended)

print("Print name with comma seperation method")
name = input("Enter your name: ")
print("Hello,", name,"!")

