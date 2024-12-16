"""
Задача: Реализуйте генератор, который построчно считывает текстовый файл (ленивое чтение).
Напишите функцию file_reader(file_path), которая возвращает строки файла по одной.
Не загружайте весь файл в память.
Пример использования:
python
Копировать код
for line in file_reader("example.txt"):
    print(line.strip())
Дополнительно: Реализуйте генератор, который возвращает только строки, содержащие слово "Python".

"""


def reader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in reader(file):
            if 'python' in line.lower():
                yield line.strip()


text_file = "text.txt"

print("file content:")
for line in reader(text_file):
    print(line)

print("\n\nstrings with 'python':")
for line in generator(text_file):
    print(line)
