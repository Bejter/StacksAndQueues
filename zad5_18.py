import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

for dog in dogs:
    if dog['age'] < 5:
        print(f"Name: {dog['name']}")
        print(f"Breed: {dog['breed']}")
        print(f"Age: {dog['age']}")
        print(f"Weight: {dog['weight_kg']} kg")
        print(f"Owner: {dog['owner']}")
        print(f"Vaccinated: {'Yes' if dog['vaccinated'] else 'No'}")
        print()
