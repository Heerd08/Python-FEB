"""
Convert & Filter Product Prices
Problem Statement:
Convert prices from USD to INR (1 USD = 83 INR)
Return only products costing more than ₹3000.
"""

def convert_to_inr(product):
    name, price = product
    return (name, price * 83)

def is_above_3000(product):
    return product[1] > 3000

def convert_and_filter_products(products):

    # Convert USD to INR
    converted_products = list(map(convert_to_inr, products))
    print(converted_products)

    # Filter products above 3000
    filtered_products = list(filter(is_above_3000, converted_products))

    return filtered_products


def main():
    products = [
        ("Pen", 10),
        ("Bag", 50),
        ("Shoes", 60)
    ]

    result = convert_and_filter_products(products)
    print(f"Products costing more than ₹3000: {result}")


if __name__ == "__main__":
    main()
