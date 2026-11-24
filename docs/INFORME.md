# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokedex
- Por qué lo eligieron (5–8 líneas): Elegimos la Pokédex porque nos resulta interesante y de interés, es un tema original y menos convencional que las otras opciones disponibles. La Pokédex contiene una gran cantidad de información sobre cada Pokémon, lo que nos permite trabajar con distintos tipos de datos y organizarlos de diferentes maneras. Por estos motivos, consideramos que es una buena opción para realizar el trabajo.

## 2. Modelo

El programa trabaja sobre el dataset de la cátedra: `data/pokedex.txt` (70 Pokémon) y `data/evoluciones.txt` (42 evoluciones).

- **Ítem del catálogo:** un `Pokemon`, una fila de `pokedex.txt`: `id`, `nombre`, `tipo1`, `tipo2`, `hp`, `ataque`, `defensa`, `velocidad`, `generacion`.
- **Qué no cambia:** el `id` es la identidad del Pokémon. La modificación del ABM no deja cambiarlo.
- **Qué cambia:** nombre, tipos y estadísticas son el estado; se pueden modificar desde la opción 10.
- **Evoluciones:** no son un atributo del Pokémon. `Pokedex` guarda la lista de pares `(origen_id, destino_id)` leída de `evoluciones.txt`. Así un Pokémon puede tener varias evoluciones (Eevee tiene tres).

| Clase | Qué guarda | Estructura |
| --- | --- | --- |
| `Pokedex` | el catálogo de 70 Pokémon y las evoluciones | `list` de Python (se ordena y se busca) |
| `Equipo` | colección principal: hasta 6 Pokémon del catálogo | `ListaEnlazada` |
| `Pila` (historial) | cada Pokémon agregado al equipo, para deshacer | `ListaEnlazada` |
| `Cola` (turnos) | los Pokémon del equipo, en orden de pelea | `ListaEnlazada` |

```text
pokedex.txt ──> Pokedex.pokemones ──(opción 6)──> Equipo (ListaEnlazada, máx. 6)
evoluciones.txt ──> Pokedex.evoluciones              ├─> Pila: historial (opción 7 deshace)
                                                     └─> Cola: turnos   (opción 8 saca el próximo)
catalogo.txt <── copia de trabajo (ABM, opción 10)   catalogo.bin <── opción 9
```

## 3. Recursión (E2)

- Funciones: `Pokedex.buscar_base()` retrocede por las evoluciones hasta el Pokémon base. `Pokedex.cadenas_desde()` recorre hacia adelante y devuelve todas las líneas evolutivas desde ese Pokémon. La opción 5 usa las dos con `cadenas_evolutivas()`.
- Caso base: en `buscar_base()`, cuando ningún Pokémon evoluciona en el id recibido (ese es el base). En `cadenas_desde()`, cuando el Pokémon no tiene evoluciones: devuelve `[[nombre]]`.
- Caso recursivo: en `buscar_base()`, se llama con el id del anterior. En `cadenas_desde()`, se llama por cada evolución y se agrega el nombre actual adelante de cada cadena que vuelve.
- Traza de un ejemplo real del dataset (una sola línea):

```text
cadenas_evolutivas(6)            # el usuario elige Charizard
  buscar_base(6)
    Charmeleon (5) evoluciona en 6 → buscar_base(5)
      Charmander (4) evoluciona en 5 → buscar_base(4)
        nadie evoluciona en 4 → caso base, devuelve Charmander
  cadenas_desde(4) → siguientes: [Charmeleon]
    cadenas_desde(5) → siguientes: [Charizard]
      cadenas_desde(6) → no evoluciona → caso base, devuelve [["Charizard"]]
    ← [["Charmeleon", "Charizard"]]
  ← [["Charmander", "Charmeleon", "Charizard"]]
Charmander -> Charmeleon -> Charizard
```

- Traza con varias evoluciones (Eevee):

```text
cadenas_evolutivas(135)          # el usuario elige Jolteon
  buscar_base(135)
    Eevee (133) evoluciona en 135 → buscar_base(133)
      nadie evoluciona en 133 → caso base, devuelve Eevee
  cadenas_desde(133) → siguientes: [Vaporeon, Jolteon, Flareon]
    cadenas_desde(134) → caso base, [["Vaporeon"]]
    cadenas_desde(135) → caso base, [["Jolteon"]]
    cadenas_desde(136) → caso base, [["Flareon"]]
  ← [["Eevee", "Vaporeon"], ["Eevee", "Jolteon"], ["Eevee", "Flareon"]]
Eevee -> Vaporeon
Eevee -> Jolteon
Eevee -> Flareon
```


## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | `insertar_al_inicio`, `insertar_al_final`, `eliminar`, `buscar`, `esta_vacia`, `tamanio`, `__iter__` (generador con `yield`) | `_cantidad` es igual a la cantidad de nodos que se alcanzan desde `_cabeza`; el último nodo tiene `siguiente = None`; si está vacía, `_cabeza` es `None` y `_cantidad` es 0. No usa `list` por debajo. |
| Pila | `apilar`, `desapilar`, `ver_tope`, `esta_vacia` | el tope es siempre la cabeza de la lista: se apila y se desapila por el inicio (LIFO). Desapilar vacía lanza `PilaVaciaError`. |
| Cola | `encolar`, `desencolar`, `ver_frente`, `esta_vacia` | el frente es la cabeza: se encola al final y se desencola del inicio (FIFO). Desencolar vacía lanza `ColaVaciaError`. |

Dónde se usa cada uno en el dominio:

- `ListaEnlazada`: guarda el `Equipo` (tope 6; el séptimo lanza `ColeccionLlenaError`). La opción 6 lo lista con el iterador.
- `Pila`: historial de agregados al equipo. La opción 7 desapila el último y lo saca del equipo (deshacer).
- `Cola`: turnos de pelea. Cada Pokémon agregado al equipo se encola; la opción 8 desencola el que espera hace más tiempo.

## 5. Complejidad (E4)

Algoritmos propios en `src/algoritmos/`: `busqueda.py` (lineal y binaria) y `ordenamiento.py` (selección, inserción y shell como extra). No usan `sorted`, `list.sort`, `bisect`, `in` de pertenencia ni `.index()`.

- Opción 3 (Buscar): lineal o binaria por nombre. `Pokedex` guarda en `orden` por qué criterio está ordenado; si no está ordenado por nombre, el menú lo ordena con inserción y avisa antes de usar la binaria.
- Opción 4 (Ordenar): por nombre, número o tipo, con selección, inserción o shell.
- Opción 2 (Ver detalle): por id o por nombre (lineal).

n = cantidad de Pokémon (70 en el dataset), e = cantidad de evoluciones (42), m = tamaño del equipo (máximo 6), k = cantidad de Pokémon de una familia evolutiva.

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre la lista una vez. |
| Ver detalle | O(n + e) | O(1) | Busca de a uno por id o por nombre y recorre las e evoluciones para mostrar de dónde viene y en qué evoluciona. |
| Búsqueda lineal | O(1) mejor / O(n) peor | O(1) | Compara de a uno; si no está, compara los n. |
| Búsqueda binaria (ya ordenado) | O(log n) | O(1) | Cada comparación descarta la mitad: n, n/2, n/4… hasta 1. |
| Búsqueda binaria (hay que ordenar antes) | O(n²) la primera vez | O(n) | Ordenar por inserción domina. Después queda ordenado y las siguientes son O(log n). |
| Ordenar por selección | O(n²) siempre | O(n) | Dos ciclos anidados: (n−1) + (n−2) + … + 1 ≈ n²/2 comparaciones, aunque ya esté ordenado. O(n) de espacio por la copia que devuelve. |
| Ordenar por inserción | O(n) mejor / O(n²) peor | O(n) | Si ya está ordenado, una comparación por ítem; si está al revés, corre todo. O(n) de espacio por la copia. |
| Ordenar por shell (extra) | O(n²) peor | O(n) | Es inserción con saltos que se achican; en la práctica es mucho más rápido (ver mediciones). |
| Cadena evolutiva (recursiva) | O(k · (e + n)) | O(k) | k llamadas recursivas; cada una recorre las e evoluciones y busca por id en O(n). Espacio: la pila de llamadas. |
| Agregar al equipo | O(n + m) | O(1) | Busca por id (O(n)) e inserta al final de la lista enlazada (O(m)). |
| Deshacer / Siguiente turno | O(m) / O(1) | O(1) | Desapilar y desencolar sacan la cabeza de la lista enlazada; deshacer además lo quita del equipo. |

Estabilidad: selección no es estable e inserción sí. Ordenando por nombre y después por tipo:

| Tipo | Con inserción (estable) | Con selección (no estable) |
| --- | --- | --- |
| Planta | Bayleef, Bulbasaur, Chikorita, Gloom, Ivysaur, Meganium, Oddish, Venusaur, Vileplume | Gloom, Meganium, Bulbasaur, Ivysaur, Chikorita, Oddish, Bayleef, Venusaur, Vileplume |
| Electrico | Ampharos, Flaaffy, Jolteon, Magnemite, Magneton, Mareep, Pichu, Pikachu, Raichu | Flaaffy, Jolteon, Ampharos, Magnemite, Magneton, Mareep, Pichu, Pikachu, Raichu |

Con inserción cada tipo sigue en orden alfabético; con selección ese orden se pierde.

Mediciones (`time.perf_counter`):

Se corren con `python -m src.algoritmos.medicion` sobre el dataset de la cátedra (70) y copias x10 (700) y x100 (7000). Las búsquedas buscan un nombre que no existe (peor caso). Cada operación se repite hasta juntar 0,05 s y se promedia.

