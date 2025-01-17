def calculate_rpn(expression):
    stack = []  

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else 'Error'  
    }

    for token in expression.split():
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') < 2):  
            stack.append(float(token)) 
        elif token in operations:  
            if len(stack) >= 2:
                y = stack.pop()
                x = stack.pop() 
                result = operations[token](x, y) 
                stack.append(result) 
            else:
                print("Error: Not enough operands.")
                return
        elif token == '=':
            if len(stack) == 1:
                print(f"Result: {stack[-1]}")
            else:
                print("Error: Invalid expression.")
            return
        else:
            print(f"Error: Unknown token '{token}'")
            return
        
while True:
    expression = input("Enter RPN expression or 'exit' to quit: ")
    if expression.lower() == 'exit':
        break
    calculate_rpn(expression)
