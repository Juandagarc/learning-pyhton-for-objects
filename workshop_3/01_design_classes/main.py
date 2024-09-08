# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style


class Avion:
    def __init__(self, modelo, capacidad, aerolinea, autonomia):
        self.modelo = modelo
        self.capacidad = capacidad
        self.aerolinea = aerolinea
        self.autonomia = autonomia

    def descripcion(self):
        return f"Avión modelo {self.modelo}, de la aerolínea {self.aerolinea} con capacidad de {self.capacidad} pasajeros."

    def es_de_largo_alcance(self):
        return self.autonomia > 10000


class Celular:
    def __init__(self, marca, modelo, almacenamiento, ram):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram

    def descripcion(self):
        return f"Celular {self.marca} {self.modelo} con {self.almacenamiento}GB de almacenamiento y {self.ram}GB de RAM."

    def es_gama_alta(self):
        return self.ram >= 8 and self.almacenamiento >= 128


class Asignatura:
    def __init__(self, nombre, profesor, creditos, duracion):
        self.nombre = nombre
        self.profesor = profesor
        self.creditos = creditos
        self.duracion = duracion

    def descripcion(self):
        return f"Asignatura: {self.nombre}, impartida por {self.profesor}."

    def es_curso_intensivo(self):
        return self.duracion < 4


class Ejercito:
    def __init__(self, nombre, pais, numero_soldados, rango_maximo):
        self.nombre = nombre
        self.pais = pais
        self.numero_soldados = numero_soldados
        self.rango_maximo = rango_maximo

    def descripcion(self):
        return f"Ejército {self.nombre} de {self.pais} con {self.numero_soldados} soldados."

    def es_poderoso(self):
        return self.numero_soldados > 50000


class Silla:
    def __init__(self, material, color, tipo, peso_maximo):
        self.material = material
        self.color = color
        self.tipo = tipo
        self.peso_maximo = peso_maximo

    def descripcion(self):
        return f"Silla de {self.material} color {self.color}, tipo: {self.tipo}."

    def es_resistente(self):
        return self.peso_maximo >= 120


class Audifonos:
    def __init__(self, marca, tipo, cancelacion_ruido, duracion_bateria):
        self.marca = marca
        self.tipo = tipo
        self.cancelacion_ruido = cancelacion_ruido
        self.duracion_bateria = duracion_bateria

    def descripcion(self):
        return f"Audífonos {self.marca}, tipo: {self.tipo}, cancelación de ruido: {self.cancelacion_ruido}."

    def es_bateria_duradera(self):
        return self.duracion_bateria > 20


def main():
    separador = Fore.MAGENTA + '--------------------------------------------------' + Style.RESET_ALL

    avion = Avion("Boeing 747", 416, "American Airlines", 13600)
    print(Fore.YELLOW + avion.descripcion() + Style.RESET_ALL)
    print(separador)

    celular = Celular("Apple", "iPhone 13", 256, 8)
    print(Fore.YELLOW + celular.descripcion() + Style.RESET_ALL)
    print(separador)

    asignatura = Asignatura("Matemáticas", "Dr. Juan Gómez", 5, 3)
    print(Fore.YELLOW + asignatura.descripcion() + Style.RESET_ALL)
    print(separador)

    ejercito = Ejercito("Armada", "EE.UU.", 100000, "General")
    print(Fore.YELLOW + ejercito.descripcion() + Style.RESET_ALL)
    print(separador)

    silla = Silla("Madera", "Negro", "Oficina", 150)
    print(Fore.YELLOW + silla.descripcion() + Style.RESET_ALL)
    print(separador)

    audifonos = Audifonos("Sony", "Inalámbricos", "Sí", 30)
    print(Fore.YELLOW + audifonos.descripcion() + Style.RESET_ALL)
    print(separador)


main()
