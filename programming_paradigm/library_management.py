# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        self._is_checked_out = True
    
    def return_book(self):
        self._is_checked_out = False
    
    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f'You have successfully checked out "{title}".'
        return f'Sorry, "{title}" is either unavailable or not in the library.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return f'You have successfully returned "{title}".'
                return f'"{title}" was not checked out.'
        return f'"{title}" not found in the library.'

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return f'Available books: {", ".join(available_books)}'
        else:
            return 'No books are currently available.'

if __name__ == "__main__":
    library = Library()

    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print(library.list_available_books())

    print(library.check_out_book("1984"))

    print(library.list_available_books())

    print(library.check_out_book("1984"))

    print(library.return_book("1984"))

    print(library.list_available_books())