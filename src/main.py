from pathlib import Path

from src.config import TEMA
from src.dominio.pokedex import Pokedex, CRITERIOS
from src.dominio.equipo import Equipo
from src.dominio.pokemon import Pokemon
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import (
    ArchivoInvalidoError,
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
)
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion, ordenar_shell
from src.persistencia.texto import (
    ENCABEZADOS_POKEDEX,
    ENCABEZADOS_EVOLUCIONES,
    cargar_texto,
    guardar_texto,
)
from src.persistencia.binario import (
    actualizar_registro,
    cargar_binario,
    guardar_binario,
)

OPCIONES_CRITERIO = {"1": "nombre", "2": "numero", "3": "tipo"}

ALGORITMOS = {
    "1": ("selección", ordenar_seleccion),
    "2": ("inserción", ordenar_insercion),
    "3": ("shell", ordenar_shell),
}

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

RUTA_DATOS = Path(__file__).resolve().parents[1] / "data"
RUTA_POKEDEX = RUTA_DATOS / "pokedex.txt"
RUTA_EVOLUCIONES = RUTA_DATOS / "evoluciones.txt"
RUTA_CATALOGO = RUTA_DATOS / "catalogo.txt"
RUTA_BINARIO = RUTA_DATOS / "catalogo.bin"

CAMPOS_NUMERICOS = ["hp", "ataque", "defensa", "velocidad", "generacion"]


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Equipo -Agregar-")
    print("7. Historial -Deshacer-")
    print("8. Cola -Siguiente turno-")
    print("9. Guardar / cargar archivos")
    print("10. Alta / baja / modificación del catálogo")
    print("0. Salir")


def _pokemon_a_fila(pokemon):
    fila = {
        "id": str(pokemon.id),
        "nombre": pokemon.nombre,
        "tipo1": pokemon.tipo1,
        "tipo2": pokemon.tipo2,
    }
    for campo in CAMPOS_NUMERICOS:
        fila[campo] = str(getattr(pokemon, campo))
    return fila


def _fila_a_pokemon(fila):
    try:
        id_pokemon = int(fila["id"])
        nombre = fila["nombre"].strip()
        tipo1 = fila["tipo1"].strip()
        tipo2 = fila["tipo2"].strip()
        numeros = []
        for campo in CAMPOS_NUMERICOS:
            numeros.append(int(fila[campo]))
    except (KeyError, AttributeError, TypeError, ValueError) as error:
        raise ValueError(f"registro incompleto o con valores inválidos: {error}") from error

    return Pokemon(id_pokemon, nombre, tipo1, tipo2, *numeros)


def _validar_catalogo(pokemones):
    ids = set()
    for pokemon in pokemones:
        if pokemon.id <= 0:
            raise ValueError("los ids deben ser enteros positivos.")
        if pokemon.id in ids:
            raise ValueError(f"el id {pokemon.id} está repetido.")
        if not pokemon.nombre.strip() or not pokemon.tipo1.strip():
            raise ValueError("cada Pokémon debe tener nombre y tipo principal.")
        for campo in CAMPOS_NUMERICOS:
            if getattr(pokemon, campo) < 0:
                raise ValueError(f"{campo} no puede ser negativo.")
        ids.add(pokemon.id)


def _filas_a_pokemones(filas):
    try:
        pokemones = [_fila_a_pokemon(fila) for fila in filas]
        _validar_catalogo(pokemones)
        return pokemones
    except ValueError as error:
        raise ArchivoInvalidoError(f"Catálogo inválido: {error}") from error


def _guardar_catalogo(pokemones):
    _validar_catalogo(pokemones)
    filas = [_pokemon_a_fila(pokemon) for pokemon in pokemones]
    guardar_texto(RUTA_CATALOGO, filas, ENCABEZADOS_POKEDEX)


def _cargar_catalogo_texto():
    return _filas_a_pokemones(cargar_texto(RUTA_CATALOGO))


def _cargar_catalogo_binario():
    return _filas_a_pokemones(cargar_binario(RUTA_BINARIO))


