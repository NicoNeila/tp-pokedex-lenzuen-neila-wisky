import time

from src.dominio.pokedex import clave_nombre
from src.persistencia.texto import cargar_texto
from src.main import RUTA_POKEDEX, _filas_a_pokemones
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion, ordenar_shell

FACTORES = [1, 10, 100]
MINIMO_SEGUNDOS = 0.05
NO_EXISTE = "missingno"


def tiempo_promedio(operacion):
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
    pokemones = _filas_a_pokemones(cargar_texto(RUTA_POKEDEX))
    print("| Operación | n | segundos |")
    print("| --- | --- | --- |")
    for factor in FACTORES:
        datos = pokemones * factor
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
