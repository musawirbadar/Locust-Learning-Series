print("Print age using f-string method")
age = int(input("Enter your age: ")) # By using "int" its number now, 
                                     # enter string as input throws error 
print(f"In 5 years, your age will be {age + 5}")

print("Print Musawir's age using + method")
age = int(input("Enter Musawir's age: "))
print("After 5 years, Musawir's age will be " + str(age + 5))

"""age + 5 is an integer (int).
Python does not allow concatenating a string with an integer directly.
We use str(age + 5) to convert it into a string."""

print("Print Musawir's age using , method")
age = int(input("Enter Musawir's age: "))
print("After 5 years, Musawir's age will be", age + 5)



