class Nodo:
    __dato:int = None
    __siguiente = None

    def __init__(self, dato:int, siguiente=None):
        self.__dato = dato
        self.__siguiente = siguiente

    def getDato(self):
        return self.__dato
    
    def setDato(self, d:int):
        self.__dato = d

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, s):
        self.__siguiente = s