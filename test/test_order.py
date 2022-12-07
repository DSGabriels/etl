import unittest
from datetime import datetime

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository


class TestGeral(unittest.TestCase):
    def test_if_order_exist(self):
        customer1 = Customer(1, "grabiel")
        customer_repository = CustomerRepository()
        customer_repository.list_customers.append(customer1)

        book1 = Book(1, "Livro1", "asd", "autor1", "teste1", 15)
        book2 = Book(2, "Livro2", "asd", "autor2", "teste2", 20)
        book_repository = BookRepository()
        book_repository.list_books.append(book1)

        # Act
        order_repository = OrderRepository()
        order1 = Order(1, customer1, datetime.today())
        order1.purchased_book = book1
        order2 = Order(2, customer1, datetime.today())
        order2.purchased_book = book2
        order_repository.list_orders.append(order1)
        order_existe = order_repository.verif_if_order_exists(order1.id)
        order_nao_existe = order_repository.verif_if_order_exists(order2.id)

        # Assert
        self.assertTrue(order_existe)
        self.assertFalse(order_nao_existe)
