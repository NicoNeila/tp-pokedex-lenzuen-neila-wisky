# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Pokedex
- Por qué lo eligieron (5–8 líneas): Elegimos la Pokédex porque nos resulta interesante y de interés, es un tema original y menos convencional que las otras opciones disponibles. La Pokédex contiene una gran cantidad de información sobre cada Pokémon, lo que nos permite trabajar con distintos tipos de datos y organizarlos de diferentes maneras. Por estos motivos, consideramos que es una buena opción para realizar el trabajo.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Las listas y los diccionarios son mutables. Los strings y los números son inmutables.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: Pokedex.buscar_base() es recursiva, no frena hasta encontrar el pokemon base, el que usamos como parametro para arrancar la cadena. También es recursiva Pokedex.cadena_desde(), que recorre la cadena hacia adelante.
- Caso base: en buscar_base(), cuando ningún pokemon evoluciona en el ID recibido, lo consideramos pokemon base. En cadena_desde(), cuando el pokemon no tiene evolución siguiente.
- Caso recursivo: en buscar_base(), en caso de arrancar por el último del eslabon, necesitamos retroceder recursivamente hasta llegar al punto inicial. En cadena_desde(), [nombre] + cadena_desde(evolucion).
- Traza de un ejemplo real del dataset:

```text
cadena_evolutiva(6)              # el usuario elige Charizard
  buscar_base(6)
    Charmeleon (id 5) evoluciona en 6 → buscar_base(5)
      Charmander (id 4) evoluciona en 5 → buscar_base(4)
        nadie evoluciona en 4 → caso base, devuelve Charmander
      ← Charmander
    ← Charmander
  cadena_desde(4) → ["Charmander"] + cadena_desde(5)
    cadena_desde(5) → ["Charmeleon"] + cadena_desde(6)
      cadena_desde(6) → Charizard no evoluciona → caso base, devuelve ["Charizard"]
  ← ["Charmander", "Charmeleon", "Charizard"]
```


## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

Algoritmos propios en `src/algoritmos/`: `busqueda.py` (lineal y binaria) y `ordenamiento.py` (selección, inserción y shell como extra). No usan `sorted`, `list.sort`, `bisect`, `in` de pertenencia ni `.index()`.

- Opción 3 (Buscar): lineal o binaria por nombre. `Pokedex` guarda en `orden` por qué criterio está ordenado; si no está ordenado por nombre, el menú lo ordena con inserción y avisa antes de usar la binaria.
- Opción 4 (Ordenar): por nombre, número o tipo, con selección, inserción o shell.
- Opción 2 (Ver detalle): por id o por nombre (lineal).

n = cantidad de Pokémon, m = tamaño del equipo (máximo 6), k = largo de una cadena evolutiva.

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre la lista una vez. |
| Ver detalle | O(n) | O(1) | Busca de a uno por id o por nombre. |
| Búsqueda lineal | O(1) mejor / O(n) peor | O(1) | Compara de a uno; si no está, compara los n. |
| Búsqueda binaria (ya ordenado) | O(log n) | O(1) | Cada comparación descarta la mitad: n, n/2, n/4… hasta 1. |
| Búsqueda binaria (hay que ordenar antes) | O(n²) la primera vez | O(n) | Ordenar por inserción domina. Después queda ordenado y las siguientes son O(log n). |
| Ordenar por selección | O(n²) siempre | O(n) | Dos ciclos anidados: (n−1) + (n−2) + … + 1 ≈ n²/2 comparaciones, aunque ya esté ordenado. O(n) de espacio por la copia que devuelve. |
| Ordenar por inserción | O(n) mejor / O(n²) peor | O(n) | Si ya está ordenado, una comparación por ítem; si está al revés, corre todo. O(n) de espacio por la copia. |
| Ordenar por shell (extra) | O(n²) peor | O(n) | Es inserción con saltos que se achican; en la práctica es mucho más rápido (ver mediciones). |
| Cadena evolutiva (recursiva) | O(k · n) | O(k) | k llamadas recursivas y cada una busca por id en O(n). Espacio: la pila de llamadas. |
| Agregar al equipo | O(n + m) | O(1) | Busca por id (O(n)) e inserta al final de la lista enlazada (O(m)). |
| Deshacer / Siguiente turno | O(m) / O(1) | O(1) | Desapilar y desencolar sacan la cabeza de la lista enlazada; deshacer además lo quita del equipo. |

Estabilidad: selección no es estable e inserción sí. Ordenando por nombre y después por tipo:

| Tipo | Con inserción (estable) | Con selección (no estable) |
| --- | --- | --- |
| Fuego | Charizard, Charmander, Charmeleon | Charmander, Charmeleon, Charizard |
| Planta | Bulbasaur, Ivysaur, Sceptile, Venusaur | Sceptile, Bulbasaur, Venusaur, Ivysaur |

Con inserción cada tipo sigue en orden alfabético; con selección ese orden se pierde.

Mediciones (`time.perf_counter`):

Se corren con `python -m src.algoritmos.medicion` (en Google Colab) sobre el catálogo original (14) y copias x10 (140) y x100 (1400). Las búsquedas buscan un nombre que no existe (peor caso). Cada operación se repite hasta juntar 0,05 s y se promedia.

| Operación | n | segundos |
| --- | --- | --- |
| búsqueda lineal, peor caso | 14 | 0.0000021 |
| búsqueda lineal, peor caso | 140 | 0.0000171 |
| búsqueda lineal, peor caso | 1400 | 0.0001645 |
| búsqueda binaria, peor caso | 14 | 0.0000012 |
| búsqueda binaria, peor caso | 140 | 0.0000018 |
| búsqueda binaria, peor caso | 1400 | 0.0000030 |
| ordenar por selección | 14 | 0.0000248 |
| ordenar por selección | 140 | 0.0022542 |
| ordenar por selección | 1400 | 0.2403457 |
| ordenar por inserción | 14 | 0.0000142 |
| ordenar por inserción | 140 | 0.0012176 |
| ordenar por inserción | 1400 | 0.1338811 |
| ordenar por inserción, lista ya ordenada | 14 | 0.0000042 |
| ordenar por inserción, lista ya ordenada | 140 | 0.0000391 |
| ordenar por inserción, lista ya ordenada | 1400 | 0.0004432 |
| ordenar por shell (extra) | 14 | 0.0000124 |
| ordenar por shell (extra) | 140 | 0.0003141 |
| ordenar por shell (extra) | 1400 | 0.0052767 |

Cada paso multiplica n por 10:

- Búsqueda lineal: el tiempo se multiplica por unos 8 y 10 → crece como n.
- Búsqueda binaria: con n 100 veces más grande tarda solo 2,5 veces más → crece como log n.
- Selección e inserción: el tiempo se multiplica por unos 90 y 110 → crece como n².
- Inserción con la lista ya ordenada: se multiplica por unos 9 y 11 → su mejor caso, O(n).
- Shell: con n = 1400 es unas 25 veces más rápido que inserción y 45 veces más rápido que selección.


## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
