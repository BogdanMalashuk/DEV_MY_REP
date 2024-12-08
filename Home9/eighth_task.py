"""
Пункты задания:
0. Есть данные в формате JSON – взять с диска с
исходными данными.
1. Реализовать функцию, которая считает данные из
исходного JSON-файла и преобразует их в формат CSV
2. Реализовать функцию, которая сохранит данные в
CSV-файл (данные должны сохраняться независимо от их
количества – если добавить в исходный JSON-файл ещё
одного сотрудника, работа программы не должна
нарушаться).
3. Реализовать функцию, которая добавит информацию о
новом сотруднике в JSON-файл. Пошагово вводятся все
необходимые данные о сотруднике, формируются данные
для записи.
4. Такая же функция для добавления информации о
новом сотруднике в CSV-файл.
5. Реализовать функцию, которая выведет информацию
об одном сотруднике по имени. Имя для поиска вводится с
клавиатуры.
6. Реализовать функцию фильтра по языку: с клавиатуры
вводится язык программирования, выводится список всех
сотрудников, кто владеет этим языком программирования.
7. Реализовать функцию фильтра по году: ввести с
клавиатуры год рождения, вывести средний рост всех
сотрудников, у которых год рождения меньше заданного.
8. Программа должна представлять собой интерактив –
пользовательское меню с возможностью выбора
определённого действия (действия – функции из
предыдущих пунктов + выход из программы). Пока
пользователь не выберет выход из программы, должен
предлагаться выбор следующего действия.
"""

import json
import csv
from validity import *

fieldnames = ["name", "birthday", "height", "weight", "car", "languages"]


def init_data():  # ввод данных
    data = {
        "name": get_valid_name(),
        "birthday": get_valid_birthday(),
        "height": get_valid_height(),
        "weight": get_valid_weight(),
        "car": get_valid_car(),
        "languages": get_valid_languages()}
    return data


def convert_to_scv(json_file, csv_file):  # задание 1-2
    with open(json_file, 'r') as file:
        employees = json.load(file)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)


def add_employee_to_json(json_file):  # задание 3
    data = init_data()
    with open(json_file, 'r') as file:
        employees = json.load(file)

    employees.append(data)
    with open(json_file, 'w') as file:
        json.dump(employees, file, indent=4)


def add_employee_to_csv(csv_file):  # задание 4
    data = init_data()
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)


def employee_info(csv_file):  # задание 5
    name = get_valid_name()
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        employees = csv.reader(file)
        for employee in employees:
            if employee[0] == name:
                print(employee)


def language_find(csv_file):  # задание 6
    language = input("language: ")
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        employees = csv.reader(file)
        for employee in employees:
            if language in employee[5]:
                print(employee)


def average_height(cvs_file):  # задание 7
    heights = []
    while True:
        year = input("year: ")
        if year.isdigit() and len(year) == 4:
            break
        else:
            print("invalid input, use 4 digits.")
    with open(cvs_file, 'r', newline='', encoding='utf-8') as file:
        employees = csv.DictReader(file)
        for employee in employees:
            if int(employee['birthday'][-4:]) < int(year):
                heights.append(int(employee['height']))
    print(sum(heights) / len(heights))


user_json_file = "employees.json"
user_csv_file = "employees.csv"

while True:
    print(f"actions list:"
          f"\n1. read JSON and convert it to CSV."
          f"\n2. add new employee to JSON."
          f"\n3. add new employee to CSV."
          f"\n4. show info by name."
          f"\n5. show info by language."
          f"\n6. show average height by year."
          f"\n7. exit")

    while True:
        try:
            choice = int(input("choice: "))
            if 1 <= choice <= 7:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, try again.")

    if choice == 1:
        convert_to_scv(user_json_file, user_csv_file)
    elif choice == 2:
        add_employee_to_json(user_json_file)
    elif choice == 3:
        add_employee_to_csv(user_csv_file)
    elif choice == 4:
        employee_info(user_csv_file)
    elif choice == 5:
        language_find(user_csv_file)
    elif choice == 6:
        average_height(user_csv_file)
    else:
        exit()
