import json

# 1. Create a JSON string
json_string = '{"name": "Sara", "age": 30, "email": "sara@test.com", "country": "Pakistan"}'

# 2. Convert JSON string into Python dictionary
user = json.loads(json_string)

# 3. Print only name and email
print("Name:", user["name"])
print("Email:", user["email"])

# 4. Update dictionary with new key-value
user["status"] = "active"

# 5. Convert dictionary back into JSON format
final_json = json.dumps(user)

# 6. Print final JSON string
print("Final JSON:", final_json)
