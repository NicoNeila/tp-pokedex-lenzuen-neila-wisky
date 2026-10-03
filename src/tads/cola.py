from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError


class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("La cola esta vacia.")
        for dato in self._lista:
            self._lista.eliminar(dato)
            return dato

    def ver_frente(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("La cola esta vacia.")
        for dato in self._lista:
            return dato

    def esta_vacia(self):
        return self._lista.esta_vacia()
