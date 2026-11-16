import csv

from src.excepciones import ArchivoInvalidoError


ENCABEZADOS_POKEDEX = [
    "id",
    "nombre",
    "tipo1",
    "tipo2",
    "evolucion",
]


def cargar_texto(ruta):
    """Carga un CSV UTF-8 y devuelve una lista de diccionarios."""
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames != ENCABEZADOS_POKEDEX:
                raise ArchivoInvalidoError(
                    f"Encabezado inválido en {ruta}. "
                    f"Se esperaba: {','.join(ENCABEZADOS_POKEDEX)}"
                )

            filas = []
            for numero_linea, fila in enumerate(lector, start=2):
                if None in fila or any(valor is None for valor in fila.values()):
                    raise ArchivoInvalidoError(
                        f"Cantidad de campos inválida en {ruta}, "
                        f"línea {numero_linea}."
                    )
                filas.append(fila)

            return filas
    except (UnicodeDecodeError, csv.Error) as error:
        raise ArchivoInvalidoError(
            f"No se pudo interpretar el archivo de texto {ruta}: {error}"
        ) from error


def guardar_texto(ruta, filas, encabezados=ENCABEZADOS_POKEDEX):
    """Guarda filas como CSV UTF-8 con encabezado."""
    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(
                archivo,
                fieldnames=encabezados,
                extrasaction="raise",
            )
            escritor.writeheader()
            escritor.writerows(filas)
    except (csv.Error, ValueError) as error:
        raise ArchivoInvalidoError(
            f"No se pudieron guardar los datos en {ruta}: {error}"
        ) from error