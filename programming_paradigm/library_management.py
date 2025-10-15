class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def set_checkout(self):
        self._is_checked_out = not self._is_checked_out

    def get_checkout(self):
        return self._is_checked_out
    
    def return_book(self):
        pass


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.get_checkout():
                book.set_checkout()
                print(f"{book.title} has been checked out.")
                return
        print("Book not found or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.get_checkout():
                book.set_checkout()=True
                print(f"{book.title} has been returned.")
                return
        print("Book not found or not checked out.")

    def list_available_books(self):
        available_books = [f"{book.title} by {book.author}" 
                           for book in self._books if not book.get_checkout()]
        return "\n".join(available_books) if available_books else "No books available."
        