from src.config import TEMA
from src.dominio.pokedex import Pokedex
from src.dominio.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


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
    print("0. Salir")


def operacion_recursiva(dex):
    texto = input("Id del Pokemon: ").strip()
    try:
        id_pokemon = int(texto)
    except ValueError:
        print("Tenes que ingresar un numero entero.")
        return
    cadena = dex.cadena_evolutiva(id_pokemon)
    if cadena == []:
        print("No existe ese Pokemon.")
        return
    print(" -> ".join(cadena))


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
    dex.cargar_datos_iniciales()
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
        elif opcion == "5":
            operacion_recursiva(dex)
        elif opcion == "6":
            agregar_al_equipo(dex, equipo, historial, turnos)
        elif opcion == "7":
            deshacer(equipo, historial)
        elif opcion == "8":
            siguiente_turno(turnos)
        elif opcion in {"2", "3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
