from entities.customer import Customer


class CustomerRepository:
    def __init__(self) -> None:
        self.list_customers: list[Customer] = []

    def verif_if_customer_exists(self, id) -> bool:
        for item in self.list_customers:
            if id == item.id:
                return True

        return False

    def get_customer(self, id):
        for item in self.list_customers:
            if id == item.id:
                return item

        return 'Cliente não existe'