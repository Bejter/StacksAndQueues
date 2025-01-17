import json

with open("euro.json", "r", encoding="utf-8") as file:
    data = json.load(file)

rates = data["rates"]

print("Date            Buying Rate     Selling Rate")
print("=" * 40)

for rate in rates:
    date = rate["effectiveDate"]
    mid_rate = rate["mid"] 
    
    print(f"{date}      {mid_rate:<10}      {mid_rate:<10}")
