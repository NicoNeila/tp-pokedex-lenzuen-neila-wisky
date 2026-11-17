# TP integrador — AyED C2 2026

Repositorio del grupo. Partir de este esqueleto. No borrar la estructura de `src/` ni de `docs/`.

## Integrantes

| Nombre | Mail | GitHub |
| --- | --- | --- |
| Neila, Cristian Nicolás | nico.neila@gmail.com | @NicoNeila |
| Lenzuen, Maximiliano | maximilianolenzuen@gmail.com | @Maximilianolenzuen |
| Wisky, Valentín | valentin10wisky@hotmail.com | @Valentin-wisky |

**Tema elegido:** Pokédex

## Cómo ejecutar

Desde la raíz del repo, con Python 3.10 o superior:

```text
python -m src.main
```

En Windows, si `python` no anda: `py -3 -m src.main`.

Solo biblioteca estándar. No hay `requirements.txt` a propósito.

## Persistencia (E5)

El catálogo que usa la aplicación se carga desde `data/catalogo.txt`. Si ese
archivo no existe, se crea con el catálogo inicial de 14 Pokémon. La opción 9
del menú permite guardar/cargar TXT o BIN y actualizar un registro binario por
posición; la opción 10 permite dar de alta, baja y modificar Pokémon, cambios
que se guardan en el TXT. El archivo `data/catalogo.bin` se genera al usar la
opción de guardado binario y está excluido de Git.

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
