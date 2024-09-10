# Conceptos basicos de programación orientada a objetos(POO)

## a. Clase
Una clase es una plantilla o un modelo que define las propiedades (atributos) y los comportamientos (métodos) que pueden tener los objetos. Es la base de la programación orientada a objetos y representa la estructura de un objeto.

**Ejemplo:**
```python
class Perro:
    especie = "Canino"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

## b. Objeto
Un objeto es una instancia de una clase. Representa una entidad concreta que tiene un estado (definido por sus atributos) y un comportamiento (definido por sus métodos). Cada objeto es único, aunque pertenezca a la misma clase.

**Ejemplo:**
```python
mi_perro = Perro("Firulais", 5)
```

## c. Self
`self` es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables que pertenecen a la misma. Es un primer parámetro obligatorio de cualquier método de instancia en Python.

**Ejemplo:**
```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Aquí self se refiere a la instancia actual
        self.edad = edad
    def ladrar(self):
        return f"{self.nombre} está ladrando"
```

## d. Constructor
Un constructor es un método especial que se llama automáticamente cuando se crea un nuevo objeto de una clase. Su propósito es inicializar los atributos del objeto. En Python, se define con el método `__init__`.

**Ejemplo:**
```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

## e. Programación Orientada a Objetos (POO)
La Programación Orientada a Objetos es un paradigma de programación basado en el concepto de "objetos", que pueden contener datos y código: datos en forma de campos (atributos) y código en forma de procedimientos (métodos). La POO facilita la reutilización de código y mejora la modularidad y la mantenibilidad de las aplicaciones.

**Ejemplo:**
```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        return f"El {self.marca} {self.modelo} está arrancando"
```

## f. Método
Un método es una función definida dentro de una clase que describe los comportamientos de los objetos creados a partir de la clase. Los métodos pueden operar sobre los atributos de los objetos y realizar acciones específicas.

**Ejemplo:**
```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        return f"Hola, soy {self.nombre}!"
```

## g. Instancia
Una instancia es un objeto concreto creado a partir de una clase específica. Cada instancia tiene su propio estado único, definido por los atributos y métodos de la clase.

**Ejemplo:**
```python
perro1 = Perro("Max")
perro2 = Perro("Luna")
```