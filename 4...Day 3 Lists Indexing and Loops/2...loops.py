# Example: For Loop through product IDs
products = [101, 102, 103, 104]

for p in products:
    print(f"Visiting product {p}")

# For loop with Range repeate something for x number
for i in range(5):   # repeat 5 times
    print("Request", i + 1)

# While loop is useful for retries 
count = 0
while count <= 3:
    print("Retrying login...")
    count += 1

# Break and continue
for i in range(5):
    if i == 2:
        continue   # skip 2
    if i == 4:
        break      # stop at 4
    print(i)

#Looping with Enumerate when you need both index and value
urls = ["/home", "/about", "/contact"]

for i, url in enumerate(urls):
    print(f"Request {i+1}: {url}")
