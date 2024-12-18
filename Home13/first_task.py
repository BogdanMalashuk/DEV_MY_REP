"""
Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию.
"""


def fibonacci(limit):
    first = 0
    second = 1
    now = second
    if limit == 1:
        return
    while now < limit:
        yield now
        now = first + second
        first = second
        second = now


while True:
    try:
        value = int(input("Input value: "))
        if value < 1:
            raise ValueError
        break
    except ValueError:
        print("invalid input, must be positive integer")


for num in fibonacci(value):
    print(num, end=' ')
