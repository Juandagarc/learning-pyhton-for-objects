import json
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

class Coche:
    def __init__(self, velocidad, cilindrada):
        self.velocidad = velocidad  # Velocidad máxima
        self.cilindrada = cilindrada  # Cilindrada en cm³

    def tiempo_viaje(self, distancia):
        # Calcular el tiempo basado en la velocidad máxima
        return round(distancia / self.velocidad, 2)

    def gasto_mensual(self, consumo_por_km, precio_litro):
        litros_mensuales = 1000 * consumo_por_km
        costo_mensual = litros_mensuales * precio_litro
        return round(costo_mensual, 2)


class Vehiculo(Coche):
    def __init__(self, tipo, marca, modelo, anio, tipo_llanta, tipo_combustible, color, ruedas, velocidad, cilindrada):
        super().__init__(velocidad, cilindrada)
        self.tipo = tipo  # Puede ser 'Coche', 'Moto', 'Camion'
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo_llanta = tipo_llanta
        self.tipo_combustible = tipo_combustible
        self.color = color
        self.ruedas = ruedas

    def duracion_llantas(self):
        if self.tipo_llanta == "MarcaA":
            return 5  # años
        elif self.tipo_llanta == "MarcaB":
            return 3  # años
        elif self.tipo_llanta == "MarcaC":
            return 2  # años
        else:
            return "Desconocida"

    def mostrar_combustible_recomendado(self):
        return f"Combustible recomendado para {self.tipo}: {self.tipo_combustible}"

    def calcular_gasto_mensual(self):
        if self.tipo_combustible == "ACPM":
            consumo_por_km = 0.08
            precio_litro = 9000
        elif self.tipo_combustible == "Extra":
            consumo_por_km = 0.1
            precio_litro = 12000
        elif self.tipo_combustible == "Corriente":
            consumo_por_km = 0.09
            precio_litro = 10000
            if self.tipo == "Moto":
                consumo_por_km = 0.07
        else:
            return "Combustible desconocido"

        return super().gasto_mensual(consumo_por_km, precio_litro)

    def tiempos_viaje(self):
        destinos = ["Bogotá", "Medellín", "Cali", "Cartagena", "Barranquilla"]
        distancias = [320, 213, 207, 1035, 970]

        tiempos = []
        for i in range(len(destinos)):
            tiempo = super().tiempo_viaje(distancias[i])
            tiempos.append((destinos[i], tiempo))

        return tiempos


def guardar_vehiculos(vehiculos, archivo="vehiculos.json"):
    with open(archivo, "w") as file:
        json.dump([vehiculo.__dict__ for vehiculo in vehiculos], file, indent=4)


def cargar_vehiculos(archivo="vehiculos.json"):
    try:
        with open(archivo, "r") as file:
            contenido = file.read()
            if not contenido.strip():  # Verificar si el archivo está vacío
                print(Fore.YELLOW + "El archivo de vehículos está vacío.")
                return []
            vehiculos = json.loads(contenido)
            return [Vehiculo(**vehiculo) for vehiculo in vehiculos]
    except FileNotFoundError:
        print(Fore.RED + "No se encontró el archivo de vehículos.")
        return []
    except json.JSONDecodeError:
        print(Fore.RED + "El archivo de vehículos no contiene datos válidos.")
        return []


def mostrar_menu():
    print(Fore.BLUE + "\n--- MENÚ ---")
    print("1. Añadir un nuevo vehículo")
    print("2. Mostrar duración de las llantas")
    print("3. Mostrar combustible recomendado")
    print("4. Mostrar tiempo de viaje a destinos")
    print("5. Mostrar gasto mensual en combustible")
    print("6. Guardar vehículos en archivo")
    print("7. Salir")


def agregar_vehiculo(vehiculos):
    tipo = input("Tipo de vehículo (1.Coche/2.Moto/3.Camion): ")
    if tipo == '1':
        tipo = "Coche"
    elif tipo == '2':
        tipo = "Moto"
    elif tipo == '3':
        tipo = "Camion"
    marca = input("Marca del vehículo(1.Chevrolet/2.Renault/3.Mazda): ")
    if marca == '1':
        marca = "Chevrolet"
    elif marca == '2':
        marca = "Renault"
    elif marca == '3':
        marca = "Mazda"
    modelo = input("Modelo del vehículo: ")
    anio = int(input("Año del vehículo: "))
    tipo_llanta = input("Tipo de llanta (1.MarcaA/2.MarcaB/3.MarcaC): ")
    if tipo_llanta == '1':
        tipo_llanta = "MarcaA"
    elif tipo_llanta == '2':
        tipo_llanta = "MarcaB"
    elif tipo_llanta == '3':
        tipo_llanta = "MarcaC"
    tipo_combustible = input("Tipo de combustible (1ACPM/2.Extra/3.Corriente): ")
    if tipo_combustible == '1':
        tipo_combustible = "ACPM"
    elif tipo_combustible == '2':
        tipo_combustible = "Extra"
    elif tipo_combustible == '3':
        tipo_combustible = "Corriente"
    color = input("Color del vehículo: ")
    if tipo == "Coche":
        ruedas = 4
    elif tipo == "Moto":
        ruedas = 2
    elif tipo == "Camion":
        ruedas = 6
    velocidad_maxima = int(input("Velocidad máxima del vehículo (km/h): "))
    cilindrada = int(input("Cilindrada del vehículo (cm³): "))

    nuevo_vehiculo = Vehiculo(tipo, marca, modelo, anio, tipo_llanta, tipo_combustible, color, ruedas, velocidad_maxima, cilindrada)
    vehiculos.append(nuevo_vehiculo)
    print(Fore.GREEN + "Vehículo añadido exitosamente.")


def main():
    vehiculos = cargar_vehiculos()

    while True:
        mostrar_menu()
        opcion = input(Fore.GREEN + "\nElige una opción: ")

        if opcion == '1':
            agregar_vehiculo(vehiculos)

        elif opcion == '2':
            for vehiculo in vehiculos:
                print(Fore.CYAN + f"{vehiculo.tipo} {vehiculo.marca} {vehiculo.modelo}: "
                                  f"{vehiculo.duracion_llantas()} años de duración de llantas")

        elif opcion == '3':
            for vehiculo in vehiculos:
                print(Fore.YELLOW + vehiculo.mostrar_combustible_recomendado())

        elif opcion == '4':
            for vehiculo in vehiculos:
                print(Fore.CYAN + f"Tiempos de viaje para {vehiculo.tipo} {vehiculo.marca} {vehiculo.modelo}:")
                tiempos = vehiculo.tiempos_viaje()
                for destino, tiempo in tiempos:  # Ahora es una lista de tuplas
                    print(f"  - A {destino}: {tiempo} horas")
        elif opcion == '5':
                for vehiculo in vehiculos:
                    print(Fore.MAGENTA + f"{vehiculo.tipo} {vehiculo.marca} {vehiculo.modelo}: "
                                         f"Gasto mensual en combustible: {vehiculo.calcular_gasto_mensual()} COP")

        elif opcion == '6':
            guardar_vehiculos(vehiculos)
            print(Fore.GREEN + "Vehículos guardados exitosamente.")

        elif opcion == '7':
            print(Fore.BLUE + "Saliendo del programa...")
            break

        else:
            print(Fore.RED + "Opción no válida. Intenta de nuevo.")


main()
