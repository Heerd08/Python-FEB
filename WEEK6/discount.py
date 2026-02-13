# 2. Problem Statement
# You are given a list of products as tuples:

#  Task:
# • Keep only products in category "Electronics"
# • Apply a 20% discount
# • Return the total discounted price
# Input
# products = [
#     ("Laptop", "Electronics", 1000),
#     ("Shirt", "Clothing", 50),
#     ("Phone", "Electronics", 500)
# ]
# Output:
# 1200.0


products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]

total = 0

for product in products:
    category = product[1]
    price = product[2]

    if category == "Electronics":
        discount = price * 0.20
        new_price = price - discount
        total = total + new_price

print(total)
