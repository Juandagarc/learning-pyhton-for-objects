# Parcial II

**Temas:** Herencia, Modularidad, Encapsulamiento, Polimorfismo, Estructura de Datos.

1. Para este punto usted debe generar un archivo JSON para crear entidades “libros”, para esto deberá realizar las siguientes actividades:
    - Revisar la documentación respecto al tema archivo JSON que se adjuntará en la sección del “parcial II”.
    - Analizar y documentar el archivo llamado “generador”, este algoritmo genera archivos JSON y tiene unos datos que no concuerdan con el contexto de libros, cosa que ustedes deben arreglar.
    - Va a generar un nuevo algoritmo donde ustedes van a adaptar el paradigma orientado a objetos a ese código “generador”, esto quiere decir que, por ejemplo, en vez de dejarlo como funciones deben diseñar métodos y así para cubrir las necesidades del código.
    - Después de adaptar el código deberá realizar métodos para que se puedan realizar las siguientes funcionalidades de agregar libro por consola y lectura de datos, para este punto debe modularizar el código.

2. Desarrolle un sistema para gestionar las reservas de habitaciones en un hotel. El hotel tiene diferentes tipos de habitaciones: Habitación Simple, Habitación Doble y Suite. Todas las habitaciones tienen un número, un precio y un estado (disponible o reservado). Las habitaciones dobles y las suites permiten agregar servicios adicionales, como desayuno o spa.

   **Requerimientos:**
    - Crear una clase base `Habitación` con atributos encapsulados (`numero`, `precio`, `estado`).
    - Crear las clases derivadas `HabitacionSimple`, `HabitacionDoble` y `Suite`, con la posibilidad de agregar servicios adicionales en `HabitacionDoble` y `Suite`.
    - Crear un sistema para reservar habitaciones, donde el número de la habitación sea la clave y el valor sea el objeto `Habitación`.
    - Implementar funciones para mostrar todas las habitaciones disponibles, reservar una habitación y calcular el precio total con servicios incluidos en las habitaciones dobles y suites.

3. Crea un sistema de gestión de pedidos para una tienda en línea. Los productos pueden ser de diferentes tipos (`Electrónico`, `Ropa`, `Alimento`). Cada producto tiene un nombre, precio y cantidad disponible. Los productos electrónicos tienen un período de garantía, la ropa tiene un tamaño y los alimentos tienen una fecha de caducidad. El sistema debe gestionar el stock, permitir realizar pedidos y calcular el total de la compra con un posible descuento si se compra una cierta cantidad de productos.

   **Requerimientos:**
    - Crear una clase base `Producto` con atributos `nombre`, `precio` y `cantidad`.
    - Crear subclases `Electrónico`, `Ropa` y `Alimento`, cada una con su atributo específico.
    - Crear un sistema de gestión de pedidos que permita:
        - Mostrar los productos disponibles.
        - Realizar un pedido, actualizando la cantidad disponible.
        - Calcular el total de la compra, aplicando un descuento si el cliente compra más de 5 unidades de un mismo producto.
        - Guardar los productos en un archivo JSON.
