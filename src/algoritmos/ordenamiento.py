def ordenar_seleccion(coleccion, clave):
    """Ordenamiento por selección. Devuelve una nueva secuencia, no usa sorted."""
    lista = list(coleccion)
    n = len(lista)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if clave(lista[j]) < clave(lista[pos_min]):
                pos_min = j
        lista[i], lista[pos_min] = lista[pos_min], lista[i]
    return lista


def ordenar_insercion(coleccion, clave):
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted."""
    lista = list(coleccion)
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and clave(lista[j]) > clave(actual):
            lista[j + 1] = lista[j]   # corro el mayor a la derecha
            j -= 1
        lista[j + 1] = actual
    return lista


def ordenar_shell(coleccion, clave):
    """Shell sort (extra). Devuelve una nueva secuencia, no usa sorted."""
    lista = list(coleccion)
    salto = len(lista) // 2
    while salto > 0:
        for i in range(salto, len(lista)):
            actual = lista[i]
            j = i
            while j >= salto and clave(lista[j - salto]) > clave(actual):
                lista[j] = lista[j - salto]
                j -= salto
            lista[j] = actual
        salto = salto // 2
    return lista
