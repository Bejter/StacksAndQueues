price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print('NORMAL PRICES')
print(30*'-')
print(f'{'ITEM':<10}PRICE')
for key, value in price_list.items():
    print(f'{key:<10}{value}')
print()
discount = 9/10
print('DISCOUNTED PRICES')
print(30*'-')
print(f'{'ITEM':<10}PRICE')
for key, value in price_list.items():
    value = value * discount
    print(f'{key:<10}{round(value,2)}')