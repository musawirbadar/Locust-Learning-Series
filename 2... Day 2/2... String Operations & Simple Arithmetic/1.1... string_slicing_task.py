title = input("Enter your title: ")

#String Operations
print(title.upper())
print(title.lower())
print(len(title))
print(title[0])

#Slicing Operation
#Hi, I'm Learning Python
print('Printing First Six Letters:-')
first_six = title[:6]
print(first_six)

print('Printing Last Six Letters:-')
last_six = title[-6:]
print(last_six)

print("Exclude first four and print rest:-")
exclude_four = title[4:]
print(exclude_four)

print("Exclude last four and print rest:-")
drop_last_four = title[:-4]
print(drop_last_four)
