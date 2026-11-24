class Pokemon:

    def __init__(self, id_pokemon, nombre, tipo1, tipo2,
                 hp, ataque, defensa, velocidad, generacion):
        self.id = id_pokemon
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def tipos(self):
        if self.tipo2 == "":
            return self.tipo1
        return self.tipo1 + "/" + self.tipo2

    def __str__(self):
        return f"{self.id:>3}  {self.nombre} ({self.tipos()})"
