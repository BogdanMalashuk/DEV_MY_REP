"""
�������� ���������, ������� �������� �� ���� ������
� ��������� ���������� ����� � ������� �� �����
���������� ����� �����, ������� ��� ����������� �����
�����������. ����������� �����, ���������� ��������
�������, ������ ��������� � ����� stop_words.txt.
��������� ������ �������� ����������� ����� � ����� ����� �����,
���� � �������� ������� �����. ������ ���������� �� ��������:
���� � ������ ����������� ���� ����� exam, �� ���������� ������
exam, eXam, EXAm � ������ ��������.
������: � stop_words.txt �������� �����: hello email
python the exam wor is
����� ����� ��� ������� �������� ���: Hello, World! Python
IS the programming language of thE future. My EMAIL is�
PYTHON as AwESOME!
����� �������� �����: *****, ***ld! ****** ** *** programming
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
