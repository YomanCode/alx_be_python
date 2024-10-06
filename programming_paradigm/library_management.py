# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._is_checked_out = False    # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


# Define the Library class
class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark the book as checked out if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f'You have successfully checked out "{title}".'
        return f'Sorry, "{title}" is either unavailable or not in the library.'

    def return_book(self, title):
        """Mark the book as returned and available."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return f'You have successfully returned "{title}".'
                return f'"{title}" was not checked out.'
        return f'"{title}" not found in the library.'

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return f'Available books: {", ".join(available_books)}'
        else:
            return 'No books are currently available.'

# Example usage:
if __name__ == "__main__":
    # Create a library instance
    library = Library()

    # Create some book instances
    book1 = Book("The Catcher in the Rye", "J.D. Salinger")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List available books
    print(library.list_available_books())

    # Check out a book
    print(library.check_out_book("1984"))

    # List available books after checkout
    print(library.list_available_books())

    # Try to check out a book that is already checked out
    print(library.check_out_book("1984"))

    # Return a book
    print(library.return_book("1984"))

    # List available books after returning
    print(library.list_available_books())