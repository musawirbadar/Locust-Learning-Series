# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["hello", 42, 3.14, True]  # Can have different data types

#Accessing list items
print(fruits[0])  # First item (apple)
print(fruits[-1])  # Last item (cherry)
print(numbers[2]) # 3rd number (30)
print(numbers[-4]) # 1st number (10)

#Modifying List Elements
fruits[1] = "mango"  # Changing 'banana' to 'mango'
print(fruits)  # ['apple', 'mango', 'cherry']

numbers[2] = 60
print(numbers)

mixed[3] = False
print(mixed)

# List indexing and Slicing
numbers = [10,20,30,40,50,60]
print(numbers[:3]) # It will print first 3 elements [10,20,30]
print('Print Last 3 elements',numbers[:-3]) # It will print last 3 elements [40,50,60]