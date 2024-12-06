"""
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
● Вывести имя вашей ОС
● Вывести путь до папки, в которой вы находитесь
● Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются
все файлы с расширением .txt, то же самое для остальных
расширений
● После рассортировки выводится сообщение типа «в папке
с текстовыми файлами перемещено 5 файлов, их
суммарный размер - 50 гигабайт»
● Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод
сообщения типа «Файл data.txt был переименован в
some_data.txt»
● Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами.
"""

import os
from pathlib import Path


if os.name == "nt":
    print("OS: Windows")
elif os.name == "posix":
    print("OS: MacOS/Linux")
else:
    print("OS: unknown OS")

print(f"\ncurrent directory: {os.getcwd()}")

cwd = os.getcwd()

extensions = ['docx', 'pdf', 'pptx', 'txt', 'py']

for file in os.listdir(cwd):
    if os.path.isfile(file):  # проверяем файл ли
        if not os.path.exists(str(Path(file).suffix)[1:]):
            os.mkdir(str(Path(file).suffix)[1:])  # создаем папку для нового расширения
            extensions.append(str(Path(file).suffix)[1:])
        os.replace(file, os.path.join(str(Path(file).suffix)[1:], file))

for dirct in os.listdir(cwd):
    if not os.path.isfile(dirct) and os.path.basename(dirct) in extensions:
        summ, memory = 0, 0
        for file in os.listdir(dirct):
            summ += 1
            memory += os.stat(dirct).st_size
        # вывод количества содержимого и суммарной памяти
        print(f"{summ} files in folder \"{dirct}\", total memory: {memory}")

try:
    os.rename(os.path.join(cwd, "pptx", "pres1.pptx"), os.path.join(cwd, "pptx", "pres.pptx"))
    print(f'file "pres1.pptx" was renamed to "pres.pptx"')
except FileNotFoundError:
    print("file was not found")

