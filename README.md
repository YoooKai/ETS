# TAREAS DE MARKDOWN

## Índice

- [Tarea 0. Tema libre: ](https://github.com/YoooKai/Markdown/tree/main/Creando%20markdown%20tema%20libre)
- [Tarea 1. Etapas de Desarrollo Software: ](https://github.com/YoooKai/Markdown/tree/main/Tarea1)


# Ciclos de Vida Software

<img src="https://inlogiq.com/wp-content/uploads/2021/11/CICLOS-DE-VIDA-DEL-SOFTWARE-Espana.png" height="300px">

La industria del desarrollo de software incluye diferentes procesos (por ejemplo, análisis, implementación, mantenimiento) y servicios (capacitación, documentación); teniendo esto como base, se le llama ciclo de vida del software al proceso de diseñar, desarrollar e implementar una aplicación (programa, sistema, software). Este ciclo deberá producir software fiable y de alta calidad que cumpla y exceda las expectativas del cliente, alcanzando los objetivos por el cual fue creado y al costo que dé inicio fue estimado. En pocas palabras, el ciclo de vida del software es una secuencia de etapas estructuradas bien definidas para desarrollar un producto de software deseado. 

## Modelo de Desarrollo Software

<img src="https://ungoti.com/es/wp-content/uploads/sites/3/Ideas-inspira.png" height="300px">

Le llamamos modelos de desarrollo de software a los diversos procesos o metodologías que se seleccionan para desarrollar un proyecto en función de sus objetivos. Existen muchos modelos, y estos mismos especifican las distintas etapas del proceso y el orden en que se llevan a cabo. 

## Modelo en cascada

<img src="http://2.bp.blogspot.com/-RFihJHEdYP0/UCBGaPGfOXI/AAAAAAAAACU/irakx2f89pU/s1600/Cascada.jpg" height="300px">

En Ingeniería de software el desarrollo en cascada, es denominado así por la posición de las fases
en el desarrollo de esta, que parecen caer en cascada “por gravedad” hacia las siguientes fases. Es el
enfoque metodológico que ordena rigurosamente las etapas del proceso para el desarrollo de
software, de tal forma que el inicio de cada etapa debe esperar a la finalización de la etapa anterior.
Al final de cada etapa, el modelo está diseñado para llevar a cabo una revisión final, que se encarga de
determinar si el proyecto está listo para avanzar a la siguiente fase. Este modelo fue el primero en
originarse y es la base de todos los demás modelos de ciclo de vida.
Este modelo comenzó a diseñarse en 1966 y se terminó alrededor de 1970. El principal problema
de esta aproximación es el que no podemos esperar que las especificaciones iníciales sean correctas y
completas y que el usuario puede cambiar de opinión sobre una u otra característica.
Además los resultados no se pueden ver hasta muy avanzado el proyecto por lo que cualquier
cambio debido a un error puede suponer un gran retraso además de un alto coste de desarrollo.
Como es evidente esto es solo un modelo teórico, si el usuario cambia de opinión en algún aspecto
tendremos que volver hacia atrás en el ciclo de vida.

## Modelos Evolutivos

<img src="https://images.slideplayer.es/12/3751089/slides/slide_5.jpg" height="300px">

En este modelo los requerimientos del usuario pueden cambiar en cualquier momento.

La práctica nos demuestra que obtener todos los requerimientos al comienzo del proyecto es muy difícil; no solo por la dificultad de el usuario transmitir su idea, sino porque  los requerimientos evolucionan durante el desarrollo y de esta manera, surgen nuevos requerimientos a cumplir. 

El sistema es entonces desarrollado, los usuarios lo usan, y proveen retroalimentación a los desarrolladores. Basada en esta retroalimentación, la especificación de requerimientos es actualizada, y una segunda versión del producto es desarrollada y desplegada. El proceso se repite indefinidamente.

- Plazos apretados
- Se comprende bien el conjunto de requerimientos o
el producto básico
- Los detalles del producto o extensiones del sistema
aún están por definirse.

el modelo de desarrollo evolutivo (algunas veces denominado como prototipado evolutivo) construye una serie de grandes versiones sucesivas de un producto. Sin embargo, mientras que la aproximación incremental presupone que el conjunto completo de requerimientos es conocido al comenzar, el modelo evolutivo asume que los requerimientos no son completamente conocidos al inicio del proyecto.

En el modelo evolutivo, los requerimientos son cuidadosamente examinados, y sólo esos que son bien comprendidos son seleccionados para el primer incremento. Los desarrolladores construyen una implementación parcial del sistema que recibe sólo estos requerimientos.

El sistema es entonces desarrollado, los usuarios lo usan, y proveen retroalimentación a los desarrolladores. Basada en esta retroalimentación, la especificación de requerimientos es actualizada, y una segunda versión del producto es desarrollada y desplegada. El proceso se repite indefinidamente.

Note que el desarrollo evolutivo es 100% compatible con el modelo cascada. El desarrollo evolutivo no demanda una forma específica de observar el desarrollo de algún incremento. Así, el modelo cascada puede ser usado para administrar cada esfuerzo de desarrollo. Obviamente, el desarrollo incremental y evolutivo puede ser combinado también.

Todo lo que uno tiene que hacer es construir un subconjunto de requerimientos conocidos (incremental), y comprender al principio que muchos nuevos requerimientos es probable que aparezcan cuando el sistema sea desplegado o desarrollado.

El desarrollo de software en forma evolutiva requiere un especial cuidado en la manipulación de documentos, programas, datos de test, etc. desarrollados para distintas versiones del software. Cada paso debe ser registrado, la documentación debe ser recuperada con facilidad, los cambios deben ser efectuados de una manera controlada. 

### Modelo Interactivo Incremental

<img src="https://1.bp.blogspot.com/_Z20u51kajjo/TK-WfOL4lYI/AAAAAAAAABM/bVE3xA-T1GU/w1200-h630-p-k-no-nu/000.jpg" height="300px">

n un desarrollo iterativo e incremental el proyecto se planifica en diversos bloques temporales (en el caso de Scrum de un mes natural o hasta de dos semanas, si así se necesita) llamados iteraciones.

Las iteraciones se pueden entender como miniproyectos: en todas las iteraciones se repite un proceso de trabajo similar (de ahí el nombre “iterativo”) para proporcionar un resultado completo sobre producto final, de manera que el cliente pueda obtener los beneficios del proyecto de forma incremental. Para ello, cada requisito se debe completar en una única iteración: el equipo debe realizar todas las tareas necesarias para completarlo (incluuyendo pruebas y documentación) y que esté preparado para ser entregado al cliente con el mínimo esfuerzo necesario. De esta manera no se deja para el final del proyecto ninguna actividad arriesgada relacionada con la entrega de requisitos.

En cada iteración el equipo evoluciona el producto (hace una entrega incremental) a partir de los resultados completados en las iteraciones anteriores, añadiendo nuevos objetivos/requisitos o mejorando los que ya fueron completados. Un aspecto fundamental para guiar el desarrollo iterativo e incremental es la priorización de los objetivos/requisitos en función del valor que aportan al cliente.

Beneficios

    Se puede gestionar las expectativas del cliente (requisitos desarrollados, velocidad de desarrollo, calidad) de manera regular, puede tomar decisiones en cada iteración. Esto es especialmente interesante cuando:
        El cliente no sabe exactamente qué es lo que necesita, lo va sabiendo conforme va viendo cuales son los resultados del proyecto.
        El cliente necesita hacer cambios a corto plazo (nuevos requisitos o a cambios en los ya realizados) por:
            Cambios en las condiciones del mercado (por un cambio de necesidades, por un nuevo producto que ha lanzado la competencia, urgencias).
            La reacción y aceptación del mercado respecto al uso de los primeros resultados del proyecto.
            Cualquier cambio en el entorno (recursos, etc.), que pueda incluso finalizar el proyecto manteniendo como mínimo los resultados alcanzados hasta ese momento.
        El equipo necesita saber si lo que ha entendido es lo que el cliente espera.
    El cliente puede comenzar el proyecto con requisitos de alto nivel, quizás no del todo completos, de manera que se vayan refinando en sucesivas iteraciones. Sólo es necesario conocer con más detalle los requisitos de las primeras iteraciones, los que más valor aportan. No es necesario realizar una recolección completa y detallada de todos los requisitos antes de empezar el desarrollo del proyecto.

    El cliente puede obtener resultados importantes y usables ya desde las primeras iteraciones.
    Se puede gestionar de manera natural los cambios que van apareciendo durante el proyecto. La finalización de cada iteración es el lugar natural donde el cliente puede proporcionar su feedback tras examinar el resultado obtenido (ver control empírico y demostración). Con esta información ya es posible planificar los cambios necesarios para alinearse con las expectativas del cliente desde las primeras iteraciones, de manera que al finalizar el proyecto el cliente obtenga los objetivos esperados.
    El cliente como máximo puede perder los recursos dedicados a una iteración, no los de todo el proyecto.
    La finalización de cada iteración es el lugar natural donde el equipo puede decidir cómo mejorar su proceso de trabajo, en función de la experiencia obtenida. Con esta información ya es posible planificar los cambios necesarios para aumentar la productividad y calidad desde las primeras iteraciones. Ver Retrospectiva.
    Permite conocer el progreso real del proyecto desde las primeras iteraciones y extrapolar si su finalización es viable en la fecha prevista. El cliente puede decidir repriorizar los requisitos del proyecto, añadir nuevos equipos, cancelarlo, etc.
    Permite mitigar desde el inicio los riesgos del proyecto. Desde la primera iteración el equipo tiene que gestionar los problemas que pueden aparecer en una entrega del proyecto. Al hacer patentes estos  riesgos, es posible iniciar su mitigación de manera anticipada.
    Permite gestionar la complejidad del proyecto.
        En una iteración sólo se trabaja en los requisitos que aportan más valor en ese momento.
        Se puede dividir la complejidad para que cada parte sea resuelta en diferentes iteraciones.

    Dado que cada iteración debe dar como resultado requisitos terminados, se minimiza el número de errores que se producen en el desarrollo y se aumentar la calidad.

 
Restricciones

    La disponibilidad del cliente debe ser alta durante todo el proyecto dado que participa de manera continua:
        El inicio de una iteración, el cliente ha de detallar (o haber detallado previamente) los requisitos que se van a desarrollar. 
        En la finalización de cada iteración, el cliente ha de revisar los requisitos desarrollados.
    La relación con el cliente ha de estar basada en los principios de colaboración y ganar/ganar más que tratarse de una relación contractual en la cual cada parte únicamente defiende su beneficio a corto plazo.
    Cada iteración debe dar como resultado requisitos terminados, de manera que el resultado sea realmente útil para el cliente y no deje tareas pendientes para futuras iteraciones o para la finalización del proyecto.
    Cada iteración ha de aportar un valor al cliente, entregar unos resultados cerrados que sean susceptibles de ser utilizados por él.
    Es necesario disponer de técnicas y herramientas que permitan hacer cambios fácilmente en el producto, de manera que pueda crecer en cada iteración de manera incremental sin hacer un gran esfuerzo adicional, manteniendo su complejidad minimizada y su calidad.

 
Recomendaciones

    Utilizar iteraciones cortas de 2 a 4 semanas incrementa la productividad del proyecto, dado que el equipo trabaja de forma más eficiente cuando tiene objetivos a corto plazo. Asímismo, con iteraciones cortas la precisión de las estimaciones aumenta. El tamaño depende de:
        Los condicionantes del proyecto.
        La necesidad de tener feedback más o menos rápido.
        Que no se degrade la relación trabajo útil / gestión operativa (por ejemplo reuniones, actividades necesarias que no producen valor directo, etc.).
    Utilizar iteraciones regulares, de manera que todas sean un timebox de la misma duración.
        El equipo aprende a calcular la velocidad de desarrollo, la cantidad de trabajo que puede hacer en una iteración (sin tener que hacer extrapolaciones si las iteraciones no fuesen regulares).
        El cliente puede proyectar cuantas iteraciones se necesitan para tener cada entrega, en función de la velocidad de desarrollo del equipo (el trabajo que pudo completar en iteraciones anteriores del mismo tamaño), y tomar decisiones al respecto.
        Permite gestionar y sincronizar de manera sencilla las necesidades del proyecto con respecto a las de otros proyectos (integración con el trabajo realizado por otros equipos, compartición de personas que son difíciles de asignar a un único equipo).
        Las iteraciones coincidiendo con meses naturales permiten sincronizar el trabajo del equipo con el de otros departamentos y con el resto de la organización (por ejemplo, la organización puede tener medidas de resultados y objetivos a nivel trimestral o cuatrimestral).


### Modelo en Espiral

<img src="https://www2.deloitte.com/content/dam/html/es/common-img/img-desarrollo-espiral.png" height="300px">

Para resolver los anteriores problemas, en 1984 Boehm presenta el ciclo de vida en espiral, en el que cada una de las fases del cascada termina con una evaluación de riesgos y un prototipo.

Los prototipos permiten a los usuarios determinar si el proyecto continua, debe volver a fases anteriores, o debe terminar. Sin embargo, las fases son todavía lineales, los requisitos se realizan en la fase de requisitos, el diseño en la fase de diseño, y así sucesivamente.

El modelo espiral de los procesos software es un modelo del ciclo de meta-vida. En este modelo, el esfuerzo de desarrollo es iterativo. Tan pronto como uno completa un esfuerzo de desarrollo, otro comienza. Además, en cada desarrollo ejecutado, puedes seguir estos cuatros pasos:

Determinar qué quieres lograr.

Determinar las rutas alternativas que puedes tomar para lograr estas metas. Por cada una, analizar los riesgos y resultados finales, y seleccionar la mejor.

Seguir la alternativa seleccionada en el paso 2.

Establecer qué tienes terminado.

 

La dimensión radial en la figura refleja costos acumulativos incurridos en el proyecto.

Observemos un escenario particular. Digamos que en este proyecto, nosotros viajaremos a resolver un conjunto particular de problemas del cliente. Durante el primer viaje alrededor de la espiral, analizamos la situación y determinamos que los mayores riesgos son la interfaz del usuario. Después de un cuidadoso análisis de las formas alternativas de direccionar esto (por ejemplo, construir un sistema y esperar lo mejor, escribir una especificación de requerimientos y esperar que el cliente lo entienda, y construir un prototipo), determinamos que el mejor curso de acción es construir un prototipo.

Lo realizamos. Luego proveemos el prototipo al cliente quien nos provee con retroalimentación útil. Ahora, comenzamos el segundo viaje alrededor de la espiral. Este tiempo decidimos que el mayor riesgo es ese miedo a que muchos nuevos requerimientos comiencen a aparecer sólo después de que el sistema sea desplegado. Analicemos las rutas alternativas, y decidimos que la mejor aproximación es construir un incremento del sistema que satisfaga sólo los requerimientos mejor entendidos. Hagámoslo ya. Después del despliegue, el cliente nos provee de retroalimentación que dirá si estamos correctos con esos requerimientos, pero 50 nuevos requerimientos ahora se originarán en las cabezas de los clientes. Y el tercer viaje alrededor de la espiral comienza.

El modelo espiral captura algunos principios básicos:

    Decidir qué problema se quiere resolver antes de viajar a resolverlo.

    Examinar tus múltiples alternativas de acción y elegir una de las más convenientes.

    Evaluar qué tienes hecho y qué tienes que haber aprendido después de hacer algo.

    No ser tan ingenuo para pensar que el sistema que estás construyendo será "EL" sistema que el cliente necesita, y

    Conocer (comprender) los niveles de riesgo, que tendrás que tolerar. 

El modelo espiral no es una alternativa del modelo cascada, ellos son completamente compatible. 

### Modelos Ágiles

<img src="https://cdnb.ganttpro.com/uploads/2021/11/que-es-metodologia-agil.png" height="300px">

Desarrollo de software ágil o Agile

por

    Kate Brush, TechTarget
    Valerie Silverthorne, TechTarget

El Desarrollo de Software Ágil —también conocido simplemente como Agile— es un tipo de metodología de desarrollo que anticipa la necesidad de flexibilidad y aplica un nivel de pragmatismo a la entrega del producto terminado. El desarrollo de software ágil requiere un cambio cultural en muchas empresas porque se centra en la entrega limpia de piezas individuales o partes del software y no en la aplicación completa.

Los beneficios de Agile incluyen su capacidad para ayudar a los equipos en un panorama en evolución mientras se mantiene un enfoque en la entrega eficiente de valor comercial. La cultura colaborativa facilitada por Agile también mejora la eficiencia en toda la organización a medida que los equipos trabajan juntos y comprenden sus roles específicos en el proceso. Por último, las empresas que utilizan el desarrollo de software ágil pueden estar seguras de que están lanzando un producto de alta calidad, ya que las pruebas se realizan durante todo el desarrollo, lo que brinda la oportunidad de realizar cambios según sea necesario y alertar a los equipos sobre cualquier problema potencial.

Agile ha reemplazado a la cascada como la metodología de desarrollo de elección en la mayoría de las empresas, pero corre el riesgo de ser eclipsada o consumida por la creciente popularidad de DevOps.
Los cuatro valores de Agile

En 2001, 17 profesionales del desarrollo de software se reunieron para discutir conceptos en torno a la idea del desarrollo de software ligero y terminaron creando el Manifiesto Ágil. El Manifiesto describe los cuatro valores centrales de Agile, y aunque ha habido un debate sobre si el Manifiesto ha sobrevivido a su utilidad, continúa en el núcleo del movimiento Agile.

Los cuatro valores fundamentales descritos en el Manifiesto Ágil son:

Las interacciones individuales son más importantes que los procesos y las herramientas. Las personas impulsan el proceso de desarrollo y responden a las necesidades comerciales. Son la parte más importante del desarrollo y deben valorarse por encima de los procesos y herramientas. Si los procesos o las herramientas impulsan el desarrollo, será menos probable que el equipo responda y se adapte al cambio y, por lo tanto, será menos probable que satisfaga las necesidades del cliente.

Enfoque en el software de trabajo en lugar de una documentación completa. Antes de Agile, se dedicaba una gran cantidad de tiempo a documentar el producto durante todo el desarrollo para su entrega. La lista de requisitos documentados era extensa y causaría grandes retrasos en el proceso de desarrollo. Si bien Agile no elimina el uso de documentación, la simplifica de manera que proporciona al desarrollador solo la información necesaria para realizar el trabajo —como las historias de usuario. El Manifiesto Ágil sigue valorando el proceso de documentación, pero le da más valor al software que funciona.

Colaboración en lugar de negociaciones contractuales. Agile se enfoca en la colaboración entre el cliente y el gerente del proyecto, en lugar de negociaciones entre los dos, para resolver los detalles de la entrega. Colaborar con el cliente significa que se incluye a lo largo de todo el proceso de desarrollo, no solo al principio y al final, lo que facilita a los equipos la satisfacción de las necesidades de sus clientes. Por ejemplo, en el desarrollo de software ágil, el cliente puede ser incluido en diferentes intervalos para demostraciones del producto. Sin embargo, el cliente también podría estar presente e interactuando con los equipos a diario, asistiendo a todas las reuniones y asegurándose de que el producto satisfaga sus deseos.

Enfoque en responder al cambio. El desarrollo de software tradicional se utilizaba para evitar cambios porque se consideraba un gasto no deseado. Agile elimina esta idea. Las breves iteraciones en el ciclo Agile permiten realizar cambios fácilmente, lo que ayuda al equipo a modificar el proceso para que se adapte mejor a sus necesidades y no al revés. En general, el desarrollo de software ágil cree que el cambio es siempre una forma de mejorar el proyecto y proporcionar valor adicional.
Los 12 principios de Agile

El Manifiesto Ágil también describió 12 principios básicos para el proceso de desarrollo. Ellos son:

    Satisfaga a los clientes mediante la entrega temprana y continua de un trabajo valioso.
    Divida el trabajo grande en tareas más pequeñas que se puedan completar rápidamente.
    Reconozca que el mejor trabajo surge de equipos autoorganizados.
    Brinde a las personas motivadas el entorno y el apoyo que necesitan, y confíe en ellos para hacer el trabajo.
    Cree procesos que promuevan esfuerzos sustentables.
    Mantenga un ritmo constante para completar el trabajo.
    Dé la bienvenida a los requisitos cambiantes, incluso al final de un proyecto.
    Reúna al equipo del proyecto y a los propietarios de negocios a diario durante todo el proyecto.
    Haga que el equipo reflexione a intervalos regulares sobre cómo ser más efectivo, luego sintonice y ajuste el comportamiento en consecuencia.
    Mida el progreso por la cantidad de trabajo completado.
    Busque continuamente la excelencia.
    Aproveche el cambio para obtener una ventaja competitiva.

El ciclo de Desarrollo de Software Ágil

El ciclo de desarrollo de software ágil se puede dividir en seis pasos: concepto, inicio, iteración/construcción, lanzamiento, producción y retiro.

El primer paso, el concepto, implica la identificación de oportunidades comerciales en cada proyecto potencial, así como una estimación del tiempo y el trabajo que se requerirá para completar el proyecto. Esta información se puede utilizar para priorizar proyectos y discernir cuáles vale la pena seguir en función de la viabilidad técnica y económica.

Durante el segundo paso, el inicio, se identifican los miembros del equipo, se establece la financiación y se discuten los requisitos iniciales con el cliente. También se debe crear una línea de tiempo que describa las diversas responsabilidades de los equipos y defina claramente cuándo se espera que se complete el trabajo para cada sprint. Un sprint es un período de tiempo establecido durante el cual se debe completar un trabajo específico y prepararlo para su revisión.

Una visualización del ciclo de Desarrollo de Software Ágil

El tercer paso, iteración/construcción, es cuando los equipos comienzan a crear software de trabajo basado en los requisitos y la retroalimentación continua. El ciclo de Desarrollo de Software Ágil se basa en iteraciones —o ciclos de desarrollo únicos— que se basan entre sí y conducen al siguiente paso del proceso de desarrollo general hasta que se completa el proyecto. Cada iteración suele durar entre dos y cuatro semanas, con una fecha de finalización establecida. El objetivo es tener un producto funcional para lanzar al final de cada iteración.

Se producen múltiples iteraciones a lo largo del ciclo de desarrollo y cada una posee su propio flujo de trabajo. Un flujo de iteración típico consta de:

    definir requisitos basados ​​en la acumulación de productos, la acumulación de sprints y los comentarios de los clientes y las partes interesadas;
    desarrollar software basado en los requisitos establecidos;
    realización de pruebas de garantía de calidad, formación y documentación internas y externas;
    entregar e integrar el producto de trabajo en la producción; y
    recopilar comentarios de los clientes y las partes interesadas sobre la iteración con el fin de definir nuevos requisitos para el próximo sprint.

El cuarto paso, la liberación, implica la prueba de garantía de calidad final, la resolución de cualquier defecto restante, la finalización del sistema y la documentación del usuario y, al final, la liberación de la iteración final a producción.

Después del lanzamiento, el quinto paso, la producción, se centra en el soporte continuo necesario para mantener el software. Los equipos de desarrollo deben mantener el software funcionando sin problemas y al mismo tiempo enseñar a los usuarios exactamente cómo usarlo. La fase de producción continúa hasta que finaliza el soporte o se planea retirar el producto.

El paso final, la jubilación, incorpora todas las actividades de fin de ciclo, como notificar a los clientes y la migración final. La versión del sistema debe retirarse de producción. Esto generalmente se hace cuando un sistema necesita ser reemplazado por una nueva versión o si el sistema se vuelve obsoleto, innecesario o comienza a ir en contra del modelo comercial.

A lo largo del ciclo Agile, se pueden agregar diferentes características a la cartera de pedidos del producto, pero todo el proceso debe consistir en repetir cada paso una y otra vez hasta que se satisfagan todos los elementos de la cartera de pedidos. Esto hace que el ciclo Agile sea más un bucle que un proceso lineal. En cualquier momento, una empresa puede tener varios proyectos que ocurren simultáneamente con iteraciones que se registran en diferentes líneas de productos y una variedad de clientes internos y externos que brindan diferentes necesidades comerciales.
Tipos de metodologías Ágiles

El objetivo de cada metodología Ágil es adoptar y adaptarse al cambio mientras entrega software funcional de la manera más eficiente posible. Sin embargo, cada método varía en la forma en que define los pasos del desarrollo de software. Los métodos ágiles más utilizados incluyen:

    Scrum
    Desarrollo de software esbelto
    Programación extrema
    Crystal
    Kanban
    Método de desarrollo de sistemas dinámicos
    Desarrollo impulsado por funciones

Scrum es un marco Ágil liviano que los gerentes de proyectos pueden usar para controlar todo tipo de proyectos iterativos e incrementales. En Scrum, el propietario del producto crea una cartera de productos que les permite trabajar con su equipo para identificar y priorizar la funcionalidad del sistema. La cartera de productos es una lista de todo lo que se necesita lograr para ofrecer un sistema de software que funcione correctamente —esto incluye correcciones de errores, características y requisitos no funcionales. Una vez que se define la cartera de productos, no se puede agregar ninguna funcionalidad adicional excepto por el equipo correspondiente.

Una vez que el equipo y el propietario del producto han establecido las prioridades, los equipos multifuncionales intervienen y acuerdan entregar incrementos funcionales de software durante cada sprint, a menudo dentro de los 30 días. Después de cada sprint, la cartera de productos se reevalúa, analiza y prioriza para seleccionar un nuevo conjunto de funciones entregables para el próximo sprint. Scrum ha ganado popularidad a lo largo de los años porque es simple, ha demostrado ser productivo y puede incorporar las diversas prácticas generales promovidas por los otros métodos Ágiles.

El desarrollo de software esbelto es otro método iterativo que se centra en el uso de un mapeo de flujo de valor efectivo para garantizar que el equipo brinde valor al cliente. Es flexible y cambiante; no tiene pautas o reglas rígidas. El método Lean utiliza los siguientes principios primarios:

    Incremento del aprendizaje
    Paso de poder al equipo
    Fomento de la integridad
    Eliminación de desechos
    Entendimiento el todo
    Toma de decisiones lo más tarde posible
    Entrega del producto lo más rápido posible

El método Lean se basa en una retroalimentación rápida y confiable entre los clientes y los programadores para proporcionar flujos de trabajo de desarrollo rápidos y eficientes. Para lograr esto, proporciona a los individuos y equipos pequeños autoridad para tomar decisiones en lugar de depender de un flujo de control jerárquico. Para eliminar el desperdicio, el método Lean pide a los usuarios que solo seleccionen características verdaderamente valiosas para su sistema, prioricen estas características elegidas y luego las entreguen en lotes pequeños. El desarrollo de software ajustado también fomenta que las pruebas unitarias automatizadas se escriban simultáneamente con el código y se concentra en garantizar que cada miembro del equipo sea lo más productivo posible.

El método de programación extrema (XP) es un enfoque disciplinado que se centra en la velocidad y la entrega continua. Promueve una mayor participación del cliente, ciclos rápidos de retroalimentación, planificación y pruebas continuas y trabajo en equipo cercano. El software se entrega a intervalos frecuentes — generalmente cada una a tres semanas. El objetivo es mejorar la calidad y la capacidad de respuesta del software ante los requisitos cambiantes de los clientes.

El método XP se basa en los valores de comunicación, retroalimentación, sencillez y valentía. Los clientes trabajan en estrecha colaboración con su equipo de desarrollo para definir y priorizar las historias de usuario solicitadas. Sin embargo, depende del equipo entregar las historias de usuario de mayor prioridad en forma de software funcional que se haya probado en cada iteración. Para maximizar la productividad, el método XP proporciona a los usuarios un marco ligero y de apoyo que los guía y ayuda a garantizar el lanzamiento de software empresarial de alta calidad.

Crystal es la metodología más ligera y adaptable. Se enfoca en las personas y las interacciones que ocurren mientras se trabaja en un proyecto Agile, así como en la importancia comercial y la prioridad del sistema en desarrollo. El método Crystal se basa en la constatación de que cada proyecto posee características únicas que requieren un conjunto de políticas, prácticas y procesos ligeramente adaptados. Como resultado, se compone de una colección de modelos de procesos Ágiles, como Crystal Orange, Crystal Clear y Crystal Yellow. Cada modelo tiene sus propias características únicas que son impulsadas por diferentes factores, incluidas las prioridades del proyecto, el tamaño del equipo y la criticidad del sistema.

Al igual que otras metodologías Ágiles, Crystal enfatiza la entrega frecuente de software de trabajo con alta participación del cliente, adaptabilidad y eliminación de burocracia y distracciones. Sus principios clave incluyen la comunicación, el trabajo en equipo y la sencillez.

Kanban utiliza un método de administración de flujo de trabajo altamente visual que permite a los equipos administrar activamente la creación de productos —enfatizando la entrega continua— sin crear más estrés en el ciclo de vida de desarrollo de software (SDLC). Se ha vuelto popular entre los equipos que también practican el desarrollo de software Lean.

Kanban utiliza tres principios básicos: visualizar el flujo de trabajo; limitar la cantidad de trabajo en curso; y mejorar el flujo de trabajo. Similar al Scrum, el método Kanban está diseñado para ayudar a los equipos a trabajar de manera más eficiente entre sí. Fomenta la colaboración continua e intenta definir el mejor flujo de trabajo posible para promover un entorno con aprendizaje y mejora activos y continuos.

El método de desarrollo de sistemas dinámicos (DSDM) es una respuesta a la necesidad de un marco industrial común para la entrega rápida de software. El DSDM se basa en ocho principios clave; El incumplimiento de cualquiera de los principios presenta un riesgo para la finalización exitosa del proyecto. Los ocho principios son:

    Colaboración
    Tiempo de entrega
    Control demostrado
    Comunicación clara y continua
    Un enfoque constante en las necesidades comerciales
    Desarrollo iterativo
    Creación en incrementos a partir de cimientos firmes
    Negativa a comprometer la calidad

En el DSDM, el retrabajo está integrado en el proceso y todos los cambios deben ser reversibles. Los requisitos del sistema se priorizan utilizando las reglas de MoSCoW, que clasifican la prioridad como:

    M - debe tener
    S - debería tener
    C - podría haberlo tenido, pero no es crítico
    W - no lo tendrá ahora, pero podría tenerlo más tarde

Es importante para el DSDM que no todos los requisitos se consideren críticos. Cada iteración debe incluir elementos menos críticos que se puedan eliminar para que los requisitos de mayor prioridad no se vean afectados.

Por último, el desarrollo basado en características (FDD) combina las mejores prácticas de ingeniería de software —como el desarrollo por característica, propiedad del código y modelado de objetos de dominio— para crear un proceso de iteración corta, cohesionado y basado en modelos. FFD comienza definiendo una forma general del modelo, que a su vez crea una lista de características. Luego, el método procede con iteraciones que duran dos semanas y se centran en la planificación por característica, el diseño por característica y la construcción por característica. Si una función tarda más de dos semanas en construirse, debe dividirse en funciones más pequeñas. La principal ventaja de FDD es que es escalable —incluso para equipos grandes— ya que utiliza el concepto de "diseño suficiente inicialmente" o JEDI.
Ventajas y desventajas de Agile

Mucho se ha comparado a lo largo de los años con enfoques ágiles versus en cascada.

En la era Waterfall del desarrollo de software, los programadores trabajaban solos, con poca o ninguna entrada antes de entregar el software a los probadores y luego a la producción. Los errores, las complicaciones y los cambios de funciones no se manejaron bien o se abordaron tan tarde en el proceso que los proyectos se retrasaron seriamente o incluso se desecharon.

La idea detrás del modelo Agile, en el que todos —incluido el lado empresarial— se mantuvieron involucrados e informados en el proceso de desarrollo, representó un cambio profundo tanto en la cultura de la empresa como en la capacidad de llevar mejor software al mercado más rápidamente.

La colaboración y la comunicación se volvieron tan importantes como la tecnología, y debido a que el Manifiesto Agile está abierto a la interpretación, Agile se ha adaptado y modificado para adaptarse a organizaciones de todos los tamaños y tipos. El cambio cultural ágil también allanó el camino para la última evolución de desarrollo de software, DevOps.

Por otro lado, muchos dirían que la mayor desventaja de Agile es el hecho de que ha sido modificado —algunos dirían diluido— por muchas organizaciones. Este fenómeno está tan extendido que los practicantes de "Agile a mi manera" se conocen como "ScrumButs", como en "Hacemos Scrum en nuestra organización, pero..."

Aunque Agile abre las líneas de comunicación entre los desarrolladores y el lado empresarial, ha sido menos exitoso incorporar las pruebas y las operaciones a esa combinación —una omisión que puede haber ayudado a que la idea de DevOps ganara terreno.

Otra preocupación potencial sobre Agile es su falta de énfasis en la tecnología, lo que puede dificultar la venta del concepto a los altos directivos que no comprenden el papel que juega la cultura en el desarrollo de software. Además, la necesidad de completar sprints a tiempo puede crear un entorno de trabajo estresante para los desarrolladores de software. Pueden verse obligados a trabajar horas extra y quedarse hasta tarde para cumplir con los plazos.


