from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria


def clave_nombre(pokemon):
    return pokemon.nombre.lower()


def clave_numero(pokemon):
    return pokemon.id


def clave_tipo(pokemon):
    return pokemon.tipo1.lower()


CRITERIOS = {
    "nombre": ("nombre", clave_nombre),
    "numero": ("número", clave_numero),
    "tipo": ("tipo principal", clave_tipo),
}


class Pokedex:

    def __init__(self):
        self.pokemones = []
        self.evoluciones = []
        self.orden = None

    def agregar(self, pokemon):
        self.pokemones.append(pokemon)
        self.orden = None

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
        for origen, destino in self.evoluciones:
            if destino == id_pokemon:
                return self.buscar_por_id(origen)
        return None

    def siguientes_de(self, id_pokemon):
        siguientes = []
        for origen, destino in self.evoluciones:
            if origen == id_pokemon:
                pokemon = self.buscar_por_id(destino)
                if pokemon is not None:
                    siguientes.append(pokemon)
        return siguientes

    def buscar_base(self, id_pokemon):
        anterior = self.anterior_de(id_pokemon)
        if anterior is None:
            return self.buscar_por_id(id_pokemon)
        return self.buscar_base(anterior.id)

    def cadenas_desde(self, id_pokemon):
        actual = self.buscar_por_id(id_pokemon)
        siguientes = self.siguientes_de(id_pokemon)
        if siguientes == []:
            return [[actual.nombre]]
        cadenas = []
        for siguiente in siguientes:
            for cadena in self.cadenas_desde(siguiente.id):
                cadenas.append([actual.nombre] + cadena)
        return cadenas

    def cadenas_evolutivas(self, id_pokemon):
        if self.buscar_por_id(id_pokemon) is None:
            return []
        base = self.buscar_base(id_pokemon)
        return self.cadenas_desde(base.id)

    def ordenar(self, criterio, algoritmo):
        _, clave = CRITERIOS[criterio]
        self.pokemones = algoritmo(self.pokemones, clave)
        self.orden = criterio

    def esta_ordenado_por(self, criterio):
        return self.orden == criterio

    def buscar_por_nombre(self, nombre):
        return busqueda_lineal(self.pokemones, nombre.strip().lower(), clave_nombre)

    def buscar_por_nombre_binaria(self, nombre):
        return busqueda_binaria(self.pokemones, nombre.strip().lower(), clave_nombre)
