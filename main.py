while True:

    num1 = float(input('Enter your first number:'))
    num2 = float(input('Enter your second number:'))

    operator = input('Choose operator: ( + , - , * , / ):')

    if operator == '+':
        print('Result:', num1 + num2)
    elif operator == '-':
        print('Result:', num1 - num2)
    elif operator == '*':
        print('Result:', num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print('Result:', num1 / num2)
        else:
            print('Cannot divide by zero')
    else:
        print('Invalid operator')

    again = input('Do you want to continue? (y/n):')
    if again != 'y':
        break