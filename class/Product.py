class Продукт:
    def __init__(self, назва, ціна, кількість):
        self._name = назва
        self._price = ціна
        self._quantity = кількість

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def set_price(self, ціна):
        self._price = ціна

    def set_quantity(self, кількість):
        self._quantity = кількість

    def __repr__(self):
        return f"Продукт(назва='{self._name}', ціна={self._price}, кількість={self._quantity})"


class Склад(Продукт):
    def __init__(self):
        self._products = []

    def add_product(self, продукт):
        self._products.append(продукт)

    def find_by_name(self, назва):
        return [продукт for продукт in self._products if продукт.get_name() == назва]

    def find_by_price_range(self, min_price, max_price):
        return [продукт for продукт in self._products if min_price <= продукт.get_price() <= max_price]

    def get_all_products(self):
        return self._products

    def remove_product(self, продукт):
        if продукт in self._products:
            self._products.remove(продукт)

    @staticmethod
    def get_total_quantity(products):
        return sum(продукт.get_quantity() for продукт in products)

    def __get_total_value(self, products):
        return sum(продукт.get_price() * продукт.get_quantity() for продукт in products)

    # Метод для доступу до приватного методу (якщо потрібно)
    def get_total_value(self, products):
        return self.__get_total_value(products)