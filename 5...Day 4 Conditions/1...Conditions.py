#If Statement
x=10
if x>5:
    print("X is greater than 5")

#If Else Statement
print("If Else Statement:-")
age=15
if age>=18:
    print("You're an adult")
else:
    print("You're under age")

#If-Elif-Else
print("If-Elif-Else")
marks = 75
if marks >=90:
    print("You've earned A grade")
elif marks >=70:
    print("You've earned B grade")
elif marks >=50:
    print("You've earned C grade")
else:
    print("F Grade, You need to work hard")

#Nested if 
num = 15
if num > 0: #First Condition: check if number is positive
    if num % 2 == 0: # Nested Condition: check if num is divisble by 2 means remainder should be 0
        print("Positive Even")
    else:
        print("Positive Odd")

#Logical operator with And condition
age1 = 60
if age1 >=20 and age1<60:
    print("You're eligible to work")
else:
    print("You spent your age limit, Take Rest!")