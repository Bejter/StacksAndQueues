import queue

def customer_service():
    customer_queue = queue.Queue() 
    ticket_number = 1  
    
    while True:
        print("\nCustomer Service Menu:")
        print("1. Add a new customer")
        print("2. Serve the next customer")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            print(f"Customer with ticket number {ticket_number} added to the queue.")
            customer_queue.put(ticket_number)  
            ticket_number += 1  
        
        elif choice == '2':
            if not customer_queue.empty():
                served_customer = customer_queue.get()  
                print(f"Serving customer with ticket number {served_customer}.")
            else:
                print("No customers in the queue to serve.")
        
        elif choice == '0':
            print("Exiting the customer service program.")
            break
        
        else:
            print("Invalid option. Please select a valid option.")
            
if __name__ == "__main__":
    customer_service()
