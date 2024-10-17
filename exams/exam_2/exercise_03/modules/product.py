class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock

class Electronic(Product):
    def __init__(self, name, price, stock, warranty):
        super().__init__(name, price, stock)
        self.__warranty = warranty

    @property
    def warranty(self):
        return self.__warranty

    @warranty.setter
    def warranty(self, warranty):
        self.__warranty = warranty

    def json_return(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "warranty": self.warranty
        }

class Food(Product):
    def __init__(self, name, price, stock, expiration_date):
        super().__init__(name, price, stock)
        self.__expiration_date = expiration_date

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    def json_return(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "expiration_date": self.expiration_date
        }

class Clothes(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def json_return(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "size": self.size
        }