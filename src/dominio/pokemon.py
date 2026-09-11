CATALOGO = [
    {"id": 1, "nombre": "Bulbasaur", "tipo1": "Planta", "tipo2": "Veneno"},
    {"id": 2, "nombre": "Ivysaur", "tipo1": "Planta", "tipo2": "Veneno"},
    {"id": 3, "nombre": "Venusaur", "tipo1": "Planta", "tipo2": "Veneno"},
    {"id": 4, "nombre": "Charmander", "tipo1": "Fuego", "tipo2": ""},
    {"id": 5, "nombre": "Charmeleon", "tipo1": "Fuego", "tipo2": ""},
    {"id": 6, "nombre": "Charizard", "tipo1": "Fuego", "tipo2": "Volador"},
    {"id": 7, "nombre": "Squirtle", "tipo1": "Agua", "tipo2": ""},
    {"id": 8, "nombre": "Wartortle", "tipo1": "Agua", "tipo2": ""},
    {"id": 9, "nombre": "Blastoise", "tipo1": "Agua", "tipo2": ""},
]


def listar_catalogo():
    for item in CATALOGO:
        print(f"{item['id']:>3}  {item['nombre']}")
