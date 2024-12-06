"""
Напишите программу, которая считывает текст из
файла (в файле может быть больше одной строки) и выводит
в новый файл самое часто встречаемое слово в каждой
строке и число – счётчик количества повторений этого слова
в строке.
"""

file_input = "input.txt"
file_output = "output.txt"

with open(file_input, 'r') as file:
    lines = file.readlines()

for line in lines:
    my_dict = {}  # словарь (слово: кол-во повторений) для каждой строки
    word_list = line.rstrip().split(' ')
    for word in set(word_list):
        my_dict[word] = word_list.count(word)
    max_word = max(my_dict, key=my_dict.get)  # ищем макс. значение и соотв. слово
    max_value = my_dict[max_word]

    with open(file_output, 'a') as file:
        file.write(f"Word '{max_word}' repeat {max_value} times\n")
