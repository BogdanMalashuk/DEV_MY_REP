"""
Напишите программу, которая получает на вход строку
с названием текстового файла и выводит на экран
содержимое этого файла, заменяя все запрещённые слова
звездочками. Запрещённые слова, разделённые символом
пробела, должны храниться в файле stop_words.txt.
Программа должна находить запрещённые слова в любом месте файла,
даже в середине другого слова. Замена независима от регистра:
если в списке запрещённых есть слово exam, то замениться должны
exam, eXam, EXAm и другие вариации.
Пример: в stop_words.txt записаны слова: hello email
python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python
IS the programming language of thE future. My EMAIL is…
PYTHON as AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming
language of *** future. My ***** **... ****** ** awesome!!!!
"""

import re

file_name = input("file name: ").strip()
sw_file = "stop_words.txt"

with open(sw_file, 'r') as sw_file:
    sw_content = sw_file.read().split()

stop_words = re.compile(r"|".join(re.escape(word) for word in sw_content), re.IGNORECASE)

with open(file_name, 'r') as input_file:
    file_content = input_file.readlines()

for line in file_content:
    line = stop_words.sub(lambda word: '*' * len(word.group()), line)
    print(line, end='')
