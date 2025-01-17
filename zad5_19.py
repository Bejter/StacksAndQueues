import json

def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data["reservations"]

def get_number_of_rooms(reservations):
    return len(reservations)

def get_paid_reservations(reservations):
    return len([reservation for reservation in reservations if reservation['paid']])

def get_unpaid_reservations(reservations):
    return len([reservation for reservation in reservations if not reservation['paid']])

def get_total_paid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if reservation['paid'])

def get_total_unpaid_value(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if not reservation['paid'])

def main():

    reservations = load_reservations('reservations.json')

    number_of_rooms = get_number_of_rooms(reservations)
    number_of_paid_reservations = get_paid_reservations(reservations)
    number_of_unpaid_reservations = get_unpaid_reservations(reservations)
    total_paid_value = get_total_paid_value(reservations)
    total_unpaid_value = get_total_unpaid_value(reservations)

    print(f"Number of rooms: {number_of_rooms}")
    print(f"Number of paid reservations: {number_of_paid_reservations}")
    print(f"Number of unpaid reservations: {number_of_unpaid_reservations}")
    print(f"Total value of paid reservations: ${total_paid_value:.2f}")
    print(f"Total value of unpaid reservations: ${total_unpaid_value:.2f}")

if __name__ == "__main__":
    main()
