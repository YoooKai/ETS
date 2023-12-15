# Ciclos de Vida Software

<img src="https://media.licdn.com/dms/image/C5612AQE-Cvyl68PUVw/article-cover_image-shrink_600_2000/0/1586939623971?e=2147483647&v=beta&t=qIjVah6OtLEn6PRoCdY8_RH0xLWXz6mXAETQ7EV_kYA" height="300px">

La esfera del desarrollo de software engloba diversas fases y funciones, tales como análisis, implementación y mantenimiento, así como la provisión de servicios como la formación y documentación.

En términos generales, se conoce como ciclo de vida del software al **proceso que implica concebir, crear e implantar una aplicación, ya sea un programa, sistema o software.**

El propósito fundamental de este ciclo es generar software confiable y de primera calidad, superando las expectativas del cliente y logrando los objetivos establecidos, todo dentro del presupuesto inicialmente estimado. En resumen, el ciclo de vida del software se refiere a una secuencia de etapas claramente definidas que estructuran el desarrollo de un producto de software específico.

## Modelo de Desarrollo Software

<img src="https://ungoti.com/es/wp-content/uploads/sites/3/Ideas-inspira.png" height="300px">

Se hace referencia a modelos de desarrollo de software para describir los diversos procesos o metodologías seleccionadas con el fin de llevar a cabo un proyecto según sus objetivos. Se cuentan con numerosos modelos, los cuales detallan las distintas etapas del proceso y establecen el orden en que deben ejecutarse.

# Modelo en cascada

<img src="https://blog.comparasoftware.com/wp-content/uploads/2021/06/1.jpg" height="300px">

En Ingeniería de Software, el enfoque conocido como desarrollo en cascada recibe su nombre debido a la disposición secuencial de las fases del desarrollo, que aparentan descender en forma de cascada, de manera que cada fase sucede después de la anterior, como si cayera "por gravedad" hacia las siguientes etapas. Esta metodología **establece un orden riguroso para las etapas del proceso de desarrollo de software, donde el inicio de cada fase está condicionado a la conclusión de la fase precedente.**

Al término de cada etapa, este modelo incorpora una revisión final destinada a determinar si el proyecto está preparado para avanzar a la siguiente fase. Fue el primer modelo de ciclo de vida en ser concebido, sirviendo como base para la creación de otros enfoques.

Este modelo fue ideado aproximadamente en 1966 y finalizado alrededor de 1970. Su principal desafío radica en la expectativa de que las especificaciones iniciales sean exactas y completas, y que las preferencias del usuario no cambien durante el proceso. Además, los resultados no son evidentes hasta etapas avanzadas del proyecto, lo que implica que cualquier corrección debido a errores puede ocasionar considerables retrasos y altos costos de desarrollo. Es importante destacar que este modelo es esencialmente teórico, ya que cualquier cambio en las preferencias del usuario podría requerir retroceder en el ciclo de vida del proyecto.

# Modelos Evolutivos

<img src="https://images.slideplayer.es/12/3751089/slides/slide_5.jpg" height="300px">

En este modelo, conocido como desarrollo evolutivo o prototipado evolutivo, se reconoce que los requerimientos del usuario pueden cambiar en cualquier momento. La realidad nos enseña que obtener todos los requerimientos al inicio del proyecto es una tarea difícil, no solo debido a la complejidad de transmitir las ideas del usuario, sino también porque los requerimientos evolucionan durante el desarrollo, dando lugar a la emergencia de nuevos requisitos.

En el desarrollo evolutivo, **se construyen sucesivas versiones amplias de un producto.** A diferencia de la aproximación incremental, que asume que el conjunto completo de requerimientos es conocido al comenzar, el modelo evolutivo parte del supuesto de que los requerimientos no son completamente conocidos al inicio del proyecto.

En este enfoque, los requerimientos se examinan detenidamente, y solo aquellos que se comprenden bien son seleccionados para el primer incremento. Los desarrolladores crean una implementación parcial del sistema que aborda únicamente estos requerimientos. Los usuarios utilizan el sistema, proporcionan retroalimentación a los desarrolladores, y basándose en esta retroalimentación, la especificación de requerimientos se actualiza. Luego, se desarrolla y despliega una segunda versión del producto. Este proceso se repite de manera continua.

Es importante destacar que el desarrollo evolutivo es totalmente compatible con el modelo cascada, ya que no exige una forma específica de observar el desarrollo de un incremento. Por lo tanto, el modelo cascada puede utilizarse para gestionar cada esfuerzo de desarrollo. Además, el desarrollo incremental y evolutivo pueden combinarse, construyendo un subconjunto de requerimientos conocidos de manera incremental, y reconociendo desde el principio que es probable que aparezcan nuevos requerimientos durante el despliegue o desarrollo del sistema.

