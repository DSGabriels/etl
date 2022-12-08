import unittest
from datetime import datetime
from books_import import AllBooks
from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository


class TestGeral(unittest.TestCase):
    def test_format(self):
       valor_livro1 = AllBooks.format_str_price_to_float("R$ 52.0")
       valor_livro2 = AllBooks.format_str_price_to_float("R$50,00")

       self.assertEqual(valor_livro1,52.0)
       self.assertEqual(valor_livro2,0)
