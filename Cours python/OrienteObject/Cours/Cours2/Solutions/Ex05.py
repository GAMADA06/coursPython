class Book:
    def __init__(self, title, category):
        self.title = title
        self.category = category


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_by_category(self, category):
        return [book.title for book in self.books if book.category == category]


# Exemple d'utilisation
lib = Library()
lib.add_book(Book("1984", "Fiction"))
lib.add_book(Book("Python 101", "Science"))

print(lib.list_by_category("Fiction"))  # ['1984']