def _cargar_evoluciones():
    evoluciones = []
    for fila in cargar_texto(RUTA_EVOLUCIONES, ENCABEZADOS_EVOLUCIONES):
        try:
            evoluciones.append((int(fila["origen_id"]), int(fila["destino_id"])))
        except ValueError as error:
            raise ArchivoInvalidoError(f"Evolución inválida: {error}") from error
    return evoluciones


def _pedir_entero(mensaje, actual=None):
    if actual is None:
        texto = input(f"{mensaje}: ").strip()
    else:
        texto = input(f"{mensaje} [{actual}]: ").strip()
        if texto == "":
            return actual
    return int(texto)


def _reemplazar_catalogo(dex, pokemones):
    _validar_catalogo(pokemones)
    _guardar_catalogo(pokemones)
    dex.pokemones = pokemones
    dex.orden = None


def manejar_archivos(dex):
    print("Archivos: 1) Guardar TXT  2) Cargar TXT")
    print("          3) Guardar BIN  4) Cargar BIN")
    print("          5) Actualizar registro BIN por posición")
    opcion = input("> ").strip()

    try:
        if opcion == "1":
            _guardar_catalogo(dex.pokemones)
            print(f"Catálogo guardado en {RUTA_CATALOGO}.")
        elif opcion == "2":
            dex.pokemones = _cargar_catalogo_texto()
            dex.orden = None
            print("Catálogo cargado desde TXT.")
        elif opcion == "3":
            guardar_binario(RUTA_BINARIO, dex.pokemones)
            print(f"Catálogo guardado en {RUTA_BINARIO}.")
        elif opcion == "4":
            dex.pokemones = _cargar_catalogo_binario()
            dex.orden = None
            print("Catálogo cargado desde BIN.")
        elif opcion == "5":
            catalogo_binario = _cargar_catalogo_binario()
            posicion = int(input("Posición 0-based del registro: ").strip())
            if posicion < 0 or posicion >= len(catalogo_binario):
                print("Posición fuera del catálogo.")
                return

            actual = catalogo_binario[posicion]
            print(f"Registro {posicion}: N.º {actual.id} — {actual.nombre}")
            nombre = input(f"Nombre [{actual.nombre}]: ").strip() or actual.nombre
            tipo1 = input(f"Tipo principal [{actual.tipo1}]: ").strip() or actual.tipo1
            tipo2_ingresado = input(
                f"Tipo secundario [{actual.tipo2}] (vacío conserva, - elimina): "
            ).strip()
            tipo2 = (
                actual.tipo2
                if tipo2_ingresado == ""
                else "" if tipo2_ingresado == "-" else tipo2_ingresado
            )
            actualizado = Pokemon(
                actual.id,
                nombre,
                tipo1,
                tipo2,
                actual.hp,
                actual.ataque,
                actual.defensa,
                actual.velocidad,
                actual.generacion,
            )
            catalogo_binario[posicion] = actualizado
            _validar_catalogo(catalogo_binario)
            actualizar_registro(RUTA_BINARIO, posicion, actualizado)
            dex.pokemones = _cargar_catalogo_binario()
            dex.orden = None
            print("Registro binario actualizado por posición.")
            print("El TXT no cambia; para persistir allí, guardalo también como TXT.")
        else:
            print("Opción inválida.")
    except (ArchivoInvalidoError, OSError, ValueError) as error:
        print(f"No se pudo completar la operación: {error}")


