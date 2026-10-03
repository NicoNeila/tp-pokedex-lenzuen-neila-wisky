from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError


class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("La pila esta vacia.")
        for dato in self._lista:
            self._lista.eliminar(dato)
            return dato

    def ver_tope(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("La pila esta vacia.")
        dato = self.desapilar()
        self.apilar(dato)
        return dato

    def esta_vacia(self):
        return self._lista.esta_vacia()
