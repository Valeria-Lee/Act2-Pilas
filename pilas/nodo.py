class Nodo:
    __dato:int = None
    __nodo = None

    def __init__(self, dato:int, nodo):
        self.__dato = dato
        self.__nodo = nodo

    def getDato(self):
        return self.__dato
    
    def setDato(self, d:int):
        self.__dato = d
    
    def getNodo(self):
        return self.__nodo
    
    def setNodo(self, n):
        self.__nodo = n