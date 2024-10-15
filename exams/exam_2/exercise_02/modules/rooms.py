class Room:
    def __init__(self, number: int, price: float, state: bool, capacity: int, services: list):
        self._number = number
        self._price = price
        self._state = state
        self._capacity = capacity
        self._services = services

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value > 0:
            self._number = value
        else:
            raise ValueError("Room number must be a positive integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price must be a positive number")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if isinstance(value, bool):
            self._state = value
        else:
            raise ValueError("State must be a boolean value")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if isinstance(value, int) and value > 0:
            self._capacity = value
        else:
            raise ValueError("Capacity must be a positive integer")

    @property
    def services(self):
        if not self._services:
            return "No services provided"
        return self._services

    @services.setter
    def services(self, value):
        if isinstance(value, list):
            self._services = value
        else:
            raise ValueError("Services must be a list")


class Simple(Room):
    def __init__(self, number: int, price: float, state: bool):
        super().__init__(number, price, state, 1, [])


class Double(Room):
    def __init__(self, number: int, price: float, state: bool, services: list):
        super().__init__(number, price, state, 2, services)


class Suite(Room):
    def __init__(self, number: int, price: float, state: bool, services: list):
        super().__init__(number, price, state, 4, services)
