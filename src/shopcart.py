class ShoppingCart:

    def __init__(self):
        self.products = []
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        """Dodawanie produktu do koszyka"""
        if not product_name or not price or not  quantity:
            return False
        self.products.append({"name": product_name, "price": price, "quantity": quantity})

        return True
        pass

    def remove_product(self, product_name: str) -> bool:
        """Usuwanie produktu z koszyka"""
        for product in self.products:
            if product["name"] == product_name:
                self.products.remove(product)
                return True
        return False
        pass

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        """Aktualizacja iloĹci produktu w koszyku"""
        if new_quantity < 0:
            return False
        for product in self.products:
            if product["name"] == product_name:
                product["quantity"] = new_quantity
                return True
        return False
        pass

    def get_products(self):
        """Pobieranie nazw produktĂłw z koszyka"""
        result = [(product["name"]) for product in self.products]
        if result == []:
            raise ValueError("Brak produktów")
        return result
        pass

    def count_products(self) -> int:
        """Pobieranie liczby produktĂłw znajdujÄcych siÄ w koszyku"""
        return sum(product["quantity"] for product in self.products)
        pass

    def get_total_price(self) -> int:
        """Pobieranie sumy cen produktĂłw w koszyku"""
        return sum(product["price"] * product["quantity"] for product in self.products)
        pass

    def apply_discount_code(self, discount_code: str) -> bool:
        """Zastosowanie kuponu rabatowego"""
        valid_discount_codes = {"SAVE10": 0.10, "SAVE20": 0.20}
        if discount_code in valid_discount_codes:
            self.discount = valid_discount_codes[discount_code]
            return True
        return False
        pass

    def checkout(self) -> bool:
        """Realizacja zamĂłwienia"""
        if not self.products:
            return False
        self.products.clear()
        return True
        pass