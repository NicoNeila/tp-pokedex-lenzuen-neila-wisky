# TP integrador — AyED C2 2026

Repositorio del grupo. Partir de este esqueleto. No borrar la estructura de `src/` ni de `docs/`.

## Integrantes

| Nombre | Mail | GitHub |
| --- | --- | --- |
| Neila, Cristian Nicolás | nico.neila@gmail.com | @NicoNeila |
| Lenzuen, Maximiliano | maximilianolenzuen@gmail.com | @Maximilianolenzuen |
| Wisky, Valentín | valentin10wisky@hotmail.com | @Valentin-wisky |

**Tema elegido:** Pokédex

Programa de consola para consultar una Pokédex: lista, busca y ordena Pokémon, muestra sus líneas evolutivas, arma un equipo de combate de hasta 6 y guarda el catálogo en archivos de texto y binario.

## Cómo ejecutar

Desde la raíz del repo, con Python 3.10 o superior:

```text
python -m src.main
```

En Windows, si `python` no anda: `py -3 -m src.main`.

Solo biblioteca estándar. No hay `requirements.txt` a propósito.

Mediciones de los algoritmos (informe §5): `python -m src.algoritmos.medicion`.

## Menú

| Opción | Qué hace |
| --- | --- |
| 1 | Listar el catálogo |
| 2 | Ver detalle de un Pokémon (por id o nombre): tipos, estadísticas y evoluciones |
| 3 | Buscar por nombre: lineal o binaria (si no está ordenado por nombre, lo ordena y avisa) |
| 4 | Ordenar por nombre, número o tipo, con selección, inserción o shell |
| 5 | Línea evolutiva (recursión): todas las cadenas de la familia del Pokémon |
| 6 | Agregar al equipo (lista enlazada, máximo 6); también lo apila en el historial y lo encola en los turnos |
| 7 | Deshacer el último agregado (pila) |
| 8 | Siguiente turno de pelea (cola) |
| 9 | Guardar / cargar TXT y BIN, y actualizar un registro del BIN por posición |
| 10 | Alta / baja / modificación del catálogo, guardada en el TXT |
| 0 | Salir |

## Datos

- Dataset de la cátedra: `data/pokedex.txt` (70 Pokémon) y `data/evoluciones.txt` (42 evoluciones). El programa no los modifica.
- `data/catalogo.txt`: copia de trabajo. Se crea desde `pokedex.txt` la primera vez y guarda el ABM. Para volver al dataset original, borrarla.
- `data/catalogo.bin`: se genera con la opción 9. Layout en `docs/INFORME.md` §6.
- Los dos archivos generados están en `.gitignore`.

## Limitaciones

- El catálogo se guarda en un `list` de Python para poder ordenarlo y buscarlo; las listas enlazadas se usan en el equipo, el historial y los turnos.
- Las evoluciones se leen de `evoluciones.txt` y no se editan desde el menú: un Pokémon dado de alta no tiene evoluciones.
- El equipo, el historial y la cola de turnos no se guardan: se pierden al salir.
- Deshacer saca al Pokémon del equipo, pero no de la cola de turnos.
- La búsqueda por nombre es por nombre completo (sin importar mayúsculas), no por parte del nombre.
- En el binario el nombre ocupa hasta 20 bytes y cada tipo hasta 12 bytes UTF-8; las estadísticas van de 0 a 65535. Si un valor no entra, se rechaza.
- Actualizar un registro del binario por posición no cambia el TXT.

## Entregas

Cada vencimiento se marca con un tag. Ver `GIT.md`.

| Tag | Vence |
| --- | --- |
| `preentrega` (opcional, solo repo) | domingo 30-ago-2026 23:59 |
| `entrega-1` | domingo 06-sep-2026 23:59 |
| `entrega-2` | domingo 20-sep-2026 23:59 |
| `entrega-3` | domingo 04-oct-2026 23:59 |
| `entrega-4` | domingo 01-nov-2026 23:59 |
| `entrega-5` | domingo 15-nov-2026 23:59 |
| `entrega-6` | domingo 22-nov-2026 23:59 |

Defensa oral (reemplaza el 2do parcial): 25 y 27-nov-2026.

La cátedra corrige el **tag**, no el último commit suelto de `main`.

El grupo se avisa por mail a diego.ambrossio@unab.edu.ar **y** angel.bianco@unab.edu.ar. Ver `GIT.md`.
