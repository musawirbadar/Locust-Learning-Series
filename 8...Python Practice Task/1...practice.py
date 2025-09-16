# Create 3 variables, Solution Task 1
print("Please Enter Your Required Details")
name = input("Please Enter Your Fullname:- ")
age = int(input("Please Enter Your Age:- "))
answer = input("Are you a tester? (yes/no):- ")

# only 'yes' will be True, everything else False
is_tester = True if answer.lower() == "yes" else False

print("Entered Details Are:", name, age, is_tester)

# Condition (If/else), Solution Task 2
number = int(input("Pleae enter any number:" ))
if number>0:
    print("Entered number is Positive")
elif number==0:
    print("Entered number is Zero")
else:
    print("Entered number is negative")

# For Loop, Solution Task 3
for i in range(10):
    print("Printing Numbers: ",i+1)

# While Loop, Solution Task 3
digit = 2
while digit<=20:
    print("Printed Even Number", digit)
    digit+=2

# Function, Solution Task 4
def multiply (a,b):
    return a*b
result = multiply(12,5)
print("Multiplication of two numbers are: ",result)

# Dictionary, Solution Task 5
users = {"username":"Musawir","email":"musawirbadar10@gmail.com","password":"123"}
users["password"] = "newpass123"
print(users)

# Dictionary with For Loop,Solution Task 6
list1=[]
for i in range (1,6):
    list2 = {
        "username" : f"user{i}",
        "email" : f"user{i}@example.com"
    }
    list1.append(list2)
    print(list2["username"])
import json
# Step 2 Converion to Json and Python, Solution Task 7
json_string = json.dumps(list1, indent=4)   # indent=4 makes it pretty
print("JSON String:\n", json_string)

# Step 3: Convert JSON string back to Python list
python_list = json.loads(json_string)

# Step 4: Print the first user's email
print("First user's email:", python_list[0]["email"])


