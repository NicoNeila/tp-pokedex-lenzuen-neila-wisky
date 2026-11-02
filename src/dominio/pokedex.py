from src.dominio.pokemon import Pokemon
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria


def clave_nombre(pokemon):
    return pokemon.nombre.lower()


def clave_numero(pokemon):
    return pokemon.id


def clave_tipo(pokemon):
    return pokemon.tipo1.lower()


# criterio -> (texto para mostrar, función que da la clave)
CRITERIOS = {
    "nombre": ("nombre", clave_nombre),
    "numero": ("número", clave_numero),
    "tipo": ("tipo principal", clave_tipo),
}


class Pokedex:
    """Catalogo de Pokemon."""

    def __init__(self):
        self.pokemones = []
        self.orden = None   # criterio por el que está ordenado, o None

    def agregar(self, pokemon):
        self.pokemones.append(pokemon)
        self.orden = None   # agregar al final puede romper el orden

    def cargar_datos_iniciales(self):
        self.agregar(Pokemon(1, "Bulbasaur", "Planta", "Veneno", 2))
        self.agregar(Pokemon(2, "Ivysaur", "Planta", "Veneno", 3))
        self.agregar(Pokemon(3, "Venusaur", "Planta", "Veneno", None))
        self.agregar(Pokemon(4, "Charmander", "Fuego", "", 5))
        self.agregar(Pokemon(5, "Charmeleon", "Fuego", "", 6))
        self.agregar(Pokemon(6, "Charizard", "Fuego", "Volador", None))
        self.agregar(Pokemon(7, "Squirtle", "Agua", "", 8))
        self.agregar(Pokemon(8, "Wartortle", "Agua", "", 9))
        self.agregar(Pokemon(9, "Blastoise", "Agua", "", None))
        self.agregar(Pokemon(254, "Sceptile", "Planta", "", None))
        self.agregar(Pokemon(282, "Gardevoir", "Hada", "Psiquico", None))
        self.agregar(Pokemon(362, "Walrein", "Hielo", "Agua", None))
        self.agregar(Pokemon(464, "Rhyperior", "Roca", "Tierra", None))
        self.agregar(Pokemon(862, "Obstagoon", "Siniestro", "Normal", None))

    def listar(self):
        for pokemon in self.pokemones:
            print(pokemon)
        print(f"Total: {len(self.pokemones)} Pokemon")

    def buscar_por_id(self, id_pokemon):
        for pokemon in self.pokemones:
            if pokemon.id == id_pokemon:
                return pokemon
        return None

    def anterior_de(self, id_pokemon):
        for pokemon in self.pokemones:
            if pokemon.evolucion == id_pokemon:
                return pokemon
        return None

    def buscar_base(self, id_pokemon):
        anterior = self.anterior_de(id_pokemon)
        if anterior is None:
            return self.buscar_por_id(id_pokemon)
        return self.buscar_base(anterior.id)

    def cadena_desde(self, id_pokemon):
        actual = self.buscar_por_id(id_pokemon)
        if actual is None:
            return []
        if actual.evolucion is None:
            return [actual.nombre]
        return [actual.nombre] + self.cadena_desde(actual.evolucion)

    def cadena_evolutiva(self, id_pokemon):
        if self.buscar_por_id(id_pokemon) is None:
            return []
        base = self.buscar_base(id_pokemon)
        return self.cadena_desde(base.id)

    def ordenar(self, criterio, algoritmo):
        """Ordena el catálogo con uno de los algoritmos de src/algoritmos."""
        _, clave = CRITERIOS[criterio]
        self.pokemones = algoritmo(self.pokemones, clave)
        self.orden = criterio

    def esta_ordenado_por(self, criterio):
        return self.orden == criterio

    def buscar_por_nombre(self, nombre):
        """Búsqueda lineal por nombre, sin importar mayúsculas."""
        return busqueda_lineal(self.pokemones, nombre.strip().lower(), clave_nombre)

    def buscar_por_nombre_binaria(self, nombre):
        """Búsqueda binaria por nombre. Requiere estar ordenado por nombre."""
        return busqueda_binaria(self.pokemones, nombre.strip().lower(), clave_nombre)
