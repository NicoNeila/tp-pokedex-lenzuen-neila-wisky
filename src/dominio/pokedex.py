from src.dominio.pokemon import Pokemon


class Pokedex:
    """Catalogo de Pokemon."""

    def __init__(self):
        self.pokemones = []

    def agregar(self, pokemon):
        self.pokemones.append(pokemon)

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
