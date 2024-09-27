def catalogar(vehiculos, numero_ruedas):
    # retorna los vehiculos con x cantidad de ruedas
    contador = 0
    for vehiculo in vehiculos:
        if vehiculo.ruedas == numero_ruedas:
            contador += 1
    return contador


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad  # km/h
        self.cilindrada = cilindrada  # cm³


class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad  # km/h
        self.cilindrada = cilindrada  # cm³


class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga  # kg


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo  # Puede ser urbana o deportiva


def main():
    # se crea un objeto de cada clase
    coche = Coche("Rojo", 4, 180, 2000)
    moto = Motocicleta('azul', 2, 120, 150)
    camioneta = Camioneta('Blanco', 6, 2000)
    bicicleta = Bicicleta('naranja', 2, 'urbana')
    vehiculos = [coche, moto, camioneta, bicicleta]
    for i in range(2, 7, 2):
        print("Se han encontrado {} vehículos con {} ruedas:".format(catalogar(vehiculos, i), i))


main()
