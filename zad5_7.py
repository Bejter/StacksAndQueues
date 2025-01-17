def hotel_list(hotels):
    return [hotel['name'] for hotel in hotels]

def avg_price(hotels):
    total_price = sum(hotel['price'] for hotel in hotels)
    return round(total_price / len(hotels))

hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},
   {"name": "Metropol", "price": 480.00},
   {"name": "New Port", "price": 420.00},
   {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},
   {"name": "Aqua", "price": 345.00},
   {"name": "La Boutique", "price": 390.00},
   {"name": "Marina", "price": 410.00}
]

avg_price_krakow = avg_price(hotels_in_Krakow)
avg_price_sopot = avg_price(hotels_in_Sopot)

krakow_hotels = hotel_list(hotels_in_Krakow)
sopot_hotels = hotel_list(hotels_in_Sopot)

print(f"Hotels in Krakow: {', '.join(krakow_hotels)}")
print(f"Average hotel price in Krakow: {avg_price_krakow}")
print(f"Hotels in Sopot: {', '.join(sopot_hotels)}")
print(f"Average hotel price in Sopot: {avg_price_sopot}")

if avg_price_krakow < avg_price_sopot:
    print("Cheaper hotels in: Krakow")
elif avg_price_krakow > avg_price_sopot:
    print("Cheaper hotels in: Sopot")
else:
    print("Hotels in both cities have the same average price")
