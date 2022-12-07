from repositories.book_repository import BookRepository
import unittest

from entities.book import Book
from repositories.book_repository import BookRepository


class TestGeral(unittest.TestCase):

    def test_verif_if_book_exist(self):
        book1 = Book(1, "Livro1", "asd", "autor1", "teste1", 15)
        book2 = Book(2, "Livro2", "asd", "autor2", "teste2", 20)
        book3 = Book(3, "Livro2", "asd", "autor2", "teste2", 20)
        book_repository = BookRepository()
        book_repository.list_books.append(book1)
        book_repository.list_books.append(book2)

        book_verdadeiro = book_repository.verif_if_book_exists(book1.id)
        book_falso = book_repository.verif_if_book_exists(book3.id)

        self.assertTrue(book_verdadeiro)
        self.assertFalse(book_falso)



    def test_down_stock(self):
        book1 = Book(1, "Livro1", "asd", "autor1", "teste1", 15)
        book2 = Book(2, "Livro2", "asd", "autor2", "teste2", 20)
        book3 = Book(3, "Livro2", "asd", "autor2", "teste2", 20)
        book_repository = BookRepository()
        book_repository.list_books.append(book1)
        book_repository.list_books.append(book2)

        book_repository.down_stock(book2.id)
        book2_stock = book_repository.get_stock(book2.id)
        book1_stock = book_repository.get_stock(book1.id)

        self.assertEqual(book1_stock,1)
        self.assertEqual(book2_stock,0)

    def test_get_book(self):
        book1 = Book(1, "Livro1", "asd", "autor1", "teste1", 15)
        book2 = Book(2, "Livro2", "asd", "autor2", "teste2", 20)
        book3 = Book(3, "Livro2", "asd", "autor2", "teste2", 20)
        book_repository = BookRepository()
        book_repository.list_books.append(book1)
        book_repository.list_books.append(book2)

        livro_existe = book_repository.get_book(book1.id)
        livro_nao_existe = book_repository.get_book(book3.id)


        self.assertEqual(livro_existe,book1)
        self.assertEqual(livro_nao_existe, 'Livro não existe')

    def test_get_stock(self):
        book1 = Book(1, "Livro1", "asd", "autor1", "teste1", 15)
        book2 = Book(2, "Livro2", "asd", "autor2", "teste2", 20)
        book3 = Book(3, "Livro2", "asd", "autor2", "teste2", 20)
        book_repository = BookRepository()
        book_repository.list_books.append(book1)
        book_repository.list_books.append(book2)

        book_repository.down_stock(book1.id)
        book_zero = book_repository.get_stock(book1.id)
        book_um = book_repository.get_stock(book2.id)
        book_dois = book_repository.get_stock(book3.id)

        self.assertEqual(book_zero,0)
        self.assertEqual(book_um,1)
        self.assertFalse(book_dois)

    def test_book_value(self):
        book1 = Book(1, "Livro1", "asd", "autor1", "teste1", 15)
        book2 = Book(2, "Livro2", "asd", "autor2", "teste2", 0)
        book_repository = BookRepository()
        book_repository.list_books.append(book1)
        book_repository.list_books.append(book2)

        book_certo = book_repository.verif_book_value(book1.id)
        book_errado = book_repository.verif_book_value(book2.id)

        self.assertTrue(book_certo)
        self.assertFalse(book_errado)



