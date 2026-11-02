def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """Recorre de a uno. Devuelve el ítem cuya clave coincide, o None. O(n)."""
    for item in coleccion:
        if obtener_clave is None:
            valor = item
        else:
            valor = obtener_clave(item)
        if valor == clave:
            return item
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave. O(log n)."""
    izq = 0
    der = len(coleccion_ordenada) - 1
    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion_ordenada[medio])
        if valor == clave:
            return coleccion_ordenada[medio]
        elif valor < clave:
            izq = medio + 1   # la clave está a la derecha
        else:
            der = medio - 1   # la clave está a la izquierda
    return None
