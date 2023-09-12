from nodo import Nodo

class Pila():

    def __init__(self, cima:Nodo=None, tamanio:int=None):
        self.__cima = cima
        self.__tamanio = tamanio

    def create(self):
        self = Pila(None, 0)
        return self
    
    def insertar(self, dato:int):
        nuevo_nodo = Nodo(dato, self.__cima)
        self.__cima = nuevo_nodo
        self.__tamanio += 1

    def quitar(self):
        if not self.estaVacia():
            self.__cima = self.__cima.getNodo()
            self.__tamanio -= 1

    def estaVacia(self):
        return self.__cima is None

    def vaciar(self):
        self.__tamanio = 0
        self.__cima = None

    def obtenerCima(self):
        if not self.estaVacia():
            return self.__cima.getDato()
        else:
            return None

    def getTamanio(self):
        return self.__tamanio