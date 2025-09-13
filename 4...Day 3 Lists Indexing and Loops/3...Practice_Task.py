#Solution a
for num in range(1, 6):   # 1 to 5
    print(num)

#Solution b
pages = ["/login","/products","/cart"]
for p in pages:
    print(f"Visited Page is {p}")

#Solution c
# Empty list to store product IDs
products = []

count = 0
while count < 3:
    product_d = input("Enter Product ID: ")
    products.append(product_d)   # add each product to the list
    count += 1

# Print all entered products
for p in products:
    print(f"Entered Product ID: {p}")
