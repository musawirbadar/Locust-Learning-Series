# Solution Task a
Enter_Num = int(input("Please Enter Number ")) # if you want user to enter integer then take input like this
if Enter_Num>0:
    print("The entered number is Positive")
elif Enter_Num<0:
    print("The entered number is Negative")
else:
    print("Entered number is 0")

# Solution Task b
age = int(input("Please enter your age: "))
if age<13:
    print("You're a child")
elif age>=13 and age<=19:
    print("You're a teenager")
elif age>=20 and age<=59:
    print("You're an adult")
else:
    print("You're a senior")

# Solution task c
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is NOT divisible by both 3 and 5")

# Solution Task d
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "123":
    print("Congrats, Login Successfully")
else:
    print("Invalid Credentials ")