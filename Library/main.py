from classes import *
import json


def load_in_lib(library: Library):
    lib_list = []
    for book in library.books:
        book_dict = {"title": book.title,
                     "author": book.author,
                     "year": book.year,
                     "id_book": book.id_book,
                     "is_available": book.is_available
                     }
        lib_list.append(book_dict)
    with open("library.json", 'w', encoding='utf-8') as file:
        json.dump(lib_list, file, indent=4)


def load_from_lib():
    with open("library.json", 'r', encoding='utf-8') as file:
        lib_list = json.load(file)
    books_list = []
    for book_dict in lib_list:
        book = Book(
            title=book_dict["title"],
            author=book_dict["author"],
            year=book_dict["year"],
            is_available=book_dict["is_available"],
        )
        books_list.append(book)
    return books_list


books = load_from_lib()
library1 = Library(books)

print("welcome to library!")

while True:
    print("1. show available books")
    print("2. add book")
    print("3. delete book")
    print("4. find book by author")
    print("5. take book")
    print("6. return book")
    print("7. exit")

    choice = input("choose an action: ")

    if choice == "1":
        library1.list_available_books()
    elif choice == "2":
        title = input("book title: ")
        author = input("book author: ")
        year = int(input("book year: "))
        new_book = Book(title, author, year)
        library1.add_book(new_book)
        print("successful!")
    elif choice == "3":
        try:
            id_book = int(input("book id to delete: "))
            library1.remove_book(id_book)
        except ValueError:
            print("invalid id.")
    elif choice == "4":
        author = input("author: ")
        library1.find_books_by_author(author)
    elif choice == "5":
        try:
            id_book = int(input("book id to take: "))
            user = input("your name: ")
            book = library1.borrow_book(id_book)
            if book:
                book.borrow(user)
                print("successful!")
            else:
                print("invalid id or book is already taken")
        except ValueError:
            print("invalid id.")
    elif choice == "6":
        try:
            id_book = int(input("book id to return: "))
            user = input("your name: ")
            if library1.return_book(id_book, user):
                print(f"successful!")
            else:
                print("invalid id or user")
        except ValueError:
            print("invalid id")
    elif choice == "7":
        load_in_lib(library1)
        print("bye bye!\nlibrary saved successfully. Goodbye!")
        break
    else:
        print("invalid choice, enter from 1 to 7")
