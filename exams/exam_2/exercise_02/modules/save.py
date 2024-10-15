import json


class HotelDataManager:
    def __init__(self, path='data.json'):
        self.path = path

    def load_data(self):
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {"name": "Hotel Sin Nombre", "rooms": []}  # Hotel vacío por defecto

    def save_data(self, hotel):
        data = {
            "hotel": {
                "name": hotel.name,
                "rooms": []
            }
        }

        for room in hotel.rooms:
            room_data = {
                "type": room.__class__.__name__,  # "Simple", "Double", "Suite
                "number": room.number,
                "price": room.price,
                "state": room.state,
                "capacity": room.capacity,
                "services": room.services
            }
            data["hotel"]["rooms"].append(room_data)

        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)
