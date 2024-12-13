class Order:
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    def set_order_id(self, order_id):
        self.order_id = order_id

    def get_order_id(self):
        return self.order_id

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_customer_name(self):
        return self.customer_name

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def display_order(self):
        print(f"ID заказа: {self.order_id}, Клиент: {self.customer_name}, Сумма: {self.amount}")


class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print("Заказ добавлен.")

    def remove_order(self, order_id):
        order = self.find_order(order_id)
        if order:
            self.orders.remove(order)
            print(f"Заказ с ID {order_id} удален.")
        else:
            print(f"Заказ с ID {order_id} не найден.")

    def find_order(self, order_id):
        for order in self.orders:
            if order.get_order_id() == order_id:
                return order
        return None

    def display_all_orders(self):
        if not self.orders:
            print("Список заказов пуст.")
        else:
            print("Список заказов:")
            for order in self.orders:
                order.display_order()


def main():
    manager = OrderManager()

    while True:
        command = input("Введите команду (добавить, удалить, найти, показать, выход): ").strip().lower()

        if command == "добавить":
            order_id = input("Введите идентификатор заказа: ")
            customer_name = input("Введите имя клиента: ")
            amount = float(input("Введите сумму заказа: "))
            order = Order(order_id, customer_name, amount)
            manager.add_order(order)

        elif command == "удалить":
            order_id = input("Введите идентификатор заказа: ")
            manager.remove_order(order_id)

        elif command == "найти":
            order_id = input("Введите идентификатор заказа: ")
            order = manager.find_order(order_id)
            if order:
                order.display_order()
            else:
                print(f"Заказ с ID {order_id} не найден.")

        elif command == "показать":
            manager.display_all_orders()

        elif command == "выход":
            print("Выход из программы.")
            break

        else:
            print("Неверная команда. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
