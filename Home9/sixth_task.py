"""
В файл записано некоторое содержимое (буквы,
цифры, пробелы, специальные символы и т.д.). Числом
назовём последовательность цифр, идущих подряд. Вывести
сумму всех чисел, записанных в файле.
Пример:
Входные данные: 123 ааа456 1x2y3z 4 5 6
Выходные данные: 600
"""

import re

file_name = "numbers.txt"
with open(file_name, 'r') as file:
    content = file.read()

numbers = sum(map(int, re.findall(r'\d+', content)))

print(numbers)
