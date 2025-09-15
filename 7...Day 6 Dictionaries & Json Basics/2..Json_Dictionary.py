# Json to Dictionary (When Recieving Data)
import json

json_data = '{"name": "Ali", "age": 25, "email": "ali@test.com"}'  # JSON string
user = json.loads(json_data)  # convert to dictionary

print(user["email"])  # now works

# Dictionary to Json (When sending data)

user = {"name": "Ali", "age": 25, "email": "ali@test.com"}  # dictionary
json_data = json.dumps(user)  # convert to JSON string

print(json_data)

