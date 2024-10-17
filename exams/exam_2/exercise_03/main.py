from modules.shop import Shop, payment
import json

path = 'data.json'


def load_products(path):
    with open(path, 'r') as file:
        return json.load(file)


def main():
    data = load_products(path)
    shop = Shop(data, path)  # We create the shop object
    while True:
        print("Que desea hacer?")
        print("1. Mostrar productos")
        print("2. Comprar productos")
        print("3. Agregar productos")
        print("4. Salir")
        option = input("Ingrese la opcion: ")
        if option == "1":
            shop.show_products()
        elif option == "2":
            order_list = []
            print("Ingrese los productos que desea comprar")
            while True:
                name = input("Ingrese el nombre del producto: ")
                stock = int(input("Ingrese la cantidad: "))
                order = shop.order_product(name, stock)
                if order == [0, 0] or order is None:
                    print("No es posible realizar la compra por falta de cantidad o porque no tenemos el producto")
                else:
                    order_list.append(order)
                print("Desea agregar otro producto? (s/n)")
                add = input()
                if add == "n":
                    break
            total = payment(order_list)
            print(f"El total a pagar es: {total}")
        elif option == "3":
            print("Ingrese los datos del producto")
            print("Categorias: Electronic, Food, Clothes")
            category = input("Ingrese la categoria: ")
            name = input("Ingrese el nombre: ")
            price = float(input("Ingrese el precio: "))
            stock = int(input("Ingrese el stock: "))
            shop.add_product(category, name, price, stock)
        elif option == "4":
            print("Guardando productos...")
            shop.save_products()
            print("Productos guardados")
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()
