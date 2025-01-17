basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

person = {**basic_data, **advanced_data}

print("Personal Data:")
for key, value in person.items():
    print(f"{key}: {value}")