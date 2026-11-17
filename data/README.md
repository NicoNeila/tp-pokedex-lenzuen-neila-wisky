# Datasets

Elegí **un** tema. Los archivos `.txt` de los otros dos temas se pueden dejar en la carpeta; no hace falta borrarlos.

Archivos de **texto simple**: codificación UTF-8, **un registro por línea**, campos separados por coma, la primera línea es el encabezado con los nombres de los campos.

| Tema | Archivos | Relación recursiva |
| --- | --- | --- |
| Pokédex | `pokedex.txt`, `evoluciones.txt` | `origen_id` → `destino_id` (una fila por evolución; Eevee tiene varias) |
| Recetario | `recetas.txt`, `ingredientes.txt`, `subrecetas.txt` | `receta_id` usa `subreceta_id` |
| Biblioteca musical | `canciones.txt`, `versiones.txt` | `cancion_id` es versión de `version_de_id` (`cover`, `live`, `remix`) |

No hardcodees las filas en el código: leé los `.txt` (recién en E5).

La aplicación de E5 usa `catalogo.txt` para persistir el modelo actual de
Pokédex (`id`, `nombre`, `tipo1`, `tipo2`, `evolucion`). Ese catálogo inicial
contiene los 14 Pokémon que ya cargaba el programa; no es una conversión del
dataset ampliado de `pokedex.txt`, que además tiene estadísticas y 70 filas.
La aplicación puede generar `catalogo.bin` desde su menú; ese binario es local
y no se versiona.
