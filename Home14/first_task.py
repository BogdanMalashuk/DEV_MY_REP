"""
Представим, что у нас есть таблица "Employees" с
полями "Name", "Position", "Department", "Salary".
● Создайте таблицу "Employees" с указанными полями.
● Вставьте в таблицу несколько записей с информацией о
сотрудниках вашей компании.
● Измените данные в таблице для каких-то сотрудников.
Например, изменим должность одного из сотрудников на
более высокую.
● Добавьте новое поле "HireDate" (дата приема на работу) в
таблицу "Employees".
Продолжение ->
Задания
● Добавьте записи о дате приема на работу для всех
сотрудников.
● Найдите всех сотрудников, чья должность "Manager".
● Найдите всех сотрудников, у которых зарплата больше
5000 долларов.
● Найдите всех сотрудников, которые работают в отделе
"Sales".
● Найдите среднюю зарплату по всем сотрудникам.
● Удалите таблицу "Employees".
* в качестве задания с повышенным уровнем сложности
"""

import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER)
    ''')


cursor.executemany('''
INSERT INTO Employees (name, position, department, salary) VALUES (?, ?, ?, ?)
''', [
    ('John Smith', 'Software Engineer', 'IT', 7500),
    ('Sarah Johnson', 'Manager', 'Finance', 4800),
    ('Michael Brown', 'Data Analyst', 'Marketing', 4200),
    ('Emily Davis', 'Manager', 'Sales', 6900),
    ('David Wilson', 'HR Specialist', 'Sales', 3000)
])


print('*'*25, 'TABLE', '*'*26, sep='')
cursor.execute('SELECT * FROM Employees')
employees = cursor.fetchall()
for employee in employees:
    print(employee)


print('*'*20, 'EDITED POSITIONS', '*'*20, sep='')
cursor.execute('UPDATE Employees SET position = "Head of HR" WHERE name = "David Wilson"')
cursor.execute('SELECT * FROM Employees WHERE name = "David Wilson"')
employees = cursor.fetchall()
for employee in employees:
    print(employee)


print('*'*20, 'WITH DATE COLUMN', '*'*20, sep='')
cursor.execute('ALTER TABLE Employees ADD COLUMN HireDate TEXT')
cursor.executemany('''
UPDATE Employees SET HireDate = ? WHERE id = ?
''', [
    ('2019-12-19', 1),
    ('2022-04-19', 2),
    ('2015-01-30', 3),
    ('2009-04-25', 4),
    ('2017-06-06', 5)
])

cursor.execute('SELECT * FROM Employees')
employees = cursor.fetchall()
for employee in employees:
    print(employee)


print('*'*24, 'MANAGERS', '*'*24, sep='')
cursor.execute('SELECT * FROM Employees WHERE position == "Manager"')
managers = cursor.fetchall()
for manager in managers:
    print(manager)


print('*'*22, '>5000 SALARY', '*'*22, sep='')
cursor.execute('SELECT * FROM Employees WHERE salary > 5000')
items = cursor.fetchall()
for item in items:
    print(item)


print('*'*25, 'SALERS', '*'*25, sep='')
cursor.execute('SELECT * FROM Employees WHERE department == "Sales"')
salers = cursor.fetchall()
for saler in salers:
    print(saler)


print('*'*20, 'AVERAGE SALARY', '*'*22, sep='')
cursor.execute('SELECT AVG(salary) FROM Employees')
avg_salary = cursor.fetchone()[0]
print(f"average salary: {avg_salary}")


print('*'*19, 'DELETING DATABASE', '*'*20, sep='')
cursor.execute('DROP TABLE Employees')
print("table was deleted")


# connection.commit()
connection.close()
