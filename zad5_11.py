import json

def read_voting_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  

def save_voting_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

filename = 'voting.json'

voting_data = read_voting_data(filename)

person_name = input('Name of the person you are voting for: ')

if person_name in voting_data:
    voting_data[person_name] += 1  
else:
    voting_data[person_name] = 1  

save_voting_data(filename, voting_data)

print(f"Vote recorded for {person_name}.")
