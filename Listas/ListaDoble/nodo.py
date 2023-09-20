class Nodo:
    __dato:int = None
    __siguiente = None
    __anterior = None

    def __init__(self, dato:int, siguiente=None, anterior=None):
        self.__dato = dato
        self.__siguiente = siguiente
        self.__anterior = anterior

    def getDato(self):
        return self.__dato
    
    def setDato(self, d:int):
        self.__dato = d

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, s):
        self.__siguiente = s

    def getAnterior(self):
        return self.__anterior
    
    def setAnterior(self, a):
        self.__anterior = a