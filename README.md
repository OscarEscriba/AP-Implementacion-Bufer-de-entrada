# AP-Implementacion-Bufer-de-entrada
## Explicación del codigo...
Este programa es una simulación de un bufer de entrada con un tamaño fijo de 10 caracteres. Para realizarlo utilizamos dos puntos, el de inicio y avance. 
Todo esto con la finalidad de procesar el texto de manera eficiente. La entrada almacena en una lista de caracteres y se recarga en el bufer conforme se procesa
1. Se carga un segmento del texto en un bufer de tamaño fijo, utilizando la función "cargar_buffer".
2. Procesa el contenido del bufer, extrayendo los lexemas. Los cuales consideramos las palabras separadas por espacios o el marcador de fin del archivo.
3. Se recarga el bufer cuando se alcanza su limite hasta procesar toda la entrada

Entonces en resumen podemos decir que el codigo simula un búfer de entrada con un tamaño fijo de 10 caracteres para procesar texto de manera eficiente.
Utiliza dos punteros: inicio, que indica desde dónde se carga el búfer, y avance, que recorre los caracteres dentro del búfer. Se identifican lexemas (palabras separadas por espacios) 
y se imprimen conforme se procesan. Cuando el búfer se llena, se recarga con la siguiente porción del texto hasta alcanzar el final, marcado con "eof".
