"""
Задача 1: Создание и заполнение таблиц
● Создайте таблицу authors с полями id, first_name и
last_name. Используйте PRIMARY KEY для поля id
● Создайте таблицу books с полями id, title, author_id и
publication_year. Используйте PRIMARY KEY для поля id и
FOREIGN KEY для поля author_id, ссылаясь на таблицу
authors
● Создайте таблицу sales с полями id, book_id и quantity.
Используйте PRIMARY KEY для поля id и FOREIGN KEY для
поля book_id, ссылаясь на таблицу books
● Добавьте несколько авторов в таблицу authors
● Добавьте несколько книг в таблицу books, указывая
авторов из таблицы authors
● Добавьте записи о продажах книг в таблицу sales
"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    books = relationship('Book', back_populates='author')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    pub_year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')
    sale = relationship('Sale', back_populates='book')

    def __str__(self):
        return self.title


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer)

    book = relationship('Book', back_populates='sale')


engine = create_engine('sqlite:///myDatabase.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(first_name='John', last_name='Smith')
author2 = Author(first_name='Emily', last_name='Johnson')
session.add(author1)
session.add(author2)

book1 = Book(title='The Secrets of Time', pub_year=2015, author_id=1)
book2 = Book(title='Winds of Change', pub_year=2018, author_id=2)
book3 = Book(title='Shadows and Light', pub_year=2021, author_id=1)
session.add(book1)
session.add(book2)
session.add(book3)

sale1 = Sale(book_id=2, quantity=2)
sale2 = Sale(book_id=1, quantity=1)
sale3 = Sale(book_id=3, quantity=1)
session.add(sale1)
session.add(sale2)
session.add(sale3)

session.commit()
for author in session.query(Author).all():
    print(f"first name: {author.first_name}  ||  last name: {author.last_name}  ||  id: {author.id}")

print()

for book in session.query(Book).all():
    print(f"title: {book.title}  |||  publication year: {book.pub_year}  |||  author: {book.author}")

print()

for sale in session.query(Sale).all():
    print(f"book: {sale.book}  |||  quantity: {sale.quantity}")
