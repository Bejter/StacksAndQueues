import csv
from collections import defaultdict

def read_province_data(filename):
    province_map = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            province_map[row['Letter']] = row['Name']
    return province_map

def count_vehicles_by_province(vehicle_file, province_map):
    province_count = defaultdict(int)
    
    with open(vehicle_file, mode='r', encoding='utf-8') as file:
        vehicles = file.readlines()
        
        for vehicle in vehicles:
            vehicle = vehicle.strip()
            if vehicle:
                first_letter = vehicle[0] 
                if first_letter in province_map:
                    province_count[province_map[first_letter]] += 1

    return province_count

province_map = read_province_data('province.csv') 
vehicle_count = count_vehicles_by_province('vehicle.txt', province_map)  

print("Vehicle count by province:")
for province, count in vehicle_count.items():
    print(f"{province}: {count}")
