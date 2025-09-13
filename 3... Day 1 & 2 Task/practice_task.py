fname = input("Enter Your First Name: ")
lname = input("Enter Your Last Name: ")

print(f"Your full name using fstring will be: Hello, {fname} {lname}")
print("Your full name using concatination will be: Hello," + " " + fname + " " + lname)

slicing = input("Please enter the word: ")
print("Here's the first 3 characters:",slicing[:3])
print("Here's the last 3 characters:",slicing[-3:])

age = int(input("Enter Your Age: "))
print(f"After 10 years your age will be {age + 10}")
print("After 10 years your age will be " + str(age + 10))