# 4. Convert & Filter Product Prices

# Problem Statement
# You are given a list of tuples (product_name, price_in_dollars).
# Convert prices to INR (1 USD = 83 INR) and return only products costing more than ₹3000.

# Input

# products = [
#     ("Pen", 10),
#     ("Bag", 50),
#     ("Shoes", 60)
# ]

products = [
    ("Pen", 10),
    ("Bag", 50),
    ("Shoes", 60)
]

# Step 1: Convert USD to INR (1 USD = 83 INR)
converted = list(map(lambda item: (item[0], item[1] * 83), products))

# Step 2: Filter products costing more than ₹3000
filtered_products = list(filter(lambda item: item[1] > 3000, converted))

print("Products costing more than ₹3000:", filtered_products)