def administrar_catalogo(dex):
    print("Catálogo: 1) Alta  2) Baja  3) Modificación")
    opcion = input("> ").strip()

    if opcion == "1":
        try:
            id_pokemon = int(input("Id: ").strip())
            nombre = input("Nombre: ").strip()
            tipo1 = input("Tipo principal: ").strip()
            tipo2 = input("Tipo secundario (vacío si no tiene): ").strip()
            numeros = []
            for campo in CAMPOS_NUMERICOS:
                numeros.append(_pedir_entero(campo.capitalize()))
            nuevo = Pokemon(id_pokemon, nombre, tipo1, tipo2, *numeros)
            _reemplazar_catalogo(dex, dex.pokemones + [nuevo])
            print("Pokémon agregado y guardado en el TXT.")
        except (ArchivoInvalidoError, OSError, ValueError) as error:
            print(f"No se pudo agregar: {error}")
        return

    if opcion == "2":
        try:
            id_pokemon = int(input("Id a eliminar: ").strip())
        except ValueError:
            print("El id debe ser un entero.")
            return

        if dex.buscar_por_id(id_pokemon) is None:
            print("No existe ese Pokémon.")
            return

        catalogo = []
        for pokemon in dex.pokemones:
            if pokemon.id != id_pokemon:
                catalogo.append(pokemon)

        try:
            _reemplazar_catalogo(dex, catalogo)
            print("Pokémon eliminado y cambio guardado en el TXT.")
        except (ArchivoInvalidoError, OSError, ValueError) as error:
            print(f"No se pudo guardar la baja: {error}")
        return

    if opcion == "3":
        try:
            id_pokemon = int(input("Id a modificar: ").strip())
        except ValueError:
            print("El id debe ser un entero.")
            return

        actual = dex.buscar_por_id(id_pokemon)
        if actual is None:
            print("No existe ese Pokémon.")
            return

        print("Dejá un campo vacío para conservarlo.")
        nombre = input(f"Nombre [{actual.nombre}]: ").strip() or actual.nombre
        tipo1 = input(f"Tipo principal [{actual.tipo1}]: ").strip() or actual.tipo1
        texto_tipo2 = input(
            f"Tipo secundario [{actual.tipo2}] (vacío conserva, - elimina): "
        ).strip()
        tipo2 = (
            actual.tipo2
            if texto_tipo2 == ""
            else "" if texto_tipo2 == "-" else texto_tipo2
        )

        try:
            numeros = []
            for campo in CAMPOS_NUMERICOS:
                numeros.append(_pedir_entero(campo.capitalize(), getattr(actual, campo)))

            actualizado = Pokemon(
                actual.id,
                nombre,
                tipo1,
                tipo2,
                *numeros,
            )
            catalogo = [
                actualizado if pokemon.id == id_pokemon else pokemon
                for pokemon in dex.pokemones
            ]
            _reemplazar_catalogo(dex, catalogo)
            print("Pokémon modificado y cambio guardado en el TXT.")
        except (ArchivoInvalidoError, OSError, ValueError) as error:
            print(f"No se pudo guardar la modificación: {error}")
        return

    print("Opción inválida.")


def operacion_recursiva(dex):
    texto = input("Id del Pokemon: ").strip()
    try:
        id_pokemon = int(texto)
    except ValueError:
        print("Tenes que ingresar un numero entero.")
        return
    cadenas = dex.cadenas_evolutivas(id_pokemon)
    if cadenas == []:
        print("No existe ese Pokemon.")
        return
    for cadena in cadenas:
        print(" -> ".join(cadena))


def mostrar_detalle(dex, pokemon):
    print(f"N.º {pokemon.id} — {pokemon.nombre}")
    print(f"  Tipo: {pokemon.tipos()}")
    print(f"  HP {pokemon.hp} | Ataque {pokemon.ataque} | Defensa {pokemon.defensa}"
          f" | Velocidad {pokemon.velocidad} | Generación {pokemon.generacion}")
    anterior = dex.anterior_de(pokemon.id)
    if anterior is None:
        print("  Viene de: -")
    else:
        print(f"  Viene de: {anterior.nombre}")
    siguientes = dex.siguientes_de(pokemon.id)
    if siguientes == []:
        print("  Evoluciona a: -")
    else:
        nombres = []
        for siguiente in siguientes:
            nombres.append(siguiente.nombre)
        print(f"  Evoluciona a: {', '.join(nombres)}")


def ver_detalle(dex):
    texto = input("Id o nombre del Pokemon: ").strip()
    if texto == "":
        print("No ingresaste nada.")
        return
    if texto.isdigit():
        pokemon = dex.buscar_por_id(int(texto))
    else:
        pokemon = dex.buscar_por_nombre(texto)
    if pokemon is None:
        print("No existe ese Pokemon.")
        return
    mostrar_detalle(dex, pokemon)


