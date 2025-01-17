import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = []  # Stos do przechowywania nawiasów
    # Mapa odpowiadających nawiasów
    brackets = {')': '(', ']': '[', '}': '{'}

    # Iterujemy przez każdy znak w wyrażeniu
    for char in expression:
        if char in "([{":  # Jeśli to nawias otwierający
            stack.append(char)
        elif char in ")]}":  # Jeśli to nawias zamykający
            # Sprawdzamy, czy stos nie jest pusty i czy nawiasy się zgadzają
            if not stack or stack[-1] != brackets[char]:
                return False  # Jeśli nie, wyrażenie jest niepoprawne
            stack.pop()  # Usuń odpowiedni nawias otwierający

    # Jeśli stos jest pusty, wszystkie nawiasy zostały poprawnie zamknięte
    return len(stack) == 0

if brackets_ok(expression1):
    print("Expression 1 has correct brackets.")
else:
    print("Expression 1 has incorrect brackets.")

if brackets_ok(expression2):
    print("Expression 2 has correct brackets.")
else:
    print("Expression 2 has incorrect brackets.")

if brackets_ok(expression3):
    print("Expression 3 has correct brackets.")
else:
    print("Expression 3 has incorrect brackets.")
