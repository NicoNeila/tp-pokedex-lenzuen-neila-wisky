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

- Función: buscar_pokemon_base() es recursiva, no frena hasta encontrar el pokemon base, el que usamos como parametro para arrancar la cadena
- Caso base: Cuando ningún pokemon evoluciona en el ID recibido, lo consideramos pokemon base. 
- Caso recursivo: En caso de arrancar por el último del eslabon, necesitamos retroceder recursivamente hasta llegar al punto inicial.
- Traza de un ejemplo real del dataset: 
```text
listar_cadena_evolutiva(6)              # el usuario elige Charizard
  buscar_pokemon_base(6)
    Charmeleon (id 5) evoluciona en 6 → buscar_pokemon_base(5)
      Charmander (id 4) evoluciona en 5 → buscar_pokemon_base(4)
        nadie evoluciona en 4 → caso base, devuelve Charmander
      ← Charmander
    ← Charmander
  recorro hacia adelante: Charmander → Charmeleon → Charizard → fin
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

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
