import queue

number_in_decimal = int(input('Input number to convert: '))

binary_number = queue.LifoQueue()

while number_in_decimal != 0:
    binary_number.put(number_in_decimal%2)
    number_in_decimal = number_in_decimal//2

while not binary_number.empty():
    print(binary_number.get(),end='')