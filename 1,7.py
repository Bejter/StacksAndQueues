products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
total = 0
print(f"{'NAME':<25}{'QUANTITY'}")
for key, value in products.items():
    total += value
    print(f'{key:<25}{value}')
print(f'Total quantity of items is: {total}')
    