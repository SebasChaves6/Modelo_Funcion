| Estudiante | Carné |
|-------------|-------------------|
| Jordan Sánchez Tencio | C4J811 |
|   |    |


Tarea Programada 1 – Primera Etapa
- 1. Modelo Función

El modelo función consiste en representar un arreglo donde a cada llave se le va asignando un valor. Funciona como si fuera un diccionario, pero hecho desde cero usando estructuras de datos.

Las características que tiene son:

Cada llave es única.
A cada llave le corresponde un valor.
Dos llaves distintas pueden tener el mismo valor.
Las llaves son strings alfanuméricos.
Los valores son strings de longitud fija (20 caracteres, letras minúsculas).

Las operaciones implementadas fueron:

Asignar (Assign): inserta una nueva relación o actualiza una existente.
Eliminar (Elimine): elimina una llave.
Buscar (Lookup): retorna el valor asociado a una llave.
Llaves (Keys): devuelve todas las llaves.
Imprimir (Imprime): muestra las relaciones.
Limpiar (Clear): vacía la estructura.
Done: libera memoria (equivalente a limpiar en Python).
- 2. Lista Ordenada (Estructura Genérica)

La lista ordenada es una estructura en la cual los elementos se mantienen en orden según la llave.

Esto permite:

Búsquedas más rápidas que una lista desordenada (se puede cortar antes).
Mantener siempre los datos organizados.

Pero:

Insertar puede ser costoso porque hay que encontrar la posición correcta.
En algunos casos hay que mover elementos o recorrer toda la lista.
- 3. Lista Ordenada por Arreglos

En esta implementación se usaron dos listas:

una para llaves
otra para valores

Las posiciones corresponden entre sí.

Funcionamiento:
Al insertar, se busca la posición donde debe ir la llave para mantener el orden.
Si la llave ya existe, se actualiza el valor.
Si no existe, se inserta en la posición correcta.
Ventajas:
Acceso directo por índice.
Implementación sencilla.
Desventajas:
Insertar o eliminar puede ser costoso (hay que mover elementos).
No es eficiente para listas muy grandes.
- 4. Lista Ordenada por Punteros

Se implementó usando una lista enlazada.

Cada nodo contiene:

llave
valor
referencia al siguiente nodo
Funcionamiento:
Se recorre la lista hasta encontrar la posición correcta.
Se inserta el nodo manteniendo el orden.
Para eliminar, se ajustan los enlaces.
Ventajas:
No hay que mover elementos como en arreglos.
Inserciones más eficientes en comparación con arreglos.
Desventajas:
Acceso más lento (hay que recorrer la lista).
Mayor uso de memoria por referencias.
- 5. Tabla Hash (Abierta)

La tabla hash se implementó usando encadenamiento, es decir:

La tabla es una lista.
Cada posición contiene otra lista.
Si dos llaves generan el mismo índice, se almacenan en la misma cubeta.
Función Hash

Se utilizó una función basada en el valor ASCII de los caracteres:

h = h * 31 + ord(c)

Luego se aplica módulo:

indice = h % capacidad
¿Por qué funciona?
Convierte strings en números.
Distribuye las llaves en diferentes posiciones.
Reduce colisiones en la mayoría de los casos.

Esta forma de calcular el hash es bastante común porque permite que pequeñas diferencias en las llaves generen resultados distintos.

- 6. Manejo de Colisiones

Se utilizó el método de encadenamiento:

Si dos llaves caen en la misma posición:
se agregan a la misma lista.
Luego se busca dentro de esa lista.

Esto evita sobrescribir datos y permite almacenar múltiples elementos en una misma posición.

- 7. Evaluación de la Función Hash

Se probó la función hash con varias llaves y se observó que:

Las llaves se distribuyen en diferentes posiciones.
No todas caen en el mismo índice.
Existen colisiones, pero no en exceso.

Esto indica que la función tiene una distribución aceptable para el tamaño de la tabla utilizada.

- 8. Descripción de la redistribución (rehashing)

Cuando una tabla hash comienza a llenarse demasiado, es común aplicar un proceso llamado redistribución o rehashing. Consiste en crear una nueva tabla con mayor tamaño y volver a insertar todos los elementos usando la función hash.

La idea es reducir la cantidad de colisiones, ya que al aumentar el tamaño de la tabla, los elementos se pueden distribuir mejor.

Este proceso tiene un costo alto, ya que es necesario recorrer todos los elementos y recalcular su posición. En términos de complejidad, es un proceso de orden O(n).


- 9. Observaciones
La lista ordenada mantiene el orden, pero puede ser lenta al insertar.
La lista por punteros evita mover elementos, pero es más lenta en acceso.
La tabla hash es más rápida para búsquedas en promedio, pero no mantiene orden.
Cada estructura tiene ventajas dependiendo del tamaño de los datos.
-  10. Conclusión

Se logró implementar el modelo función utilizando diferentes estructuras de datos.

Se comprobó que:

No existe una estructura “mejor” en todos los casos.
La eficiencia depende del tipo de operación y del tamaño de los datos.
La tabla hash es más eficiente en búsquedas, mientras que las listas ordenadas permiten mantener los datos organizados.
