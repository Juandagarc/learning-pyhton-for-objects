import json
from .product import Electronic, Food, Clothes


def payment(order_list):
    total = 0
    for order in order_list:
        if order is None:
            continue
        elif order[1] >= 5:
            total += order[0] * order[1] * 0.8
        else:
            total += order[0] * order[1]
    return total


class Shop:
    def __init__(self, data, path):
        self.__data = data
        self.__path = path

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    def add_product(self, category, name, price, stock):
        if category == "Electronic":
            warranty = input("Ingrese la garantia: ")
            product = Electronic(name, price, stock, warranty)
        elif category == "Food":
            expiration_date = input("Ingrese la fecha de vencimiento: ")
            product = Food(name, price, stock, expiration_date)
        elif category == "Clothes":
            size = input("Ingrese la talla: ")
            product = Clothes(name, price, stock, size)
        if category in self.data:
            self.data[category].append(product.json_return())
        else:
            print("Categoria no válida")

    def show_products(self):
        for category in self.data:
            print(f"Categoria: {category}")
            for product in self.data[category]:
                print(f"\tNombre: {product['name']}")
                print(f"\tPrecio: {product['price']}")
                print(f"\tStock: {product['stock']}")
                if category == "Electronic":
                    print(f"\tGarantia: {product['warranty']}")
                elif category == "Food":
                    print(f"\tFecha de vencimiento: {product['expiration_date']}")
                elif category == "Clothes":
                    print(f"\tTalla: {product['size']}")

    def order_product(self, name, stock):
        for category in self.data:
            for product in self.data[category]:
                if product['name'] == name:
                    if product['stock'] >= stock:
                        product['stock'] -= stock
                        return [product['price'], stock]
                    else:
                        return [0, 0]

    def save_products(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file, indent=4)
