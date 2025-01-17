countries = [
    {"COUNTRY": "Poland", "POPULATION": 38000000},
    {"COUNTRY": "Germany", "POPULATION": 83000000},
    {"COUNTRY": "France", "POPULATION": 67000000},
    {"COUNTRY": "Italy", "POPULATION": 59000000},
    {"COUNTRY": "Spain", "POPULATION": 47000000},
]

print(f"{'COUNTRY':<15}{'POPULATION':<15}")
print("-" * 30)
for country in countries:
    print(f"{country['COUNTRY']:<15}{country['POPULATION']:<15}")
