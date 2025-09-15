# Example Dictionary 
user = {"name" : "Musawir",
        "age" : "26",
        "city" : "Islamabad"}
print (user["name"])
print (user["age"])

# Nested Dictionaries

profile =  {"username" : "admin",
            "password" : "123",
            "address":{                 # nested dictionary 
                "country" : "Pakistan",
                "Region" : "South Asia"
            }}
print(profile["address"]["country"])
print(profile["address"]["Region"])

#Dictionary with user input
user1 = {
    "role": "Tester"   # fixed value
}

# add user inputs
user1["name"] = input("Enter your name: ")
user1["age"] = int(input("Enter your age: "))

print(user1)

# Locust Example: Auto-generate multiple users (without manual input)
users = []

for i in range(1, 11):   # create 10 users
    user2 = {
        "username": f"user{i}",
        "email": f"user{i}@test.com",
        "password": "password123"
    }
    users.append(user2) # append add item at the end of the list

print(users)

