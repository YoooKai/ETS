
<!-- APUNTES
requerimientos

funcionales o no funcionales

funcionales tienen que ver con los datos que se proveen del mismo programa

los no funcionales no son

la fase de diseño es dividir el programa en partes más pequeñas, poniendo nombre a todas las partes

la codificación es elegir el porgrama que vas a utilizar para implementar ese sistema informático para el programa

hay unha fase que es complación, que es compilar o interpretar el programa

pruebas, es la fase que somete al sistema informático a unas pruebas que pueden ser unitarias o de integración

las unitarias es someter a todas las partes pequeñas a unas entradas y ver qué salidas se obtienen, si son esperadas o no

las integrales es tener en cuenta a todo el conjunto

tras la fase de prueba, a dónde se lleva al programa?

a la fase de explotación, en la empresa del cliente

la fase de mantenimiento es la más larga en la empresa, ver si funciona todo y si da problemas

la documentación es una fase que considste en unas erie de guías, que puede ser de usuario

para el cliente o técnicos que van a ponerlo dentro de la empresa

fases de ciclos de vida-->

# Etapas de Desarrollo Software

El desarrollo de software es un proceso complejo que implica la creación de programas informáticos destinados a resolver problemas específicos o satisfacer necesidades particulares. Para garantizar la eficiencia, calidad y éxito de un proyecto, este proceso se organiza en distintas etapas que constituyen el ciclo de vida del desarrollo de software.

<img src="https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Screenshots_2019/wasserfallmodell-ES-1.jpg" height="300">

## ANÁLISIS DE UN REQUESITOS

Un requisito es una declaración que describe una característica, función o restricción que debe cumplir un sistema o software. Estos requisitos pueden ser de dos tipos: funcionales, que describen lo que el sistema debe hacer (por ejemplo, registrar un usuario), y no funcionales, que describen cómo el sistema debe ser (por ejemplo, ser seguro o rápido).

<img src="https://donhk.dev/wp-content/uploads/2021/03/functional-requirements-vs-non-functional-requirements.jpg" height="250px">

<br>

<br>

| Requisitos Funcionales | Requisitos No Funcionales |
|---|---|
|Describen qué hace el sistema. | Describen cómo debe ser el sistema. |
| Detallan las funcionalidades específicas que el sistema debe proporcionar. | Se centran en la calidad, el rendimiento, la seguridad y las características del sistema. |
| Orientados a lo que el sistema debe lograr en términos de comportamiento y resultados. | Orientados a cómo el sistema debe cumplir con los requisitos de calidad, rendimiento y experiencia. |
| Medidos por su capacidad para cumplir con escenarios y casos de uso específicos. | Medidos por atributos como velocidad, seguridad, usabilidad, disponibilidad, entre otros. |
| Directamente afectan la interacción del usuario con el sistema. | Indirectamente afectan la experiencia del usuario y la calidad del sistema. |
| Se traducen en funcionalidades específicas del sistema. | Se traducen en criterios de rendimiento, seguridad, usabilidad, entre otros. |
| Se traducen en funcionalidades específicas del sistema. | Se centran en la calidad, el rendimiento, la seguridad y las características del sistema. |



## DISEÑO

<img src="https://streambe.com/wp-content/uploads/2022/09/diseno-we-grafico-scaled.jpg" height="250px">

Esta es la segunda etapa del ciclo de vida del desarrollo de software, que implica el desarrollo de la arquitectura, los prototipos y el diseño de la experiencia del usuario. He aquí un rápido resumen de lo que implica esta etapa:

- **Arquitectura de software:** Se refiere al proceso de establecer una cadena ordenada de elementos en un programa de software para el control de calidad, la legibilidad y la accesibilidad. Se puede pensar en la arquitectura del software como el plano del equipo de desarrollO.
- **Prototipo:** El equipo de interfaz de usuario/experiencia de usuario (UI/UX) del software crea una edición prototipo del programa para verificar su aspecto y el flujo de los elementos de diseño del software. Permite al equipo y a las partes interesadas imaginarse el aspecto visual del software.

## CODIFICACIÓN Y COMPILACIÓN

<img src="https://www.solbyte.com/blog/wp-content/uploads/5-etapas-del-proceso-de-desarrollo-de-software.jpg" height="250px">

En esta fase del ciclo de vida de un sistema, se genera el código fuente en el lenguaje de programación escogido. Aquí también puede definirse la parametrización del software.

Para el desarrollo del código se pueden utilizar herramientas denominadas IDE (Integrated Development Environment) o entornos de desarrollo integrado, que sirven para codificar de manera más fácil y práctica.

En esta fase también pueden realizarse pruebas unitarias que definirán la versatilidad del sistema y su capacidad de detección de fallos.

## **PRUEBAS**

La prueba de software es el proceso de evaluar y verificar que un producto o aplicación de software hace lo que se supone que debe hacer. Los beneficios de las pruebas incluyen la prevención de errores, la reducción de los costos de desarrollo y la mejora del rendimiento.

<img src="https://res.cloudinary.com/pym/image/upload/f_auto/v1/articles/2019/testing/tipos-prueba-software.png" height="300px">

