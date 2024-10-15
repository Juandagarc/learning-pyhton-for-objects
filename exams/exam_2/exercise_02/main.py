from modules.hotels import Hotel, Simple, Double, Suite
from modules.save import HotelDataManager


def create_hotel():
    data_manager = HotelDataManager()
    data = data_manager.load_data()

    hotel_data = data.get("hotel", {})
    hotel_name = hotel_data.get("name", "Hotel Sin Nombre")
    rooms_data = hotel_data.get("rooms", [])

    hotel = Hotel(hotel_name, [])

    for room in rooms_data:
        if room["type"] == "Simple":
            hotel.rooms.append(Simple(room["number"], room["price"], room["state"]))
        elif room["type"] == "Double":
            hotel.rooms.append(Double(room["number"], room["price"], room["state"], room["services"]))
        elif room["type"] == "Suite":
            hotel.rooms.append(Suite(room["number"], room["price"], room["state"], room["services"]))

    return hotel, data_manager


def menu(hotel, data_manager):
    while True:
        print("\n--- Menú del Hotel ---")
        print("1. Hacer una reserva")
        print("2. Calcular el precio total de una estadía")
        print("3. Ver habitaciones disponibles")
        print("4. Ver servicios de una habitación")
        print("5. Salir")

        option = input("Selecciona una opción (1-5): ")

        if option == '1':
            room_number = int(input("Ingresa el número de la habitación: "))
            print(hotel.make_reservation(room_number))
        elif option == '2':
            room_number = int(input("Ingresa el número de la habitación: "))
            nights = int(input("Ingresa el número de noches: "))
            print(hotel.total_price(room_number, nights))
        elif option == '3':
            print("Habitaciones disponibles:", hotel.get_available_rooms())
        elif option == '4':
            room_number = int(input("Ingresa el número de la habitación: "))
            room = hotel.get_room(room_number)
            if room:
                print("Servicios de la habitación:", room.services)
            else:
                print(f"La habitación {room_number} no existe.")
        elif option == '5':
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def main():
    hotel, data_manager = create_hotel()
    print(hotel.name)

    menu(hotel, data_manager)
    data_manager.save_data(hotel)


if __name__ == "__main__":
    main()
