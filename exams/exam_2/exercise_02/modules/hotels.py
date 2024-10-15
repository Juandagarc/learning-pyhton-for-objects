from .rooms import Simple, Double, Suite


class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def get_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room
        return None

    def get_available_rooms(self):
        available_rooms = [room.number for room in self.rooms if room.state]
        if available_rooms:
            return available_rooms
        return "No available rooms"

    def make_reservation(self, room_number):
        room = self.get_room(room_number)
        if room:
            if room.state:  # Assuming state True means available
                room.state = False  # Mark room as reserved
                return f"Room number {room_number} successfully reserved"
            else:
                return f"Room number {room_number} is not available"
        return f"Room number {room_number} does not exist"

    def total_price(self, room_number, nights):
        room = self.get_room(room_number)
        if room:
            return room.price * nights
        return f"Room number {room_number} does not exist"


