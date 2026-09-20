CATALOGO = [
    {"id": 1, "nombre": "Bulbasaur", "tipo1": "Planta", "tipo2": "Veneno", "evolucion": 2},
    {"id": 2, "nombre": "Ivysaur", "tipo1": "Planta", "tipo2": "Veneno", "evolucion": 3},
    {"id": 3, "nombre": "Venusaur", "tipo1": "Planta", "tipo2": "Veneno", "evolucion": None},
    {"id": 4, "nombre": "Charmander", "tipo1": "Fuego", "tipo2": "", "evolucion": 5},
    {"id": 5, "nombre": "Charmeleon", "tipo1": "Fuego", "tipo2": "", "evolucion": 6},
    {"id": 6, "nombre": "Charizard", "tipo1": "Fuego", "tipo2": "Volador", "evolucion": None},
    {"id": 7, "nombre": "Squirtle", "tipo1": "Agua", "tipo2": "", "evolucion": 8},
    {"id": 8, "nombre": "Wartortle", "tipo1": "Agua", "tipo2": "", "evolucion": 9},
    {"id": 9, "nombre": "Blastoise", "tipo1": "Agua", "tipo2": "", "evolucion": None},
]


def listar_catalogo():
    for item in CATALOGO:
        print(f"{item['id']:>3}  {item['nombre']}")

def (id_pokemon) :
    for item in CATALOGO:
        if item ['id'] == id_pokemon:
            return item
    return None

#recursiva hasta encontrar el pokemon que arranca la cadena evolutiva
def buscar_pokemon_base(id_pokemon):
    for item in CATALOGO:
        if item["evolucion"] == id_pokemon:
            return buscar_pokemon_base(item["id"])
    return buscar_por_id(id_pokemon)

def listar_cadena_evolutiva (id_pokemon):
    # Primero valido que el pokemon existe
    actual = buscar_por_id(id_pokemon)
    if actual is None: 
        return []

    actual = buscar_pokemon_base(id_pokemon)
    cadenaEvolutiva = []
    while actual is not None:
        cadenaEvolutiva.append(actual["nombre"])
        actual = buscar_por_id(actual["evolucion"])    
    return cadenaEvolutiva

