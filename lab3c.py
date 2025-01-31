#!/usr/bin/env python3
'''Lab 3 Investigation 2 - Operate Function'''
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
    print(operate(10, 5, 'add'))       
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))  
    print(operate(10, 5, 'divide'))    

