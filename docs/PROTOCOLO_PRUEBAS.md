# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y elegir la opción 1 (Listar catálogo) | dataset de la cátedra | lista de 14 Pokémon y "Total: 14 Pokemon", sin traceback | pasa | Expectativa corregida en E4: decía 9 Pokémon, pero el catálogo tiene 14 |
| P02 | E1 | Opción 5 e ingresar un ítem inexistente | entrada = `-1` | mensaje "No existe ese Pokémon." y el menú vuelve a mostrarse | pasa | Se prueba en la opción 5 porque "Ver detalle" (opción 2) era pendiente hasta E3 |
| P03 | E2 | Opción 5 sobre una forma final (sube 2 escalones hasta la base) | entrada = `6` (Charizard) | `Charmander → Charmeleon → Charizard` | pasa | Es el ejemplo de la traza del informe |
| P04 | E2 | Opción 5 sobre una forma final (caso base de `cadena_desde`: no tiene evolución siguiente) | entrada = `9` (Blastoise) | `Squirtle → Wartortle → Blastoise` | pasa | Blastoise tiene `evolucion: None`, así que `cadena_desde` entra directo al caso base |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | pasa |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | pasa |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | pasa |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | pasa |  |
| P09 | E4 | Opción 3 → 1 (lineal) con un nombre que existe | `Gardevoir` | lo encuentra y muestra sus datos | pasa |  |
| P10 | E4 | Opción 3 → 1 (lineal) con un nombre que no existe | `Missingno` | "No se encontró…", sin traceback, el menú sigue | pasa |  |
| P11 | E4 | Recién arrancado (no ordenado por nombre): opción 3 → 2 (binaria) | `Obstagoon`, después `Bulbasaur` | avisa que reordena por nombre y lo encuentra; no da un falso "no encontrado" | pasa | La segunda búsqueda ya no avisa porque el catálogo quedó ordenado |
| P12 | E4 | Opción 4: por nombre (selección), después por tipo (inserción), después por número (selección) | catálogo completo | el orden cambia cada vez | pasa | Ordenado por tipo, cada grupo queda en orden alfabético: inserción es estable |
| P13 | E5 | Opción 10 → 1 (alta); salir con 0; volver a iniciar y listar (opción 1) | id `900`, nombre `Articunox`, tipo `Hielo`/`Volador`, sin evolución | Articunox aparece después del reinicio y el total pasa a 15 | pasa | Los cambios del CLI se guardan en `data/catalogo.txt`. Después de la prueba se dio de baja (P20) para dejar el catálogo con 14 |
| P14 | E5 | Opción 9 → 3 (guardar BIN); opción 9 → 5 (actualizar posición); opción 9 → 4 (cargar BIN) y listar | posición `0`; nombre `Prueba`; tipos sin cambiar | Al cargar BIN, el registro 0 muestra `Prueba`; los otros 13 no cambian | pasa | El archivo mide 9 + 14 × 52 = 737 bytes. Solo cambian los bytes del nombre del registro 0: se escribe con `seek(9 + 0 × 52)` sin reescribir el archivo |
| P15 | E5 | Opción 9 → 4 (cargar BIN) con archivos dañados; iniciar el programa con un `catalogo.txt` dañado | BIN de 3 bytes, BIN con magia `XXXX`, BIN truncado; TXT con encabezado incorrecto o una fila con campos de menos | BIN: informa el error (`ArchivoInvalidoError`) y el menú sigue. TXT al iniciar: informa el error y el programa termina sin traceback | pasa | Expectativa corregida: con el TXT dañado al iniciar no hay catálogo para mostrar, así que el programa avisa y cierra. No se suben los archivos de prueba |
| P16 | E2 | Opción 5 sobre una forma intermedia (sube 1 escalón, después baja) | entrada = `5` (Charmeleon) | `Charmander → Charmeleon → Charizard` | pasa | Verifica que incluya al anterior y al siguiente |
| P17 | E2 | Opción 5 sobre el primero de una línea evolutiva (no tiene anterior) | entrada = `7` (Squirtle) | `Squirtle → Wartortle → Blastoise` | pasa | `buscar_base` entra directo a su caso base porque nadie evoluciona en 7 |
| P18 | E2 | Opción 5 con un id fuera del catálogo | entrada = `99` | mensaje "No existe ese Pokémon.", sin traceback, el menú sigue | pasa |  |
| P19 | E2 | Opción 5 con texto que no es un Pokémon ni un número | entrada = `abc` | mensaje "Tenes que ingresar un numero entero.", sin traceback, el menú sigue | pasa | Expectativa corregida en E4: la opción 5 pide un id y valida que sea un número |
| P20 | E5 | Opción 10 → 3 (modificar), reiniciar; después opción 10 → 2 (baja), reiniciar | id `900` (creado en P13): nombre `ArtiNuevo`; después baja del 900 | Tras reiniciar se ve `ArtiNuevo`; tras la baja el 900 no aparece, el total vuelve a 14 y ningún Pokémon queda evolucionando a un id que no existe | pasa | La baja deja en vacío la evolución de quien apuntaba al Pokémon eliminado |