El desarrollo de software de forma evolutiva requiere especial atención en la manipulación de documentos, programas, datos de prueba, etc., desarrollados para distintas versiones del software. Cada paso debe ser registrado, la documentación debe ser fácilmente recuperable, y los cambios deben realizarse de manera controlada.

## Modelo Interactivo Incremental

<img src="https://1.bp.blogspot.com/_Z20u51kajjo/TK-WfOL4lYI/AAAAAAAAABM/bVE3xA-T1GU/w1200-h630-p-k-no-nu/000.jpg" height="300px">

En un enfoque de desarrollo iterativo e incremental, el proyecto se planifica en bloques temporales llamados iteraciones, que pueden tener una duración de uno a dos meses, o incluso dos semanas en el caso de Scrum. Cada iteración se asemeja a un miniproyecto, ya que implica la repetición de un proceso de trabajo similar. El objetivo es proporcionar resultados completos sobre el producto final de manera incremental, permitiendo al cliente obtener beneficios progresivos del proyecto.

En cada iteración, se completa un conjunto de requisitos, y el equipo realiza todas las tareas necesarias, incluyendo pruebas y documentación, para entregarlos al cliente con el mínimo esfuerzo. Esto garantiza que no se posterguen actividades críticas relacionadas con la entrega de requisitos hasta el final del proyecto.

El equipo evoluciona el producto en cada iteración, construyendo sobre los resultados de las iteraciones anteriores al agregar nuevos objetivos o mejorar los requisitos existentes. La priorización de los objetivos y requisitos se realiza en función del valor que aportan al cliente.

**Beneficios del enfoque iterativo e incremental:**

1. **Gestión de expectativas del cliente:** Permite gestionar regularmente las expectativas del cliente en términos de requisitos desarrollados, velocidad de desarrollo y calidad. Esto es particularmente útil cuando el cliente no tiene una comprensión clara de lo que necesita, y sus requisitos evolucionan durante el desarrollo.

2. **Flexibilidad ante cambios:** Facilita la incorporación de cambios a corto plazo en respuesta a condiciones del mercado, reacciones del usuario o cambios en el entorno. Los clientes pueden ajustar sus requisitos a medida que observan los resultados del proyecto.

3. **Resultados tempranos y usables:** Permite al cliente obtener resultados significativos y utilizables desde las primeras iteraciones del proyecto.

4. **Gestión natural de cambios:** Facilita la gestión de cambios durante el proyecto, ya que la finalización de cada iteración proporciona un lugar natural para que el cliente proporcione retroalimentación y se realicen ajustes.

5. **Mitigación temprana de riesgos:** Permite identificar y abordar los riesgos del proyecto desde el inicio, ya que el equipo gestiona los problemas que pueden surgir en cada entrega.

6. **Gestión de la complejidad:** Permite abordar la complejidad del proyecto al trabajar en requisitos que aportan más valor en cada iteración.

7. **Minimización de errores:** Al exigir requisitos terminados en cada iteración, se minimiza el número de errores que se producen durante el desarrollo, aumentando la calidad del producto.

Restricciones del enfoque iterativo e incremental:

1. **Alta disponibilidad del cliente:** Requiere la participación continua del cliente en el inicio y la finalización de cada iteración para detallar y revisar los requisitos desarrollados.

2. **Relación colaborativa:** Se basa en una relación de colaboración y en principios de ganar/ganar, en lugar de ser una relación contractual centrada en beneficios a corto plazo para cada parte.

3. **Requisitos terminados en cada iteración:** Cada iteración debe resultar en requisitos terminados y entregables, sin dejar tareas pendientes para futuras iteraciones o para la finalización del proyecto.

4. **Aportar valor al cliente en cada iteración:** Cada iteración debe aportar un valor tangible al cliente, entregando resultados cerrados susceptibles de ser utilizados.

5. **Herramientas y técnicas flexibles:** Se necesita disponer de herramientas y técnicas que permitan realizar cambios fácilmente en el producto, facilitando el crecimiento incremental sin un esfuerzo adicional significativo.

## Modelo en Espiral

<img src="https://www2.deloitte.com/content/dam/html/es/common-img/img-desarrollo-espiral.png" height="300px">

