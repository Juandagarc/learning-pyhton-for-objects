# Taller 4

## Tema: Herencia simple

### Instrucciones

1. Realice un programa en el que podamos observar los atributos de las clases inspiradas en el siguiente gráfico. Se debe implementar herencia simple y se deben guardar la información de cada vehículo en uno o varios archivos para poder listarlos cuando se necesiten. El programa también debe contar con los siguientes métodos:

   **Métodos Vehículo:**
   - **a.** Debe mostrar información dependiendo del vehículo (camión, moto, automóvil) de cuántos años aproximadamente le pueden durar las llantas. Esto también está sujeto a tres tipos de marcas.
   - **b.** Tipo de combustible que se recomienda usar para el vehículo que se elija (ACPM, Extra, Corriente).

   **Métodos Coche:**
   - **a.** Mostrar cuánto tiempo se tomaría cada vehículo en llegar desde Pereira a diferentes lugares en Colombia (mínimo 5 lugares).
   - **b.** Mostrar cuánto gastaría al mes en combustible cada automóvil, suponiendo que cada uno hace viajes de 1000 km mensuales. Ustedes pueden consultar precios actuales para parametrizar el combustible.
  
     <img width="163" alt="image" src="https://github.com/user-attachments/assets/2a3b4b34-390c-4107-8c61-c98142387f18">

2. **Diagrama a utilizar:**

   Implemente:
   
   <img width="358" alt="image" src="https://github.com/user-attachments/assets/ac38b157-afb1-4203-89b1-2472140ec24d">


   - Cree al menos un objeto de cada subclase y añádalos a una lista llamada `vehículos`.
   - Realice una función llamada `catalogar()` que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.
   - Modifique la función `catalogar()` para que reciba un argumento optativo `ruedas`, haciendo que muestre únicamente los que su número de ruedas concuerden con el valor del argumento. También debe mostrar un mensaje: 
     > "Se han encontrado {} vehículos con {} ruedas:"

     Únicamente si se envía el argumento `ruedas`. Pruébela con valores 0, 2 y 4 ruedas.
