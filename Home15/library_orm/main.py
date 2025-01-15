from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    year = Column(Integer, nullable=False)
    is_taken = Column(Integer, default=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')

    def __str__(self):
        return f'{self.title}'


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String, nullable=False)

    books = relationship('Book', back_populates='author')

    def __str__(self):
        return f'{self.fullname}'


def add_book():
    title = input('enter book title: ')
    year = input('enter publication year: ')
    book = Book(title=title, year=year)
    session.add(book)
    session.commit()


def del_book():
    id_to_del = input('enter book id to del: ')
    book_to_del = session.query(User).filter_by(id=id_to_del)
    session.delete(book_to_del)
    session.commit()


def take_book():
    id_to_take = input('enter book id to take: ')
    book_to_take = session.query(Book).filter_by(id=id_to_take).first()
    if not book_to_take.is_taken:
        reader_name = input('enter login: ')
        password = input('enter your password: ')
    else:
        print('book is already taken')

    session.commit()


def return_book():
    pass
    session.commit()


engine = create_engine('sqlite:///myDatabase.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def main():
    while True:
        print(f'choose command number:'
              f'\n1. add new book'
              f'\n2. delete book'
              f'\n3. take book'
              f'\n4. return book'
              f'\n5. exit')

        command = input('your choice: ')

        if command == '1':
            add_book()
        elif command == '2':
            del_book()
        elif command == '3':
            take_book()
        elif command == '4':
            return_book()
        elif command == '5':
            print('bye bye!')
            break


main()
