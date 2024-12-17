"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
"""


def infinity(count):
    for i in range(count - 1):
        yield f"{i % 3 + 1}-"
    yield f"{(count - 1) % 3 + 1}"


while True:
    try:
        value = int(input("Input count: "))
        if value < 1:
            raise ValueError
        break
    except ValueError:
        print("invalid input, must be positive integer")

for item in infinity(value):
    print(item, end='')
