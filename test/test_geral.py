import unittest
from datetime import datetime

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository


class TestGeral(unittest.TestCase):
    def test_geral(self):
        customer1 = Customer(1, "grabiel")
        customer_repository = CustomerRepository()
        customer_repository.list_customers.append(customer1)

        book1 = Book(1,"Livro1", "asd", "autor1", "teste1", 15)
        book2 = Book(2, "Livro2", "asd", "autor2", "teste2", 20)
        book3 = Book(3, "Livro2", "asd", "autor2", "teste2", 20)
        book_repository = BookRepository()
        book_repository.list_books.append(book1)
        book_repository.list_books.append(book2)

        # Act
        order_repository = OrderRepository()
        order1 = Order(1, customer1, datetime.today())
        order1.purchased_book = book2
        order_repository.list_orders.append(order1)
        book_repository.down_stock(book2.id)
        book2_stock = book_repository.get_stock(book2.id)
        book1_stock = book_repository.get_stock(book1.id)

        book_false = book_repository.verif_if_book_exists(3)
        book_true = book_repository.verif_if_book_exists(2)

        # Assert
        self.assertEqual(book1_stock,1)
        self.assertEqual(book2_stock,0)
        self.assertEqual(book_false, False)
        self.assertEqual(book_true, True)
        self.assertEqual(order1.id,1)
