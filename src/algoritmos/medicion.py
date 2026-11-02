import time

from src.dominio.pokedex import Pokedex, clave_nombre
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion, ordenar_shell

FACTORES = [1, 10, 100]      # catálogo original, x10 y x100
MINIMO_SEGUNDOS = 0.05
NO_EXISTE = "missingno"      # para medir el peor caso de las búsquedas


def tiempo_promedio(operacion):
    """Repite la operación hasta juntar MINIMO_SEGUNDOS y promedia. Mejor de 3."""
    mejor = None
    for _ in range(3):
        repeticiones = 0
        inicio = time.perf_counter()
        while True:
            operacion()
            repeticiones += 1
            transcurrido = time.perf_counter() - inicio
            if transcurrido >= MINIMO_SEGUNDOS:
                break
        promedio = transcurrido / repeticiones
        if mejor is None or promedio < mejor:
            mejor = promedio
    return mejor


def main():
    dex = Pokedex()
    dex.cargar_datos_iniciales()
    print("| Operación | n | segundos |")
    print("| --- | --- | --- |")
    for factor in FACTORES:
        datos = dex.pokemones * factor
        ordenados = ordenar_insercion(datos, clave_nombre)
        n = len(datos)
        filas = [
            ("búsqueda lineal, peor caso",
             lambda: busqueda_lineal(datos, NO_EXISTE, clave_nombre)),
            ("búsqueda binaria, peor caso",
             lambda: busqueda_binaria(ordenados, NO_EXISTE, clave_nombre)),
            ("ordenar por selección",
             lambda: ordenar_seleccion(datos, clave_nombre)),
            ("ordenar por inserción",
             lambda: ordenar_insercion(datos, clave_nombre)),
            ("ordenar por inserción, lista ya ordenada",
             lambda: ordenar_insercion(ordenados, clave_nombre)),
            ("ordenar por shell (extra)",
             lambda: ordenar_shell(datos, clave_nombre)),
        ]
        for nombre, operacion in filas:
            print(f"| {nombre} | {n} | {tiempo_promedio(operacion):.7f} |")


if __name__ == "__main__":
    main()
