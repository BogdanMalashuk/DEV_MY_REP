"""
Дан текстовый файл с несколькими строками.
Зашифровать шифром Цезаря, при этом шаг зависит от
номера строки: для первой строки шаг 1, для второй – 2 и т.д.
Пример:
Входные данные:           Выходные данные:
Hello                     Ifmmp
Hello                     Jgnnq
Hello                     Khoor
Hello                     Lipps
"""

file_input = "input.txt"
file_output = "output.txt"
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


with open(file_input, 'r') as i_file, open(file_output, 'w') as o_file:
    lines = i_file.readlines()
    for i in range(0, len(lines)):
        locked_str = ''
        key = i + 1

        for lit in lines[i]:
            if lit in alphabet_lower:
                locked_str += alphabet_lower[(alphabet_lower.index(lit) + key) % 26]
            elif lit in alphabet_upper:
                locked_str += alphabet_upper[(alphabet_upper.index(lit) + key) % 26]
            else:
                locked_str += lit
        o_file.write(locked_str)
