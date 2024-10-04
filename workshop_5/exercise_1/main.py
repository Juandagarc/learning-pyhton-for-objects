import json
from datetime import datetime


class ProfesorAyudante:
    def __init__(self, nombre, id_personal, fecha_ingreso, edad, email, telefono, horas_trabajadas=None,
                 tipo_profesor=None, salario_hora=None, carrera=None, nivel=None, promedio=None):
        self.nombre = nombre
        self.id_personal = id_personal
        self.fecha_ingreso = fecha_ingreso
        self.edad = edad
        self.email = email
        self.telefono = telefono
        self.horas_trabajadas = horas_trabajadas
        self.tipo_profesor = tipo_profesor
        self.salario_hora = salario_hora
        self.carrera = carrera
        self.nivel = nivel
        self.promedio = promedio

    def calcular_sueldo(self):
        if self.horas_trabajadas and self.salario_hora:
            return self.horas_trabajadas * self.salario_hora
        return 0

    def calcular_antiguedad(self):
        fecha_actual = datetime.now()
        antiguedad = fecha_actual.year - self.fecha_ingreso.year
        return antiguedad

    def asignar_materias(self):
        if self.tipo_profesor == "titular":
            materias = ["Matemáticas Avanzadas", "Física Cuántica", "Algoritmos Complejos"]
        elif self.tipo_profesor == "adjunto":
            materias = ["Matemáticas Básicas", "Física General", "Programación"]
        else:
            materias = ["Introducción a la Física", "Álgebra Lineal", "Lógica"]
        return materias


class Profesor(ProfesorAyudante):
    def __init__(self, nombre, id_personal, fecha_ingreso, edad, email, telefono, horas_trabajadas, tipo_profesor,
                 salario_hora):
        super().__init__(nombre, id_personal, fecha_ingreso, edad, email, telefono, horas_trabajadas, tipo_profesor,
                         salario_hora)


class Alumno(ProfesorAyudante):
    def __init__(self, nombre, id_personal, fecha_ingreso, edad, email, telefono, carrera, nivel, promedio):
        super().__init__(nombre, id_personal, fecha_ingreso, edad, email, telefono, None, None, None, carrera, nivel,
                         promedio)


class PersonalUniversitario(Profesor, Alumno):
    def __init__(self, nombre, id_personal, fecha_ingreso, edad, email, telefono, horas_trabajadas, tipo_profesor,
                 salario_hora, carrera, nivel, promedio):
        Profesor.__init__(self, nombre, id_personal, fecha_ingreso, edad, email, telefono, horas_trabajadas,
                          tipo_profesor, salario_hora)
        Alumno.__init__(self, nombre, id_personal, fecha_ingreso, edad, email, telefono, carrera, nivel, promedio)


def guardar_en_json(lista_personal, nombre_archivo="personal_universitario.json"):
    with open(nombre_archivo, 'w') as archivo:
        json.dump([p.__dict__ for p in lista_personal], archivo, indent=4, default=str)
    print(f"Información guardada en {nombre_archivo}")


if __name__ == "__main__":
    profesor_ayudante = ProfesorAyudante("Luis Méndez", "PA001", datetime(2020, 1, 10), 23, "luis@universidad.com",
                                         "333444555", 80, "auxiliar", 20, "Matemáticas", 2, 4.5)

    profesor1 = Profesor("Dr. Juan Pérez", "P001", datetime(2005, 3, 14), 45, "juan@universidad.com", "123456789", 160,
                         "titular", 50)

    alumno1 = Alumno("Carlos Gómez", "A001", datetime(2021, 9, 1), 20, "carlos@universidad.com", "111222333",
                     "Ingeniería de Sistemas", 3, 4.2)

    personal1 = PersonalUniversitario("Ana López", "PU001", datetime(2015, 5, 10), 40, "ana@universidad.com",
                                      "444555666", 120, "adjunto", 40, "Ingeniería Electrónica", 5, 4.8)

    print(f"Sueldo mensual de {profesor_ayudante.nombre}: {profesor_ayudante.calcular_sueldo()}")
    print(f"Sueldo mensual de {profesor1.nombre}: {profesor1.calcular_sueldo()}")

    print(f"Antigüedad de {alumno1.nombre}: {alumno1.calcular_antiguedad()} años")
    print(f"Antigüedad de {personal1.nombre}: {personal1.calcular_antiguedad()} años")

    print(f"Materias de {profesor_ayudante.nombre}: {profesor_ayudante.asignar_materias()}")
    print(f"Materias de {profesor1.nombre}: {profesor1.asignar_materias()}")

    personal_universitario = [profesor_ayudante, profesor1, alumno1, personal1]
    guardar_en_json(personal_universitario)
