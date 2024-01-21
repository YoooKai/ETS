# Aplicación de transporte -  Especificación de Casos de Uso

Desarrollo de un diagrama de casos de uso para un sistema de biblioteca. Los actores pueden ser "Usuario" y "Bibliotecario". Algunos casos de uso podrían ser "Prestar Libro", "Devolver Libro", "Buscar Libro", etc.

<img src="">

## ACTORES

| Actor | Usuario |
|---|---|
| Descripción | Usuarios que utilizan el sistema de biblioteca para buscar, prestar y devolver libros. |
| Características | Tienen la capacidad para buscar libros según distintos parámetros como autor, de realizar préstamos y devoluciones. |
| Relaciones | Interactúan con el caso de uso "Buscar Libro", "Prestar Libro", "Devolver Libro" con el bibliotecario cada vez que realizan un préstamo. |
| Referencias | Buscar Libro, Prestar Libro, Devolver Libro |
| Notas | Los usuarios pueden tener distintos niveles de acceso basados en su tipo.|
| Autor | Kai Rodríguez García |
| Fecha | 20/01/2024 |


| Actor | Bibliotecario |
|---|---|
| Descripción | Individuo encargado de la gestión y administración del sistema bibliotecario. |
| Características | Habilidad para gestionar el inventario de libros. Capacidad para registrar nuevos libros en el sistema. Responsable de supervisar préstamos y devoluciones. Acceso a informes y estadísticas sobre el uso de la biblioteca. |
| Relaciones | Interactúa con el caso de uso "Actualizar Catálogo", "Prestar Libro", y "Devolver libro" pues tiene relación con el usuario al realizar préstamos. |
| Referencias | Gestionar Inventario, Registrar Libro, Gestionar Préstamos, Prestar libro, Actualizar catálogo |
| Notas | Puede acceder a los datos relacionados con la actividad de la biblioteca. |
| Autor | Kai Rodríguez García |
| Fecha | 20/01/2024 |


## Casos de Uso

|  Caso de Uso                |      Prestar Libro          |
|------------------|-----------------------------------|
| **Fuentes**      | Sistema de préstamos                           |
| **Actores**      | Bibliotecario, Usuario             |
| **Descripción**  | El bibliotecario presta un libro al usuario, registrando la transacción. |
| **Flujo básico** | Usuario solicita préstamo. El bibliotecario confirma solicitud, verificando y registrando del préstamo. También realiza acciones como renovar, extender o cancelar préstamos.  |
| **Pre-condiciones** | Disponibilidad del libro. |
| **Post-condiciones** | Libro registrado como prestado y asociado al usuario. |
| **Requerimientos** | Acceso al sistema de préstamos y el libro. |
| **Notas**        | El sistema guarda el préstamo realizado. |


|  Caso de Uso               |   Devolver Libro       |
|------------------|-----------------------------------|
| **Fuentes**      | Sistema de la Biblioteca           |
| **Actores**      | Bibliotecario, Usuario             |
| **Descripción**  | El bibliotecario recibe la devolución de un libro, actualizando su estado. |
| **Flujo básico** |Inicio de sesión del bibliotecario. Usuario entrega el libro. Verificación y actualización del estado del libro. Registro de la devolución en el sistema. |
| **Pre-condiciones** | Sesión iniciada por el bibliotecario, usuario solicitó devolución, usuario debe tener le libro |
| **Post-condiciones** | Libro disponible para préstamo. |
| **Requerimientos** | El libro que debe ser devuelto. |
| **Notas**        | El sistema calcula y registra multas por devolución tardía. |


| Caso de Uso            |        Buscar Libro       |
|------------------|-----------------------------------|
| **Fuentes**      | Inventario de Biblioteca                 |
| **Actores**      | Usuario                           |
| **Descripción**  | El usuario busca un libro en el catálogo de la biblioteca. |
| **Flujo básico** | Especificación de términos de búsqueda (autor, título). El usuario ve los resultados de búsqueda, si está disponible o no. |
| **Pre-condiciones** | Información del libro a buscar |
| **Post-condiciones** | Presentación de libros coincidentes con la búsqueda. |
| **Requerimientos** | Acceso a la función de búsqueda. |
| **Notas**        | El sistema permite búsquedas avanzadas por varios criterios. |

|  Caso de Uso    |    Actualizar catálogo  |
|------------------|-----------------------------------|
| **Fuentes**      | Sistema de la Biblioteca    |
| **Actores**      | Bibliotecario                      |
| **Descripción**  | El bibliotecario administra y actualizar el catálogo de libros disponibles|
| **Flujo básico** | Bibliotecario agrega nuevos libros, actualiza detalles o elimina registros según sea necesario, añadiendo o modificando la base de datos del catálogo. |
| **Pre-condiciones** | Información sobre los datos de libros disponibles. |
| **Post-condiciones** | El catálogo se actualiza tras las modificaciones realizadas. |
| **Requerimientos** | Acceso a la base de datos del sistema de biblioteca |
| **Notas**        | Acción escencial para el correcto funcionamiento las acciones de búsqueda de libros y préstamos |
