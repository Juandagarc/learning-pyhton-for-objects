import json


# Clase principal 1: Persona
class Persona:
    def __init__(self, nombre, id_personal, edad, email, telefono):
        self.nombre = nombre
        self.id_personal = id_personal
        self.edad = edad
        self.email = email
        self.telefono = telefono


# Clase principal 2: InstrumentoMusical
class InstrumentoMusical:
    def __init__(self, tipo_instrumento, afinacion, material, marca_instrumento):
        self.tipo_instrumento = tipo_instrumento
        self.afinacion = afinacion
        self.material = material
        self.marca_instrumento = marca_instrumento

    def afinar(self):
        print(f"{self.tipo_instrumento} está siendo afinado.")


# Clase principal 3: Piano
class Piano:
    def __init__(self, marca, modelo, año_fabricacion, precio, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.precio = precio
        self.tipo = tipo


# Subclase 1: Cliente (Hereda de Persona y puede tocar el piano como InstrumentoMusical)
class Cliente(Persona, InstrumentoMusical):
    def __init__(self, nombre, id_personal, edad, email, telefono, tipo_cliente, tipo_instrumento, afinacion, material, marca_instrumento):
        Persona.__init__(self, nombre, id_personal, edad, email, telefono)
        InstrumentoMusical.__init__(self, tipo_instrumento, afinacion, material, marca_instrumento)
        self.tipo_cliente = tipo_cliente
        self.pianos_comprados = []

    def comprar_piano(self, piano):
        self.pianos_comprados.append(piano)
        print(f"{self.nombre} ha comprado un {piano.marca} {piano.modelo}.")

    def tocar_piano(self):
        print(f"{self.nombre} está tocando el {self.tipo_instrumento} de {self.marca_instrumento}.")


# Subclase 2: Empleado (Hereda de Persona y también toca instrumentos)
class Empleado(Persona, InstrumentoMusical):
    def __init__(self, nombre, id_personal, edad, email, telefono, salario, puesto, tipo_instrumento, afinacion, material, marca_instrumento):
        Persona.__init__(self, nombre, id_personal, edad, email, telefono)
        InstrumentoMusical.__init__(self, tipo_instrumento, afinacion, material, marca_instrumento)
        self.salario = salario
        self.puesto = puesto

    def calcular_salario_anual(self):
        return self.salario * 12

    def tocar_instrumento(self):
        print(f"{self.nombre}, que es {self.puesto}, está tocando el {self.tipo_instrumento}.")


# Subclase 3: PianoDeCola (Hereda de Piano)
class PianoDeCola(Piano):
    def __init__(self, marca, modelo, año_fabricacion, precio, longitud):
        super().__init__(marca, modelo, año_fabricacion, precio, "De Cola")
        self.longitud = longitud


# Subclase 4: PianoVertical (Hereda de Piano)
class PianoVertical(Piano):
    def __init__(self, marca, modelo, año_fabricacion, precio, altura):
        super().__init__(marca, modelo, año_fabricacion, precio, "Vertical")
        self.altura = altura


# Subclase 5: Proveedor (Hereda de Persona y también puede tocar instrumentos)
class Proveedor(Persona, InstrumentoMusical):
    def __init__(self, nombre, id_personal, edad, email, telefono, empresa, tipo_instrumento, afinacion, material, marca_instrumento):
        Persona.__init__(self, nombre, id_personal, edad, email, telefono)
        InstrumentoMusical.__init__(self, tipo_instrumento, afinacion, material, marca_instrumento)
        self.empresa = empresa

    def surtir_pianos(self, lista_pianos, piano):
        lista_pianos.append(piano)
        print(f"{self.nombre} ha surtido un {piano.marca} {piano.modelo} a la tienda.")

    def tocar_instrumento(self):
        print(f"{self.nombre}, proveedor de {self.empresa}, está tocando su {self.tipo_instrumento}.")


def guardar_en_json(lista_objetos, nombre_archivo="tienda_pianos.json"):
    with open(nombre_archivo, 'w') as archivo:
        json.dump([obj.__dict__ for obj in lista_objetos], archivo, indent=4, default=str)
    print(f"Información guardada en {nombre_archivo}")


if __name__ == "__main__":
    cliente1 = Cliente("Laura Torres", "C001", 30, "laura@correo.com", "123456789", "Regular", "Piano", "440Hz", "Madera", "Yamaha")
    empleado1 = Empleado("Juan Gómez", "E001", 28, "juan@correo.com", "987654321", 1500, "Vendedor", "Guitarra", "Standard", "Madera", "Gibson")
    proveedor1 = Proveedor("Carlos Ruiz", "P001", 45, "carlos@correo.com", "123987654", "Pianos S.A.", "Flauta", "Do", "Metal", "Yamaha")

    piano1 = PianoDeCola("Yamaha", "C7", 2022, 15000, 2.27)
    piano2 = PianoVertical("Kawai", "K300", 2021, 7000, 1.22)

    lista_pianos = []
    lista_personas = [cliente1, empleado1, proveedor1]

    proveedor1.surtir_pianos(lista_pianos, piano1)
    cliente1.comprar_piano(piano1)

    print(f"Salario anual de {empleado1.nombre}: {empleado1.calcular_salario_anual()}")

    cliente1.tocar_piano()
    empleado1.tocar_instrumento()
    proveedor1.tocar_instrumento()

    guardar_en_json(lista_personas + lista_pianos)
