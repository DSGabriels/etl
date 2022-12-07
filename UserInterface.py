from datetime import date
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository

class UserInterface:
    def __init__(self, customer_repository : CustomerRepository, book_repository : BookRepository, order_repository : OrderRepository) -> None:
        self.customer_repository = customer_repository
        self.book_repository = book_repository
        self.order_repository = order_repository

    def main_menu(self) -> int:
        try:
            print("1 - Cadastrar cliente")
            print("2 - Fazer pedido")
            print("3 - Relatório de Pedidos")
            print("4 - Relatório de Clientes")
            print("5 - Relatório de Livros")
            print("0 - Sair")
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0

    def register_new_customer(self):
        try:
            id = int(input("Informe o código do cliente: "))
            if self.customer_repository.verif_if_customer_exists(id):
                return "Cliente já existe"
            nome = input("Informe o nome do cliente: ")
            if nome == "":
                return "Nome do cliente está em branco"
            customer = Customer(id, nome)
            self.customer_repository.list_customers.append(customer)
            return "Client cadastrado com sucesso!"
        except:
            return "Alguma informação está invalida ou em branco, tente novamente"

    def selling_book(self):
        try:
            id = int(input("Informe o código do pedido: "))
            customer_id = int(input("Informe o código do cliente: "))
            book_id = int(input("Informe o código do livro: "))
            today = date.today()
            book = self.book_repository.get_book(book_id)

            validate_sell_result = self.verify_if_sell_is_possible(customer_id, id, book)
            if validate_sell_result != True:
                print(validate_sell_result)
                return "Algo deu errado :/"

            customer = self.customer_repository.get_customer(customer_id)
            order = Order(id, customer, today)
            order.purchased_book = book
            self.book_repository.down_stock(book_id)

            self.order_repository.list_orders.append(order)
            return "Pedido cadastrado com sucesso!"
        except:
            return "Algo deu errado, tente novamente"

    def verify_if_sell_is_possible(self, order_id, customer_id, book):
        if self.order_repository.verif_if_order_exists(order_id):
            return "Pedido já existe"

        if not self.customer_repository.verif_if_customer_exists(customer_id):
            return "Cliente não existe"

        if not self.book_repository.verif_if_book_exists(book.id):
            return "Livro não cadastrado"

        if self.book_repository.get_stock(book.id) <= 0:
            return "Livro esgotado"

        if not self.book_repository.verif_book_value(book.id):
            return "Livro com preço invalido"


        return True

    def show_all_orders(self):
        print("\n***** Relatório de pedidos *****\n")
        for order in self.order_repository.list_orders:
            print(f"Código do Pedido: {order.id}")
            print(f"Cliente: {order.customer.name}")
            print(f"Data do pedido: {order.date_order}")
            print(f"Livro escolhido: {order.purchased_book.name} \n")

    def show_all_customers(self):
        formatText = "{0:<10} {1:<20}\n"
        menu = ("\n***** Relatório de clientes *****\n")
        menu += formatText.format("Id", "Cliente")

        for customer in self.customer_repository.list_customers:
            menu += formatText.format(customer.id, customer.name)
        print(menu)

    def show_all_books(self):
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<20}\n"
        menu = ("\n***** Relatório de livros cadastrados *****\n")
        menu += formatText.format("Id", "Título", "ISBN",
                                  "Autor", "Assunto", "Valor", "Estoque")

        for book in self.book_repository.list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                      book.author, book.category, book.price, book.stock)
        print(menu)