import unittest

from entities.customer import Customer
from repositories.customer_repository import CustomerRepository


class TestGeral(unittest.TestCase):

    def test_verif_if_customer_exist(self):
        customer1 = Customer(1, "c1")
        customer2 = Customer(2, "c2")
        customer_repository = CustomerRepository()
        customer_repository.list_customers.append(customer1)
        customer_true = customer_repository.verif_if_customer_exists(customer1.id)
        customer_false = customer_repository.verif_if_customer_exists(customer2.id)

        self.assertTrue(customer_true)
        self.assertFalse(customer_false)

    def test_get_customer(self):
        customer1 = Customer(1, "c1")
        customer2 = Customer(2, "c2")
        customer_repository = CustomerRepository()
        customer_repository.list_customers.append(customer1)

        cadastrado = customer_repository.get_customer(customer1.id)
        nao_cadastrado = customer_repository.get_customer(customer2.id)

        self.assertEqual(cadastrado,customer1)
        self.assertEqual(nao_cadastrado, 'Cliente não existe')




