class Figura:
    def area(self):
        raise NotImplementedError("This method should be implemented by subclasses")


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        import math
        return math.pi * (self.radio ** 2)


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


rectangulo = Rectangulo(4, 5)
triangulo = Triangulo(6, 7)
circulo = Circulo(3)
cuadrado = Cuadrado(4)

print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Área del triángulo: {triangulo.area()}")
print(f"Área del círculo: {circulo.area()}")
print(f"Área del cuadrado: {cuadrado.area()}")
