import json

product = {}

product['name'] = input("Enter the product name: ")

while True:
    try:
        product['price'] = round(float(input("Enter the price of the product: ")), 2)
        break 
    except ValueError:
        print("Invalid input. Please enter a valid number for price.")

while True:
    paid_input = input("Has the product been paid for? (yes/no): ").lower()
    if paid_input == 'yes':
        product['paid'] = True
        break
    elif paid_input == 'no':
        product['paid'] = False
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4)

print("Product data has been saved to product.json.")
