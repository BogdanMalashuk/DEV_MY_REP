"""
 Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать обработку
исключений.
"""

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        action = input("Choose operation (+, -, *, /, ^): ")

        if action == '+':
            print(f"{a} + {b} = {a + b}")
            break
        elif action == '-':
            print(f"{a} - {b} = {a - b}")
            break
        elif action == '*':
            result = a * b
            print(f"{a} * {b} = {a * b}")
            break
        elif action == '/':
            if b == 0:
                raise ZeroDivisionError
            print(f"{a} / {b} = {a / b}")
            break
        elif action == '^':
            print(f"{a} ^ {b} = {a ** b}")
            break
        else:
            print("Incorrect operation. Try again.")

    except ZeroDivisionError:
        print(f"Exception, impossible dividing by zero")
    except ValueError:
        print(f"Exception, input the number")
