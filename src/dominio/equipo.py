from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError


class Equipo:
    """Equipo de combate. Usa ListaEnlazada y tiene un tope de 6 Pokemon."""

    TOPE = 6

    def __init__(self):
        self._lista = ListaEnlazada()

    def agregar(self, pokemon):
        if self._lista.tamanio() == Equipo.TOPE:
            raise ColeccionLlenaError("El equipo ya tiene 6 Pokemon.")
        self._lista.insertar_al_final(pokemon)

    def quitar(self, pokemon):
        self._lista.eliminar(pokemon)

    def tamanio(self):
        return self._lista.tamanio()

    def __iter__(self):
        return iter(self._lista)