En 1984, Barry Boehm propuso el modelo de ciclo de vida en espiral como una respuesta a los problemas inherentes al modelo en cascada. En este enfoque, cada fase del ciclo en cascada concluye con una evaluación de riesgos y la creación de un prototipo.

A diferencia del modelo en cascada, el modelo en espiral permite una iteración más frecuente y evaluaciones continuas de riesgos. Aunque las fases siguen siendo lineales, se incorpora flexibilidad mediante la introducción de prototipos, los cuales permiten a los usuarios determinar si el proyecto debe avanzar, retroceder a fases anteriores o incluso finalizar.

El modelo en espiral representa un ciclo de meta-vida, donde el esfuerzo de desarrollo es iterativo. Cada desarrollo sigue cuatro pasos:

1. Determinar qué se quiere lograr.
2. Identificar las rutas alternativas para alcanzar esas metas. Para cada alternativa, analizar riesgos y resultados finales, y seleccionar la mejor.
3. Seguir la alternativa seleccionada.
4. Evaluar y determinar qué se ha logrado.
5. La dimensión radial en la figura del modelo refleja los costos acumulativos en el proyecto.

El modelo en espiral se ilustra con un escenario específico: en el primer viaje alrededor de la espiral, se identifica la interfaz de usuario como el mayor riesgo, y se decide construir un prototipo para abordarlo. Luego, en los viajes subsiguientes, se enfrentan a nuevos riesgos y se toman decisiones iterativas basadas en el aprendizaje continuo.

**Principios básicos capturados por el modelo en espiral:**

1. **Definición clara del problema:** Decidir qué problema se quiere resolver antes de abordarlo.

2. **Análisis de alternativas:** Examinar múltiples alternativas de acción y seleccionar la más conveniente.
3. **Evaluación continua:** Evaluar lo que se ha logrado y lo que se ha aprendido después de cada fase de desarrollo.
4. **Flexibilidad ante cambios:** Reconocer que el sistema construido inicialmente puede no ser el definitivo y estar preparado para cambios en los requisitos.
5. **Gestión de riesgos:** Conocer y comprender los niveles de riesgo que se deben tolerar.

Es importante destacar que el modelo en espiral no es una alternativa al modelo en cascada; son completamente compatibles. Ambos modelos pueden coexistir y complementarse en proyectos de desarrollo de software.

## Modelos Ágiles

<img src="https://cdnb.ganttpro.com/uploads/2021/11/que-es-metodologia-agil.png" height="300px">

El Desarrollo de Software Ágil, también conocido como Agile, es una metodología que prioriza la flexibilidad y entrega eficiente de partes individuales del software en lugar de la aplicación completa. Requiere un cambio cultural y se centra en la colaboración, entrega de valor y pruebas continuas.

Beneficios de Agile:

- Adaptable a cambios en un entorno en evolución.
- Mejora la eficiencia mediante la colaboración y roles definidos.
- Garantiza productos de alta calidad con pruebas continuas.

Los Cuatro Valores del Manifiesto Ágil:

1. **Individuos e interacciones sobre procesos y herramientas:** La importancia de las personas en el proceso de desarrollo.

2. **Software funcionando sobre documentación extensiva:** Prioridad en el producto funcional en lugar de documentación detallada.

3. **Colaboración con el cliente sobre negociaciones contractuales:** Enfasis en la colaboración para resolver detalles de entrega.

4. **Responder al cambio sobre seguir un plan:** Aceptar y adaptarse a cambios para mejorar el proyecto.

Ciclo de Desarrollo Ágil:

1. **Concepto:** Identificación de oportunidades y estimación de tiempo y trabajo.

2. **Inicio:** Establecimiento de equipo, financiamiento y requisitos iniciales con el cliente.

3. **Iteración/Construcción:** Creación de software basado en requisitos y retroalimentación continua.

4. **Lanzamiento:** Pruebas finales, resolución de defectos y liberación de la iteración final.

5. **Producción:** Soporte continuo y enseñanza a usuarios.

6. **Retiro:** Finalización de todas las actividades del proyecto.

**Ventajas:**

- Mejora en la colaboración y comunicación.
  Entrega rápida de software funcional.
- Adaptabilidad a cambios y mejora continua.

**Desventajas:**

- Modificaciones excesivas y dilución de la metodología.
- Menor énfasis en pruebas y operaciones.
  Posible estrés para cumplir con plazos.

En general, Agile ha transformado la forma en que se desarrolla el software, enfocándose en la flexibilidad, colaboración y entrega continua de valor. Aunque tiene desafíos, sigue siendo una metodología esencial en la industria del desarrollo de software.
