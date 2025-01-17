import queue

# create a visited_websites stack
visited_websites = queue.LifoQueue()

# some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

# Initialize the current website as the most recently visited one
current_website = visited_websites.get()

while True:
    print('You are currently viewing:', current_website)
    print()
    
    website = input('Enter website name (0 for back): ')
    
    if website == '0':  # Cofanie do poprzednio odwiedzonej strony
        if visited_websites.empty():
            print('No previously visited websites.')
        else:
            print('<-- Going back to a previously visited website')
            current_website = visited_websites.get()  # Ustaw stronę na poprzednią
    elif website != "":  # Dodawanie nowej strony
        visited_websites.put(current_website)  # Zapisz aktualną stronę w historii
        current_website = website  # Ustaw nową stronę jako aktualną
    else:
        print('Please enter a valid website name or "0" to go back.')
