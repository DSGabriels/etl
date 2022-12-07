from entities.book import Book

class BookRepository:
    def __init__(self) -> None:
        self.list_books: list[Book] = []

    def verif_if_book_exists(self, book_id: int) -> bool:
        for book in self.list_books:
            if book.id == book_id:
                return True
        return False

    def get_book(self, book_id: int):
        for book in self.list_books:
            if book_id == book.id:
                return book
        return "Livro não existe"


    def down_stock(self, book_id):
        for book in self.list_books:
            if book.id == book_id:
                book = self.get_book(book_id)
                book.stock -= 1
        return False


    def get_stock(self, book_id: int):
        for book in self.list_books:
            if book.id == book_id:
                book = self.get_book(book_id)
                return book.stock
        return False


    def verif_book_value(self, book_id: int):
        book = self.get_book(book_id)
        if book.price > 0 :
            return True
        return False