| Operación | n | segundos |
| --- | --- | --- |
| búsqueda lineal, peor caso | 70 | 0.0000050 |
| búsqueda lineal, peor caso | 700 | 0.0000448 |
| búsqueda lineal, peor caso | 7000 | 0.0004739 |
| búsqueda binaria, peor caso | 70 | 0.0000008 |
| búsqueda binaria, peor caso | 700 | 0.0000014 |
| búsqueda binaria, peor caso | 7000 | 0.0000019 |
| ordenar por selección | 70 | 0.0002891 |
| ordenar por selección | 700 | 0.0301559 |
| ordenar por selección | 7000 | 3.1260822 |
| ordenar por inserción | 70 | 0.0001875 |
| ordenar por inserción | 700 | 0.0187181 |
| ordenar por inserción | 7000 | 2.0590051 |
| ordenar por inserción, lista ya ordenada | 70 | 0.0000112 |
| ordenar por inserción, lista ya ordenada | 700 | 0.0001197 |
| ordenar por inserción, lista ya ordenada | 7000 | 0.0013791 |
| ordenar por shell (extra) | 70 | 0.0000967 |
| ordenar por shell (extra) | 700 | 0.0016330 |
| ordenar por shell (extra) | 7000 | 0.0209825 |

Cada paso multiplica n por 10:

- Búsqueda lineal: el tiempo se multiplica por unos 9 y 11 → crece como n.
- Búsqueda binaria: con n 100 veces más grande tarda solo 2,4 veces más → crece como log n.
- Selección e inserción: el tiempo se multiplica por unos 100 y 110 → crece como n².
- Inserción con la lista ya ordenada: se multiplica por unos 11 y 12 → su mejor caso, O(n).
- Shell: con n = 7000 es unas 100 veces más rápido que inserción y 150 veces más rápido que selección.


## 6. Persistencia (E5)

Al arrancar, el programa lee el dataset de la cátedra: `data/pokedex.txt` y `data/evoluciones.txt`. Esos dos archivos no se modifican. La primera vez copia `pokedex.txt` a `data/catalogo.txt`, que es la copia de trabajo: ahí se guardan el alta, baja y modificación (opción 10), y al volver a abrir el programa se carga desde ahí. Para volver al dataset original alcanza con borrar `catalogo.txt`.

Los `.txt` son CSV en UTF-8, con una fila de encabezado y una fila por registro. Columnas de `pokedex.txt` y `catalogo.txt`: `id,nombre,tipo1,tipo2,hp,ataque,defensa,velocidad,generacion`. Columnas de `evoluciones.txt`: `origen_id,destino_id`.

El archivo `data/catalogo.bin` se genera desde el menú (opción 9) y usa orden little-endian (`<`), sin padding:

| Parte | Formato `struct` | Tamaño | Campos |
| --- | --- | ---: | --- |
| Header | `<4s1sI` | 9 bytes | magia `AYED` (4 bytes), tema `P` (1 byte), cantidad (uint32, 4 bytes) |
| Registro | `<I20s12s12s5H` | 58 bytes | id (uint32), nombre (20 bytes UTF-8), tipo1 (12 bytes), tipo2 (12 bytes), hp, ataque, defensa, velocidad y generación (uint16, 2 bytes cada uno) |

Con los 70 Pokémon el archivo mide `9 + 70 * 58 = 4069` bytes. Los textos ocupan anchos fijos en bytes UTF-8 y se completan con bytes nulos. No se truncan: un valor que excede el ancho se rechaza. Al cargar se verifica la magia, el tema y que el tamaño sea exactamente `9 + cantidad * 58` bytes; si algo falla se lanza `ArchivoInvalidoError` y el menú sigue. `data/catalogo.bin` no se incluye en el repositorio.

Para actualizar un registro por posición (índice 0-based) se calcula `desplazamiento = 9 + posicion * 58`. Se abre el archivo como `r+b`, se hace `seek(desplazamiento)` y se escriben los 58 bytes del nuevo registro, sin reescribir los demás. Ejemplo: el registro 3 empieza en el byte `9 + 3 * 58 = 183`.

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
| Neila, Cristian Nicolás | E1 (tema, clase Pokemon y menú), E2 (clases Pokemon y Pokedex, recursión hacia adelante), E3 (ListaEnlazada, Pila, Cola, Equipo y menú), E4 (búsquedas, ordenamientos, mediciones e informe §5), E6 (adaptación al dataset de la cátedra, protocolo, informe y README) | TADs e invariantes, recursión, búsqueda y ordenamiento, complejidad, menú |
| Lenzuen, Maximiliano Tomás | E2 (módulos, clases y recursión del tema), E5 (texto.py, binario.py, opciones 9 y 10 del menú) | recursión, persistencia en texto y binario, `seek` y layout del registro, ABM |
| Wisky, Valentín | Abandonó la materia; no participó del trabajo | — |
