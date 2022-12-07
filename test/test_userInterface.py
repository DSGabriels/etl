from datetime import datetime
from unittest import mock
from entities.book import Book
from entities.order import Order
from entities.customer import Customer
from UserInterface import UserInterface
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
import unittest


class TestGeral(unittest.TestCase):
    def test_registration(self):
        with mock.patch('builtins.input', side_effect=[2,"asd",2]):
            user = UserInterface(CustomerRepository(), BookRepository(), OrderRepository())
            user_input = user.register_new_customer()
            user_input2 = user.register_new_customer()


            self.assertEqual(user_input, "Client cadastrado com sucesso!")
            self.assertEqual(user_input2, "Cliente já existe")

    def test_validate_sell(self):
        customer_repository = CustomerRepository()
        book_repository = BookRepository()
        order_repository = OrderRepository()
        user_interface = UserInterface(customer_repository, book_repository, order_repository)

        customer1 = Customer(1,'c1')
        customer_repository.list_customers.append(customer1)

        book1 = Book(1, "Livro1", "a", "autor1", "tipo1", 10)
        book2 = Book(2, "Livro2", "b", "autor2","tipo2", 15)
        book3 = Book(3, "Livro3", "c", "autor3", "tipo3", 20)
        book4 = Book(4, "Livro4", "d", "autor4","tipo4", 0)
        book_repository.list_books.append(book4)
        book_repository.list_books.append(book2)
        book_repository.list_books.append(book3)

        book_repository.down_stock(book3.id)

        order1 = Order(1,customer1,datetime.today())
        order_repository.list_orders.append(order1)

        book_not_exist = user_interface.verify_if_sell_is_possible(2,customer1.id,book1)
        book_zeroed = user_interface.verify_if_sell_is_possible(2,customer1.id,book3)
        book_invalid_price = user_interface.verify_if_sell_is_possible(2,customer1.id,book4)
        invalid_order = user_interface.verify_if_sell_is_possible(order1.id,customer1.id,book2)
        invalid_customer = user_interface.verify_if_sell_is_possible(2,2,book1)

        self.assertEqual(book_not_exist, "Livro não cadastrado")
        self.assertEqual(book_zeroed, "Livro esgotado")
        self.assertEqual(book_invalid_price, "Livro com preço invalido")
        self.assertEqual(invalid_order, "Pedido já existe")
        self.assertEqual(invalid_customer, "Cliente não existe")




def test_selling(monkeypatch):
    #   Me ajudaram nesse teste aqui, por isso quebrei o padrão do Unittest #
    customer_repository = CustomerRepository()
    book_repository = BookRepository()
    order_repository = OrderRepository()
    user_interface = UserInterface(customer_repository, book_repository, order_repository)

    book1 = Book(1, "livro1", "a", "autor1", "tipo1", 15)
    book_repository.list_books.append(book1)

    customer1 = Customer(1, "c1")
    customer_repository.list_customers.append(customer1)

    inputs = iter([1, customer1.id, book1.id])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    vendido = user_interface.selling_book()

    inputs = iter([2, 2, 2])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    nao_vendido = user_interface.selling_book()

    assert vendido == "Pedido cadastrado com sucesso!"
    assert nao_vendido == "Algo deu errado :/"
    #   Me ajudaram nesse teste aqui, por isso quebrei o padrão do Unittest #

