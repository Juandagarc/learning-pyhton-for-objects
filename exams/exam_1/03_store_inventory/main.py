import os

data_file = 'store_data.txt'


class Product:
    next_id = 1

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = Product.next_id
        Product.next_id += 1

    def decrease_inventory(self, quantity: int):
        if quantity <= self.quantity:
            self.quantity -= quantity
        else:
            print(f"Not enough inventory for {self.name}.")

    def increase_inventory(self, quantity: int):
        self.quantity += quantity

    def show_info(self):
        return f"Product {self.id}: {self.name}, Price: {self.price}, Quantity in inventory: {self.quantity}"


class Customer:
    next_id = 1

    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        self.id = Customer.next_id
        Customer.next_id += 1

    def make_purchase(self, product: Product, quantity: int):
        total_cost = product.price * quantity
        if self.balance >= total_cost and product.quantity >= quantity:
            self.balance -= total_cost
            product.decrease_inventory(quantity)
            print(f"Purchase successful: {quantity} of {product.name} bought by {self.name}.")
        else:
            print("Purchase failed: Insufficient balance or stock.")

    def show_info(self):
        return f"Customer {self.id}: {self.name}, Balance: {self.balance}"


class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product: Product):
        self.products.append(product)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def make_sale(self, customer_id: int, product_id: int, quantity: int):
        customer = next((cust for cust in self.customers if cust.id == customer_id), None)
        product = next((prod for prod in self.products if prod.id == product_id), None)

        if customer and product:
            customer.make_purchase(product, quantity)
        else:
            print("Sale failed: Customer or Product not found.")

    def show_products(self):
        for product in self.products:
            print(product.show_info())

    def show_customers(self):
        for customer in self.customers:
            print(customer.show_info())

    def save_data(self):
        with open(data_file, 'w') as file:
            # Save products
            file.write("PRODUCTS\n")
            for product in self.products:
                file.write(f"{product.id},{product.name},{product.price},{product.quantity}\n")

            # Save customers
            file.write("CUSTOMERS\n")
            for customer in self.customers:
                file.write(f"{customer.id},{customer.name},{customer.balance}\n")

    def load_data(self):
        if os.path.exists(data_file):
            with open(data_file, 'r') as file:
                section = None
                for line in file:
                    line = line.strip()
                    if line == "PRODUCTS":
                        section = "PRODUCTS"
                        continue
                    elif line == "CUSTOMERS":
                        section = "CUSTOMERS"
                        continue

                    if section == "PRODUCTS":
                        id, name, price, quantity = line.split(',')
                        product = Product(name, float(price), int(quantity))
                        product.id = int(id)
                        self.products.append(product)
                        Product.next_id = max(Product.next_id, product.id + 1)
                    elif section == "CUSTOMERS":
                        id, name, balance = line.split(',')
                        customer = Customer(name, float(balance))
                        customer.id = int(id)
                        self.customers.append(customer)
                        Customer.next_id = max(Customer.next_id, customer.id + 1)


def main():
    store = Store()

    store.load_data()

    while True:
        print("\nMenu:")
        print("1. Add product")
        print("2. Add customer")
        print("3. Make sale")
        print("4. Show products")
        print("5. Show customers")
        print("6. Save data")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity in inventory: "))
            store.add_product(Product(name, price, quantity))
        elif choice == '2':
            name = input("Enter customer name: ")
            balance = float(input("Enter customer balance: "))
            store.add_customer(Customer(name, balance))
        elif choice == '3':
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            store.make_sale(customer_id, product_id, quantity)
        elif choice == '4':
            store.show_products()
        elif choice == '5':
            store.show_customers()
        elif choice == '6':
            store.save_data()
        else:
            print("Invalid option.")


main()
