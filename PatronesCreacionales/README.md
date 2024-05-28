# Los Patrones de Diseño
<img src="https://refactoring.guru/images/patterns/content/index/full/patterns-01.png?id=e9cf5363691b460aa690c2716ce35557">

## ¿Qué es un patrón de diseño?
Los patrones de diseño son soluciones comunes a problemas recurrentes en el diseño de software. Funcionan como planos que se pueden adaptar para resolver problemas específicos en tu código.

## Características principales:
- **Concepto general:** No se trata de fragmentos de código específicos que puedas copiar y pegar. En cambio, son ideas que guían la solución de problemas de diseño.

- **Personalización:** Debes adaptar el patrón a las necesidades y contextos particulares de tu programa.

- **Diferencia con algoritmos:** Un algoritmo es una serie de pasos claros para resolver un problema, similar a una receta de cocina. Un patrón de diseño es más como un plano arquitectónico, que da una visión general de cómo resolver un problema, pero no dicta los pasos exactos.

### Estructura de un patrón de diseño:
- **Propósito:** Breve explicación del problema y la solución.

- **Motivación:** Detalle del problema y cómo el patrón lo resuelve.

- **Estructura de clases:** Diagrama que muestra las partes del patrón y sus relaciones.

- **Ejemplo de código:** Código en un lenguaje de programación popular que ilustra el uso del patrón.



<hr>

Existen distintas categorías de patrones de diseño:

# Patrones Creacionales.
Es un patrón que se enfoca en cómo crear objetos de manera flexible y eficiente. Estos patrones proporcionan soluciones a problemas comunes relacionados con la creación de objetos, como la necesidad de instanciar un objeto en un momento específico o la necesidad de crear objetos de diferentes tipos según ciertas condiciones. Los patrones creacionales ayudan a mantener un código limpio, modular y fácil de mantener al separar la creación de objetos de su uso.

## FACTORY METHOD

El Factory Method es un tipo de patrón creacional, y es una manera organizada de crear objetos en programación. En lugar de que el código tenga que saber exactamente qué tipo de objeto necesita crear, usamos una "fábrica" (un método especial) para hacer ese trabajo por nosotros. Esto hace que el código sea más flexible, pues puedes cambiar fácilmente qué tipo de objeto se crea sin cambiar mucho código, fácil de mantener y ordenado, porque el código que crea objetos está separado del resto del programa.

El esquema sería el siguiente:
<img src="https://refactoring.guru/images/patterns/diagrams/factory-method/structure.png">

Y el ejemplo que yo he creado con la temática de criaturas mitológicas es:

<img src"https://github.com/YoooKai/ETS/blob/main/PatronesCreacionales/diagrama.png">
