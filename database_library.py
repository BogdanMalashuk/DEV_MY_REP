import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
author TEXT NOT NULL,
year INTEGER,
available INTEGER NOT NULL CHECK (available IN (0, 1))
)
''')


# cursor.executemany('''
# INSERT INTO books (title, author, year, available)
# VALUES (?, ?, ?, ?)
# ''', [
#     ("1984", "George Orwell", 1949, 1),
#     ("To Kill a Mockingbird", "Harper Lee", 1960, 1),
#     ("The Great Gatsby", "F. Scott Fitzgerald", 1925, 0),
#     ("Moby Dick", "Herman Melville", 1851, 1),
#     ("War and Peace", "Leo Tolstoy", 1869, 0)
# ])

print('////////////////////////////////////////////////')
cursor.execute('SELECT title, author FROM books WHERE available == ?', (1,))
results = cursor.fetchall()
for row in results:
    print(row)

print('////////////////////////////////////////////////')

cursor.execute('SELECT title, author FROM books WHERE year > ?', (1950,))
results = cursor.fetchall()
for row in results:
    print(row)

print('////////////////////////////////////////////////')

cursor.execute('UPDATE books SET available = ? WHERE title = ?', (1, 'The Great Gatsby'))
cursor.execute('SELECT * FROM books')
users = cursor.fetchall()
for row in users:
    print(row)

print('////////////////////////////////////////////////')

cursor.execute('DELETE FROM books WHERE title = ?', ("Moby Dick",))
cursor.execute('SELECT * FROM books')
users = cursor.fetchall()
for row in users:
    print(row)

print('////////////////////////////////////////////////')

connection.commit()

connection.close()
