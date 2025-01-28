class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            print(book.get_description())


# Exemple d'utilisation
library = Library()
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library.add_book(book1)
library.add_book(book2)

library.list_books()
