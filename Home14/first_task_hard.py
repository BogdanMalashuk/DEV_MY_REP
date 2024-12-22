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


import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql_password_pass7",
)
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS employees_db")
cursor.execute("USE employees_db")

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Position VARCHAR(50),
    Department VARCHAR(50),
    Salary INT)
''')


# cursor.execute('''
# INSERT INTO employees (Name, Position, Department, Salary)
# VALUES ('John Smith', 'Software Engineer', 'IT', 7500),
#     ('Sarah Johnson', 'Manager', 'Finance', 4800),
#     ('Michael Brown', 'Data Analyst', 'Marketing', 4200),
#     ('Emily Davis', 'Manager', 'Sales', 6900),
#     ('David Wilson', 'HR Specialist', 'Sales', 3000)
# ''')

cursor.execute('''
SELECT * FROM employees''')
employees = cursor.fetchall()
print("\nAll employees:")
for employee in employees:
    print(employee)


cursor.execute('''
UPDATE employees
SET Position = "Head HR" WHERE Name = "David Wilson"
''')

cursor.execute('''
SELECT * FROM employees WHERE Name = "David Wilson"''')
employees = cursor.fetchall()
print("\nEdited employee:")
for employee in employees:
    print(employee)


# cursor.execute('''
# ALTER TABLE employees ADD COLUMN HireDate DATE''')
# cursor.executemany('''
# UPDATE employees
# SET HireDate = %s WHERE id = %s
# ''', [
#     ('2019-12-19', 1),
#     ('2022-04-19', 2),
#     ('2015-01-30', 3),
#     ('2009-04-25', 4),
#     ('2017-06-06', 5)
# ])

cursor.execute('''DROP PROCEDURE IF EXISTS get_managers;''')  # если уже создана
cursor.execute('''
CREATE PROCEDURE get_managers()
BEGIN
    SELECT * FROM employees WHERE Position = "Manager";
END
''')
cursor.callproc('get_managers')

print("\nmanagers:")
for results in cursor.stored_results():
    managers = results.fetchall()
    for manager in managers:
        print(manager)


cursor.execute('''DROP PROCEDURE IF EXISTS get_majors;''')  # если уже создана
cursor.execute('''
CREATE PROCEDURE get_majors()
BEGIN
    SELECT * FROM employees WHERE Salary > 5000;
END
''')
cursor.callproc('get_majors')

print("\n>5000 salary have:")
for results in cursor.stored_results():
    majors = results.fetchall()
    for major in majors:
        print(major)


cursor.execute('''DROP PROCEDURE IF EXISTS get_salers;''')  # если уже создана
cursor.execute('''
CREATE PROCEDURE get_salers()
BEGIN
    SELECT * FROM employees WHERE Department = "Sales";
END
''')
cursor.callproc('get_salers')

print("\nsalers:")
for results in cursor.stored_results():
    salers = results.fetchall()
    for saler in salers:
        print(saler)


cursor.execute('''DROP FUNCTION IF EXISTS avg_salary;''')  # если уже создана
cursor.execute('''
CREATE FUNCTION avg_salary() 
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE avg_salary DECIMAL(10, 2);
    SELECT AVG(Salary) INTO avg_salary FROM employees;
    RETURN avg_salary;
END
''')

cursor.execute('''SELECT avg_salary();''')
avg_salary = cursor.fetchone()[0]
print(f"\naverage salary: {avg_salary}")


# cursor.execute('DROP TABLE employees')
# connection.commit()
connection.close()
