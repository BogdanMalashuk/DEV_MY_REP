import random

"""
Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0.
"""

rand_list = [random.randint(0, 20) - 10 for i in range(10)]
print("Random list:")
print(rand_list)

positive_list = list(filter(lambda x: x > 0, rand_list))
print("Positive_list:")
print(positive_list)
