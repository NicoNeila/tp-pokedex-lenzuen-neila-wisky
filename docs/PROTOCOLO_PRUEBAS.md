# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y elegir la opción 1 (Listar catálogo) | dataset de la cátedra | lista de 9 Pokémon (ids 1 a 9), sin traceback | no corrido |  |
| P02 | E1 | Opción 5 e ingresar un ítem inexistente | entrada = `-1` | mensaje "No existe ese Pokémon." y el menú vuelve a mostrarse | no corrido | Se prueba en la opción 5 porque "Ver detalle" (opción 2) todavía es pendiente |
| P03 | E2 | Opción 5 sobre una forma final (sube 2 escalones hasta la base) | entrada = `6` (Charizard) | `Charmander → Charmeleon → Charizard` | no corrido | Es el ejemplo de la traza del informe |
| P04 | E2 | Opción 5 sobre una forma final (caso base de `cadena_desde`: no tiene evolución siguiente) | entrada = `9` (Blastoise) | `Squirtle → Wartortle → Blastoise` | no corrido | Blastoise tiene `evolucion: None`, así que `cadena_desde` entra directo al caso base |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar texto (`.txt`), salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
| P16 | E2 | Opción 5 sobre una forma intermedia (sube 1 escalón, después baja) | entrada = `5` (Charmeleon) | `Charmander → Charmeleon → Charizard` | no corrido | Verifica que incluya al anterior y al siguiente |
| P17 | E2 | Opción 5 sobre el primero de una línea evolutiva (no tiene anterior) | entrada = `7` (Squirtle) | `Squirtle → Wartortle → Blastoise` | no corrido | `buscar_base` entra directo a su caso base porque nadie evoluciona en 7 |
| P18 | E2 | Opción 5 con un id fuera del catálogo | entrada = `99` | mensaje "No existe ese Pokémon.", sin traceback, el menú sigue | no corrido |  |
| P19 | E2 | Opción 5 con texto que no es un Pokémon ni un número | entrada = `abc` | mensaje "No existe ese Pokémon.", sin traceback, el menú sigue | no corrido | Variante: dejar la entrada vacía (solo Enter) |
