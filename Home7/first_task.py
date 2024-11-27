import random

"""
Дан список чисел. С помощью map() получить список,
где каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
"""

int_list = [random.randint(0, 10) for i in range(10)]
print("Integer list:")
print(int_list)

string_list = list(map(str, int_list))
print("String list:")
print(string_list)
