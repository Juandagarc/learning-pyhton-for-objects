# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style

# Json module is used to load data from file
import json

path = 'data.json'


def load_data():
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


class Libro:
    def __init__(self, titulo, autor, isbn, publicacion, genero):
        self.id = len(load_data().get("Libros", []))
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.publicacion = publicacion
        self.genero = genero

    def resumen(self):
        return f"'{self.titulo}' by {self.autor}, ISBN: {self.isbn}"

    def es_favorito(self):
        return self.genero.lower() in ['ciencia ficción', 'fantasía']

    def save_data(self):
        data = load_data()
        if "Libros" not in data:
            data["Libros"] = []

        data["Libros"].append({
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "publicacion": self.publicacion,
            "genero": self.genero
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Casa:
    def __init__(self, direccion, habitaciones, banos, metros_cuadrados, tipo):
        self.id = len(load_data().get("Casas", []))
        self.direccion = direccion
        self.habitaciones = habitaciones
        self.banos = banos
        self.metros_cuadrados = metros_cuadrados
        self.tipo = tipo

    def descripcion(self):
        return f"Casa en {self.direccion}, {self.habitaciones} habitaciones, {self.banos} baños."

    def es_grande(self):
        return self.metros_cuadrados > 200

    def save_data(self):
        data = load_data()
        if "Casas" not in data:
            data["Casas"] = []

        data["Casas"].append({
            "id": self.id,
            "direccion": self.direccion,
            "habitaciones": self.habitaciones,
            "banos": self.banos,
            "metros_cuadrados": self.metros_cuadrados,
            "tipo": self.tipo
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Pelicula:
    def __init__(self, titulo, director, duracion, genero, estreno):
        self.id = len(load_data().get("Peliculas", []))
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        self.genero = genero
        self.estreno = estreno

    def es_larga(self):
        return self.duracion > 120

    def descripcion(self):
        return f"Pelicula: {self.titulo}, dirigida por {self.director}"

    def save_data(self):
        data = load_data()
        if "Peliculas" not in data:
            data["Peliculas"] = []

        data["Peliculas"].append({
            "id": self.id,
            "titulo": self.titulo,
            "director": self.director,
            "duracion": self.duracion,
            "genero": self.genero,
            "estreno": self.estreno
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Bodega:
    def __init__(self, ubicacion, tamano, capacidad, tipo, precio):
        self.id = len(load_data().get("Bodegas", []))
        self.ubicacion = ubicacion
        self.tamano = tamano
        self.capacidad = capacidad
        self.tipo = tipo
        self.precio = precio

    def descripcion(self):
        return f"Bodega en {self.ubicacion}, {self.tamano}m²"

    def es_economica(self):
        return self.precio < 1000

    def save_data(self):
        data = load_data()
        if "Bodegas" not in data:
            data["Bodegas"] = []

        data["Bodegas"].append({
            "id": self.id,
            "ubicacion": self.ubicacion,
            "tamano": self.tamano,
            "capacidad": self.capacidad,
            "tipo": self.tipo,
            "precio": self.precio
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Lampara:
    def __init__(self, marca, tipo, voltaje, potencia, color):
        self.id = len(load_data().get("Lamparas", []))
        self.marca = marca
        self.tipo = tipo
        self.voltaje = voltaje
        self.potencia = potencia
        self.color = color

    def es_ahorradora(self):
        return self.potencia < 15

    def descripcion(self):
        return f"Lámpara {self.marca}, tipo: {self.tipo}, color: {self.color}"

    def save_data(self):
        data = load_data()
        if "Lamparas" not in data:
            data["Lamparas"] = []

        data["Lamparas"].append({
            "id": self.id,
            "marca": self.marca,
            "tipo": self.tipo,
            "voltaje": self.voltaje,
            "potencia": self.potencia,
            "color": self.color
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Modem:
    def __init__(self, marca, velocidad, tipo, puerto, precio):
        self.id = len(load_data().get("Modems", []))
        self.marca = marca
        self.velocidad = velocidad
        self.tipo = tipo
        self.puerto = puerto
        self.precio = precio

    def es_rapido(self):
        return self.velocidad > 100

    def descripcion(self):
        return f"Modem {self.marca}, velocidad: {self.velocidad}Mbps"

    def save_data(self):
        data = load_data()
        if "Modems" not in data:
            data["Modems"] = []

        data["Modems"].append({
            "id": self.id,
            "marca": self.marca,
            "velocidad": self.velocidad,
            "tipo": self.tipo,
            "puerto": self.puerto,
            "precio": self.precio
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Router:
    def __init__(self, marca, velocidad, tipo, rango, puerto):
        self.id = len(load_data().get("Routers", []))
        self.marca = marca
        self.velocidad = velocidad
        self.tipo = tipo
        self.rango = rango
        self.puerto = puerto

    def es_bueno_para_juegos(self):
        return self.velocidad > 300 and self.rango > 50

    def descripcion(self):
        return f"Router {self.marca}, velocidad: {self.velocidad}Mbps"

    def save_data(self):
        data = load_data()
        if "Routers" not in data:
            data["Routers"] = []

        data["Routers"].append({
            "id": self.id,
            "marca": self.marca,
            "velocidad": self.velocidad,
            "tipo": self.tipo,
            "rango": self.rango,
            "puerto": self.puerto
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Maletin:
    def __init__(self, marca, material, tamano, compartimientos, color):
        self.id = len(load_data().get("Maletines", []))
        self.marca = marca
        self.material = material
        self.tamano = tamano
        self.compartimientos = compartimientos
        self.color = color

    def es_para_viaje(self):
        return self.tamano > 15

    def descripcion(self):
        return f"Maletín {self.marca}, material: {self.material}, color: {self.color}"

    def save_data(self):
        data = load_data()
        if "Maletines" not in data:
            data["Maletines"] = []

        data["Maletines"].append({
            "id": self.id,
            "marca": self.marca,
            "material": self.material,
            "tamano": self.tamano,
            "compartimientos": self.compartimientos,
            "color": self.color
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class PacienteOncologico:
    def __init__(self, nombre, edad, diagnostico, tratamiento, pronostico):
        self.id = len(load_data().get("Pacientes", []))
        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.pronostico = pronostico

    def es_alto_riesgo(self):
        return self.pronostico.lower() == "reservado"

    def descripcion(self):
        return f"Paciente: {self.nombre}, diagnóstico: {self.diagnostico}"

    def save_data(self):
        data = load_data()
        if "Pacientes" not in data:
            data["Pacientes"] = []

        data["Pacientes"].append({
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento,
            "pronostico": self.pronostico
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


class Gato:
    def __init__(self, nombre, edad, raza, color, peso):
        self.id = len(load_data().get("Gatos", []))
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color
        self.peso = peso

    def maullar(self):
        return f"{self.nombre} está maullando."

    def es_joven(self):
        return self.edad < 2

    def save_data(self):
        data = load_data()
        if "Gatos" not in data:
            data["Gatos"] = []

        data["Gatos"].append({
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "raza": self.raza,
            "color": self.color,
            "peso": self.peso
        })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


def main():
    separador = Fore.MAGENTA + '--------------------------------------------------' + Style.RESET_ALL
    # Crear un ejemplo para cada clase y guardar los datos
    libro = Libro("1984", "George Orwell", "123456789", "1949", "Ciencia Ficción")
    libro.save_data()
    print(Fore.YELLOW + libro.resumen() + Style.RESET_ALL)
    print(separador)

    casa = Casa("123 Calle Falsa", 4, 3, 250, "Residencial")
    casa.save_data()
    print(Fore.YELLOW + casa.descripcion() + Style.RESET_ALL)
    print(separador)

    pelicula = Pelicula("Inception", "Christopher Nolan", 148, "Ciencia Ficción", "2010")
    pelicula.save_data()
    print(Fore.YELLOW + pelicula.descripcion() + Style.RESET_ALL)
    print(separador)

    bodega = Bodega("Zona Industrial", 500, 10000, "Almacenamiento", 1500)
    bodega.save_data()
    print(Fore.YELLOW + bodega.descripcion() + Style.RESET_ALL)
    print(separador)

    lampara = Lampara("Philips", "LED", 110, 10, "Blanco")
    lampara.save_data()
    print(Fore.YELLOW + lampara.descripcion() + Style.RESET_ALL)
    print(separador)

    modem = Modem("TP-Link", 150, "ADSL", 1, 50)
    modem.save_data()
    print(Fore.YELLOW + modem.descripcion() + Style.RESET_ALL)
    print(separador)

    router = Router("Netgear", 400, "WiFi", 100, 4)
    router.save_data()
    print(Fore.YELLOW + router.descripcion() + Style.RESET_ALL)

    maletin = Maletin("Samsonite", "Cuero", 20, 5, "Negro")
    maletin.save_data()
    print(Fore.YELLOW + maletin.descripcion() + Style.RESET_ALL)
    print(separador)

    paciente = PacienteOncologico("Juan Pérez", 65, "Cáncer de pulmón", "Quimioterapia", "Reservado")
    paciente.save_data()
    print(Fore.YELLOW + paciente.descripcion() + Style.RESET_ALL)
    print(separador)

    gato = Gato("Whiskers", 1, "Persa", "Blanco", 4)
    gato.save_data()
    print(Fore.YELLOW + gato.maullar() + Style.RESET_ALL)


main()
