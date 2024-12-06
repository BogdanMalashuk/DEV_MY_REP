"""
В текстовый файл построчно записаны фамилия и имя
учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов.
"""

text_file = "text.txt"

with open(text_file, 'r') as file:
    lines = file.readlines()

for line in lines:
    if int(line.strip('\n').split()[2]) < 3:
        print(line, end='')
