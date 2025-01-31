#!/usr/bin/env python3

# Author ID: epatel16

def operate(number1, number2, operator):
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    # Test the function with different operators
    print(operate(10, 5, 'add'))       # Expected output: 15
    print(operate(10, 5, 'subtract'))  # Expected output: 5
    print(operate(10, 5, 'multiply'))  # Expected output: 50
    print(operate(10, 5, 'divide'))    # Expected output: Error message

