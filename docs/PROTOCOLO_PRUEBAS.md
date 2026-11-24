# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y elegir la opción 1 (Listar catálogo) | dataset de la cátedra (`pokedex.txt`) | lista de 70 Pokémon y "Total: 70 Pokemon", sin traceback | pasa | E6: el catálogo pasó de 14 Pokémon cargados en el código al dataset de la cátedra |
| P02 | E1 | Opción 5 e ingresar un ítem inexistente | entrada = `-1` | mensaje "No existe ese Pokemon." y el menú vuelve a mostrarse | pasa |  |
| P03 | E2 | Opción 5 sobre una forma final (sube 2 escalones hasta la base) | entrada = `6` (Charizard) | `Charmander -> Charmeleon -> Charizard` | pasa | Es el ejemplo de la traza del informe |
| P04 | E2 | Opción 5 sobre una forma final (caso base de `cadenas_desde`: no tiene evolución siguiente) | entrada = `9` (Blastoise) | `Squirtle -> Wartortle -> Blastoise` | pasa |  |
| P05 | E3 | Opción 6: agregar al equipo hasta el tope | ids 1 a 7 | el séptimo falla con "El equipo ya tiene 6 Pokemon." (`ColeccionLlenaError`) y el menú sigue | pasa |  |
| P06 | E3 | Opción 7 (deshacer) con el historial vacío | pila vacía | "La pila esta vacia." (`PilaVaciaError`), el menú sigue | pasa |  |
| P07 | E3 | Opción 8 (siguiente turno) con la cola vacía | cola vacía | "La cola esta vacia." (`ColaVaciaError`), el menú sigue | pasa |  |
| P08 | E3 | Opción 6 con 2 Pokémon: el equipo se lista con el iterador | ids `25` y `133` | `Equipo (2 de 6)`: Pikachu, Eevee, en el orden en que se agregaron | pasa |  |
| P09 | E4 | Opción 3 → 1 (lineal) con un nombre que existe | `Mewtwo` | lo encuentra y muestra sus datos | pasa |  |
| P10 | E4 | Opción 3 → 1 (lineal) con un nombre que no existe | `Missingno` | "No se encontró…", sin traceback, el menú sigue | pasa |  |
| P11 | E4 | Recién arrancado (no ordenado por nombre): opción 3 → 2 (binaria) | `Dragonite`, después `bulbasaur` | avisa que reordena por nombre y lo encuentra; no da un falso "no encontrado" | pasa | La segunda búsqueda ya no avisa porque el catálogo quedó ordenado |
| P12 | E4 | Opción 4: por nombre (selección), después por tipo (inserción), después por número (selección) | catálogo completo | el orden cambia cada vez | pasa | Ordenado por tipo, cada grupo queda en orden alfabético: inserción es estable |
| P13 | E5 | Opción 10 → 1 (alta); salir con 0; volver a iniciar y listar (opción 1) | id `900`, nombre `Articunox`, tipo `Hielo`/`Volador`, stats 90/85/100/85, generación 1 | Articunox aparece después del reinicio y el total pasa a 71 | pasa | Los cambios del CLI se guardan en `data/catalogo.txt`; `pokedex.txt` no se toca. Después se dio de baja (P20) |
| P14 | E5 | Opción 9 → 3 (guardar BIN); opción 9 → 5 (actualizar posición); opción 9 → 4 (cargar BIN) y listar | posición `0`; nombre `Prueba`; tipos sin cambiar | Al cargar BIN, el registro 0 muestra `Prueba`; los otros 69 no cambian | pasa | El archivo mide 9 + 70 × 58 = 4069 bytes. Se escribe con `seek(9 + 0 × 58)` sin reescribir el archivo |
| P15 | E5 | Opción 9 → 4 (cargar BIN) con archivos dañados; iniciar el programa con un `catalogo.txt` dañado | BIN de 3 bytes, BIN con magia `XXXX`, BIN truncado; TXT con encabezado incorrecto, una fila con campos de menos o un número inválido | BIN: informa el error (`ArchivoInvalidoError`) y el menú sigue. TXT al iniciar: informa el error y el programa termina sin traceback | pasa | No se suben los archivos de prueba |
| P16 | E2 | Opción 5 sobre una forma intermedia (sube 1 escalón, después baja) | entrada = `5` (Charmeleon) | `Charmander -> Charmeleon -> Charizard` | pasa | Verifica que incluya al anterior y al siguiente |
| P17 | E2 | Opción 5 sobre el primero de una línea evolutiva (no tiene anterior) | entrada = `7` (Squirtle) | `Squirtle -> Wartortle -> Blastoise` | pasa | `buscar_base` entra directo a su caso base porque nadie evoluciona en 7 |
| P18 | E2 | Opción 5 con un id fuera del catálogo | entrada = `99` | mensaje "No existe ese Pokemon.", sin traceback, el menú sigue | pasa |  |
| P19 | E2 | Opción 5 con texto que no es un número | entrada = `abc` | mensaje "Tenes que ingresar un numero entero.", sin traceback, el menú sigue | pasa |  |
| P20 | E5 | Opción 10 → 3 (modificar), reiniciar; después opción 10 → 2 (baja), reiniciar | id `900` (creado en P13): nombre `ArtiNuevo`, ataque `99`; después baja del 900 | Tras reiniciar se ve `ArtiNuevo` con ataque 99; tras la baja el 900 no aparece y el total vuelve a 70 | pasa |  |
| P21 | E6 | Opción 5 sobre un Pokémon con varias evoluciones | entrada = `135` (Jolteon) | tres líneas: `Eevee -> Vaporeon`, `Eevee -> Jolteon`, `Eevee -> Flareon` | pasa | Usa `evoluciones.txt`: Eevee (133) tiene tres destinos |
| P22 | E6 | Clone limpio: arrancar sin `data/catalogo.txt` | repo recién clonado | crea `catalogo.txt` copiando `pokedex.txt` y lista 70 Pokémon | pasa | `catalogo.txt` y `catalogo.bin` están en `.gitignore` |
