from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.book_repository import BookRepository
from books_import import AllBooks
from UserInterface import UserInterface

book_repository = BookRepository()
all_books = AllBooks(book_repository)
all_books.import_books()
customer_repository = CustomerRepository()
order_repository = OrderRepository()
user_interface = UserInterface(customer_repository, book_repository, order_repository)


while True:
    menu_option = user_interface.main_menu()
    if menu_option == 0:
        break

    print("\n")

    if menu_option == 1:
        print(user_interface.register_new_customer())
    if menu_option == 2:
        print(user_interface.selling_book())
    if menu_option == 3:
        user_interface.show_all_orders()
    if menu_option == 4:
        user_interface.show_all_customers()
    if menu_option == 5:
        user_interface.show_all_books()
