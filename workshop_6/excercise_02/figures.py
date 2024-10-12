class Figure:
    def __init__(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self._width = None
        self._height = None
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive number")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive number")

    def area(self):
        return self._width * self._height


class Triangle(Figure):
    def __init__(self, base, height):
        super().__init__()
        self._base = None
        self._height = None
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if value > 0:
            self._base = value
        else:
            raise ValueError("Base must be a positive number")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive number")

    def area(self):
        return (self._base * self._height) / 2


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self._radius = None
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be a positive number")

    def area(self):
        import math
        return math.pi * (self._radius ** 2)


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self._side = None
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
        else:
            raise ValueError("Side must be a positive number")

    def area(self):
        return self._side ** 2
