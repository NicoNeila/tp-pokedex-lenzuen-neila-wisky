from src.config import TEMA
from src.dominio.pokedex import Pokedex, CRITERIOS
from src.dominio.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion, ordenar_shell

# opción del submenú -> criterio de CRITERIOS
OPCIONES_CRITERIO = {"1": "nombre", "2": "numero", "3": "tipo"}

# opción del submenú -> (texto, función de ordenamiento)
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


def mostrar_detalle(dex, pokemon):
    print(f"N.º {pokemon.id} — {pokemon.nombre}")
    print(f"  Tipo: {pokemon.tipos()}")
    if pokemon.evolucion is None:
        print("  Evoluciona a: -")
    else:
        siguiente = dex.buscar_por_id(pokemon.evolucion)
        print(f"  Evoluciona a: {siguiente.nombre}")


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
        # la binaria solo sirve si está ordenado por nombre: si no, ordena y avisa
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
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
