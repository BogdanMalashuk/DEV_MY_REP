class Book:
    counter = 0
    instance = []

    def __init__(self, title, author, year, is_available=True, reader=None):
        self.title = title
        self.author = author
        self.year = year
        self.id_book = Book.counter
        self.is_available = is_available
        self.reader = reader
        Book.counter += 1
        self.__class__.instance.append(self)

    def borrow(self, reader):
        self.is_available = False
        self.reader = reader

    def return_book(self):
        self.is_available = True
        self.reader = None


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                self.books.remove(book)
                print("successful!")
                return
        print(f"there is no book with id: {id_book}\n")

    def find_books_by_author(self, author):
        is_in = False
        for book in self.books:
            if book.author == author:
                is_in = True
                print(f"title: {book.title} ||| "
                      f"year: {book.year} ||| "
                      f"id: {book.id_book} ||| "
                      f"is available: {book.is_available}")
        if not is_in:
            print(f"there is no books with author: {author}")

    def list_available_books(self):
        is_in = False
        for book in self.books:
            if book.is_available:
                is_in = True
                print(f"title: {book.title} ||| "
                      f"author: {book.author} |||"
                      f"year: {book.year} ||| "
                      f"id: {book.id_book}")
        if not is_in:
            print("there is no available books\n")

    def borrow_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                if book.is_available:
                    return book
                else:
                    print(f"The book with id {book.id_book} is already taken by {book.reader}.")
                    return None
        print(f"No book with id {id_book}.")
        return None

    def return_book(self, id_book, user):
        for book in self.books:
            if book.id_book == id_book:
                if not book.is_available and book.reader == user:
                    book.return_book()
                    return True
                elif book.reader != user:
                    print(f"The book with id {id_book} is taken by another user ({book.reader}).")
                    return False
        print(f"No book with id {id_book}.")
        return False
