import struct

from src.excepciones import ArchivoInvalidoError


FORMATO_HEADER = "<4s1sI"
FORMATO_REGISTRO = "<I20s12s12s5H"

TAM_HEADER = struct.calcsize(FORMATO_HEADER)
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)

MAGIA = b"AYED"
TEMA_POKEDEX = b"P"

CAMPOS_NUMERICOS = ["hp", "ataque", "defensa", "velocidad", "generacion"]


def _valor(item, campo):
    if isinstance(item, dict):
        return item[campo]
    return getattr(item, campo)


def _texto_a_bytes(valor, ancho, campo):
    texto = str(valor)
    codificado = texto.encode("utf-8")

    if b"\x00" in codificado:
        raise ArchivoInvalidoError(
            f"El campo {campo} contiene un byte nulo."
        )
    if len(codificado) > ancho:
        raise ArchivoInvalidoError(
            f"El campo {campo} supera el máximo de {ancho} bytes UTF-8."
        )

    return codificado


def _empaquetar_registro(item):
    try:
        id_pokemon = int(_valor(item, "id"))
        nombre = _texto_a_bytes(_valor(item, "nombre"), 20, "nombre")
        tipo1 = _texto_a_bytes(_valor(item, "tipo1"), 12, "tipo1")
        tipo2 = _texto_a_bytes(_valor(item, "tipo2"), 12, "tipo2")

        numeros = []
        for campo in CAMPOS_NUMERICOS:
            numeros.append(int(_valor(item, campo)))

        return struct.pack(
            FORMATO_REGISTRO,
            id_pokemon,
            nombre,
            tipo1,
            tipo2,
            *numeros,
        )
    except (KeyError, AttributeError, TypeError, ValueError, struct.error) as error:
        if isinstance(error, ArchivoInvalidoError):
            raise
        raise ArchivoInvalidoError(
            f"Registro inválido para guardar: {error}"
        ) from error


def _desempaquetar_registro(datos):
    try:
        id_pokemon, nombre, tipo1, tipo2, *numeros = struct.unpack(
            FORMATO_REGISTRO,
            datos,
        )
        fila = {
            "id": str(id_pokemon),
            "nombre": nombre.rstrip(b"\x00").decode("utf-8"),
            "tipo1": tipo1.rstrip(b"\x00").decode("utf-8"),
            "tipo2": tipo2.rstrip(b"\x00").decode("utf-8"),
        }
        for campo, numero in zip(CAMPOS_NUMERICOS, numeros):
            fila[campo] = str(numero)
        return fila
    except (UnicodeDecodeError, struct.error) as error:
        raise ArchivoInvalidoError(
            f"Registro binario inválido: {error}"
        ) from error


def _leer_archivo_validado(ruta):
    with open(ruta, "rb") as archivo:
        datos = archivo.read()

    if len(datos) < TAM_HEADER:
        raise ArchivoInvalidoError("El archivo binario no contiene un header completo.")

    magia, tema, cantidad = struct.unpack(
        FORMATO_HEADER,
        datos[:TAM_HEADER],
    )

    if magia != MAGIA:
        raise ArchivoInvalidoError("La magia del archivo binario no es AYED.")
    if tema != TEMA_POKEDEX:
        raise ArchivoInvalidoError("El archivo binario no corresponde a Pokédex.")

    tamanio_esperado = TAM_HEADER + cantidad * TAM_REGISTRO
    if len(datos) != tamanio_esperado:
        raise ArchivoInvalidoError(
            "El tamaño del archivo binario no coincide con la cantidad "
            "de registros indicada en el header."
        )

    return datos, cantidad


def guardar_binario(ruta, items):
    registros = [_empaquetar_registro(item) for item in items]
    header = struct.pack(
        FORMATO_HEADER,
        MAGIA,
        TEMA_POKEDEX,
        len(registros),
    )

    with open(ruta, "wb") as archivo:
        archivo.write(header)
        for registro in registros:
            archivo.write(registro)


def cargar_binario(ruta):
    datos, cantidad = _leer_archivo_validado(ruta)
    filas = []

    for posicion in range(cantidad):
        inicio = TAM_HEADER + posicion * TAM_REGISTRO
        fin = inicio + TAM_REGISTRO
        filas.append(_desempaquetar_registro(datos[inicio:fin]))

    return filas


def actualizar_registro(ruta, posicion, item):
    if not isinstance(posicion, int) or posicion < 0:
        raise ArchivoInvalidoError("La posición debe ser un entero no negativo.")

    _, cantidad = _leer_archivo_validado(ruta)
    if posicion >= cantidad:
        raise ArchivoInvalidoError(
            f"La posición {posicion} está fuera del archivo "
            f"(cantidad: {cantidad})."
        )

    registro = _empaquetar_registro(item)
    desplazamiento = TAM_HEADER + posicion * TAM_REGISTRO

    with open(ruta, "r+b") as archivo:
        archivo.seek(desplazamiento)
        archivo.write(registro)