- ## Unitarias

<img src="https://autify.com/wp-content/uploads/2022/08/what-is-unit-testing-min.jpg" height="300px">

Las pruebas unitarias consisten en aislar una parte del código y comprobar que funciona a la perfección. Son pequeños tests que validan el comportamiento de un objeto y la lógica.

El unit testing suele realizarse durante la fase de desarrollo de aplicaciones de software o móviles. Normalmente las llevan a cabo los desarrolladores, aunque en la práctica, también pueden realizarlas los responsables de QA.

Hay una especie de mito respecto a las pruebas unitarias. Algunos desarrolladores están convencidos de que son una pérdida de tiempo y las evitan buscando ahorrar tiempo.

Nada más alejado de la realidad.

Con ellas se detectan antes errores que, sin las pruebas unitarias, no se podrían detectar hasta fases más avanzadas como las pruebas de sistema, de integración e incluso en la beta.

Realizar pruebas unitarias con regularidad supone, al final, un ahorro de tiempo y dinero.

- ## De integración

<img src="https://blog.shiftasia.com/content/images/2021/12/Integration-Testing.png" height="300px">

Las pruebas de integración o pruebas integradas se definen como un mecanismo de testeo de software, donde se realiza un análisis de los procesos relacionados con el ensamblaje o unión de los componentes, sus comportamientos con múltiples partes del sistema (ya sea de archivos operativos) o de hardware, entre otras.

De modo que las pruebas de integración están a cargo del examen de las interfaces entre los subsistemas o los grupos de componentes del programa o aplicación que se analiza, lo que contribuye a garantizar su funcionamiento correcto.

## EXPLOTACIÓN

<img src="https://www.turing.com/blog/wp-content/uploads/2022/05/Top-Software-Developer-Skills-to-Learn-This-Year-for-Tech-Jobs-scaled.jpg" height="300px">

La explotación en el contexto del desarrollo de software se refiere a la fase en la que el software es implementado y puesto en funcionamiento para su uso continuo. En esta etapa, el sistema se ejecuta en un entorno operativo real, y los usuarios comienzan a utilizarlo para llevar a cabo las tareas previstas. La explotación implica la gestión y supervisión continua del software para garantizar su correcto funcionamiento, eficiencia y seguridad. También puede incluir la aplicación de actualizaciones y parches para corregir posibles problemas y mejorar el rendimiento.

## MANTENIMIENTO

<img src="https://www.standardfirms.com/wp-content/uploads/2023/04/Hire-Software-Maintenance-Team.png" height="300px">

El mantenimiento de software es la fase dedicada a la gestión y mejora continua del sistema después de su implementación. Se divide comúnmente en cuatro tipos de actividades:

1. **Corrección de Errores (Correctiva):** Se centra en la identificación y solución de errores o defectos que surgen durante la operación del software.

2. **Adaptación (Adaptativa):** Implica realizar modificaciones para que el software se adapte a cambios en el entorno operativo, como actualizaciones de hardware o software de sistema.

3. **Mejora (Perfectiva):** Se enfoca en mejorar el rendimiento, la eficiencia y la funcionalidad del software, incluso cuando no hay problemas evidentes.

4. **Prevención de Problemas (Preventiva):** Consiste en la implementación de medidas para prevenir posibles problemas futuros y mejorar la estabilidad y seguridad del sistema.

El mantenimiento es esencial para asegurar que el software siga siendo efectivo y cumpla con los requisitos cambiantes a lo largo del tiempo.

## Documentación. 
### Tipos de documentos

<img src="https://res.cloudinary.com/dfe4dvbuz/image/upload/f_auto/v1629771591/blog/Who_does_Documentation_belong_to_eh22mi" height="300px">

La documentación en el desarrollo de software comprende la creación y mantenimiento de registros escritos que describen diferentes aspectos del sistema. Estos documentos pueden incluir:

1. **Documentación de Requisitos:** Detalla los requisitos funcionales y no funcionales del sistema.

2. **Documentación de Diseño:** Describe la arquitectura del software, los prototipos y la experiencia del usuario.

3. **Documentación de Código:** Incluye comentarios en el código fuente que explican su funcionamiento y lógica.

4. **Documentación de Pruebas:** Registra los detalles de las pruebas realizadas, incluyendo resultados y casos de prueba.

5. **Manuales de Usuario:** Proporciona información sobre cómo utilizar el software.

6. **Documentación de Mantenimiento:** Registra cambios y actualizaciones realizadas durante la fase de mantenimiento.

La documentación es esencial para facilitar la comprensión, mantenimiento y evolución del software a lo largo del tiempo.

## Video Resumen

En este vídeo de manera concisa y didáctica se explican las distintas etapas del desarrollo software.

[![Etapas del desarrollo Software](https://img.freepik.com/vector-premium/7-etapas-proceso-desarrollo-productos-software-o-sdlc-o-ciclo-vida-desarrollo-software_518018-1686.jpg?w=2000)](https://www.youtube.com/watch?v=bVMQQNjygoA)
