def reverse_string(input_string):
    stack = [] 

    for char in input_string:
        stack.append(char)
    
    reversed_string = ""

    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

input_text = input("Enter the text you want to reverse: ")
reversed_text = reverse_string(input_text)
print(f"Reversed text: {reversed_text}")