def buscar(dex):
    print("Buscar por: 1) Nombre (lineal)  2) Nombre (binaria)")
    tipo = input("> ").strip()
    if tipo != "1" and tipo != "2":
        print("Opción inválida.")
        return
    nombre = input("Ingresá el nombre: ").strip()
    if nombre == "":
        print("No ingresaste nada.")
        return
    if tipo == "1":
        pokemon = dex.buscar_por_nombre(nombre)
    else:
        if not dex.esta_ordenado_por("nombre"):
            dex.ordenar("nombre", ordenar_insercion)
            print("El catálogo no estaba ordenado por nombre: "
                  "lo ordené por nombre (inserción) para usar búsqueda binaria.")
        pokemon = dex.buscar_por_nombre_binaria(nombre)
    if pokemon is None:
        print(f"No se encontró ningún Pokemon llamado '{nombre}'.")
        return
    mostrar_detalle(dex, pokemon)


def ordenar(dex):
    print("Ordenar por: 1) Nombre  2) Número  3) Tipo principal")
    criterio = OPCIONES_CRITERIO.get(input("> ").strip())
    if criterio is None:
        print("Opción inválida.")
        return
    print("[1] Selección  [2] Inserción  [3] Shell")
    algoritmo = ALGORITMOS.get(input("> ").strip())
    if algoritmo is None:
        print("Opción inválida.")
        return
    nombre_algoritmo, funcion = algoritmo
    dex.ordenar(criterio, funcion)
    nombre_criterio, _ = CRITERIOS[criterio]
    print(f"Catálogo ordenado por {nombre_criterio} ({nombre_algoritmo}).")
    dex.listar()


def listar_equipo(equipo):
    print(f"Equipo ({equipo.tamanio()} de 6):")
    for pokemon in equipo:
        print(f"  {pokemon.nombre}")


def agregar_al_equipo(dex, equipo, historial, turnos):
    texto = input("Id del Pokemon: ").strip()
    try:
        id_pokemon = int(texto)
    except ValueError:
        print("Tenes que ingresar un numero entero.")
        return
    pokemon = dex.buscar_por_id(id_pokemon)
    if pokemon is None:
        print("No existe ese Pokemon.")
        return
    try:
        equipo.agregar(pokemon)
    except ColeccionLlenaError as error:
        print(error)
        return
    historial.apilar(pokemon)
    turnos.encolar(pokemon)
    print(f"{pokemon.nombre} se sumo al equipo.")
    listar_equipo(equipo)


def deshacer(equipo, historial):
    try:
        pokemon = historial.desapilar()
    except PilaVaciaError as error:
        print(error)
        return
    equipo.quitar(pokemon)
    print(f"Se deshizo el agregado de {pokemon.nombre}.")
    listar_equipo(equipo)


def siguiente_turno(turnos):
    try:
        pokemon = turnos.desencolar()
    except ColaVaciaError as error:
        print(error)
        return
    print(f"Pelea {pokemon.nombre}.")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    dex = Pokedex()
    try:
        RUTA_DATOS.mkdir(parents=True, exist_ok=True)
        if RUTA_CATALOGO.exists():
            dex.pokemones = _cargar_catalogo_texto()
        else:
            dex.pokemones = _filas_a_pokemones(cargar_texto(RUTA_POKEDEX))
            _guardar_catalogo(dex.pokemones)
        dex.evoluciones = _cargar_evoluciones()
    except (ArchivoInvalidoError, OSError, ValueError) as error:
        print(f"No se pudo iniciar el catálogo: {error}")
        return

    equipo = Equipo()
    historial = Pila()
    turnos = Cola()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            dex.listar()
        elif opcion == "2":
            ver_detalle(dex)
        elif opcion == "3":
            buscar(dex)
        elif opcion == "4":
            ordenar(dex)
        elif opcion == "5":
            operacion_recursiva(dex)
        elif opcion == "6":
            agregar_al_equipo(dex, equipo, historial, turnos)
        elif opcion == "7":
            deshacer(equipo, historial)
        elif opcion == "8":
            siguiente_turno(turnos)
        elif opcion == "9":
            manejar_archivos(dex)
        elif opcion == "10":
            administrar_catalogo(dex)
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
