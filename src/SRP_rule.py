# Naruszona zasada SRP

class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer

class ValidateOrder:
    def _validate_order(self):
        print("Walidacja zamowienia.")

class SaveOrder:
    def _save_order_to_database(self):
        print("Zapisywanie zamowienia do bazy danych.")

class SendOrder:
    def _send_confirmation_email(self):
        print("Wysylanie e-maila potwierdzajacego.")


class OrderProcessor(ValidateOrder,SaveOrder,SendOrder):
    def __init__(self, order):
        self.order = order

    def process_order(self):
        self._validate_order()
        self._save_order_to_database()
        self._send_confirmation_email()

order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(order)
processor.process_order()