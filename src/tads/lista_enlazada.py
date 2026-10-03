from src.tads.nodo import Nodo
from src.excepciones import ItemNoEncontradoError


class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
        self._cabeza = None
        self._cantidad = 0

    def esta_vacia(self):
        return self._cabeza is None

    def tamanio(self):
        return self._cantidad

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        self._cantidad = self._cantidad + 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._cantidad = self._cantidad + 1

    def eliminar(self, dato):
        if self._cabeza is None:
            raise ItemNoEncontradoError("La lista esta vacia.")
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self._cantidad = self._cantidad - 1
            return
        anterior = self._cabeza
        actual = self._cabeza.siguiente
        while actual is not None and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            raise ItemNoEncontradoError("El dato no esta en la lista.")
        anterior.siguiente = actual.siguiente
        self._cantidad = self._cantidad - 1

    def buscar(self, dato):
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
        return None

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
