# Datasets

Elegí **un** tema. Los archivos `.txt` de los otros dos temas se pueden dejar en la carpeta; no hace falta borrarlos.

Archivos de **texto simple**: codificación UTF-8, **un registro por línea**, campos separados por coma, la primera línea es el encabezado con los nombres de los campos.

| Tema | Archivos | Relación recursiva |
| --- | --- | --- |
| Pokédex | `pokedex.txt`, `evoluciones.txt` | `origen_id` → `destino_id` (una fila por evolución; Eevee tiene varias) |
| Recetario | `recetas.txt`, `ingredientes.txt`, `subrecetas.txt` | `receta_id` usa `subreceta_id` |
| Biblioteca musical | `canciones.txt`, `versiones.txt` | `cancion_id` es versión de `version_de_id` (`cover`, `live`, `remix`) |

No hardcodees las filas en el código: leé los `.txt` (recién en E5).

La aplicación lee `pokedex.txt` y `evoluciones.txt` y no los modifica. La
1ra vez copia `pokedex.txt` a `catalogo.txt`, es la copia de trabajo
donde se guarda el alta, baja y modificación. `catalogo.txt` y `catalogo.bin`
los genera el programa y no se suben al repositorio.
