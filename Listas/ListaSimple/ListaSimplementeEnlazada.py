from nodo import Nodo

class ListaSimplementeEnlazada():
    __nodoAnterior:Nodo = None
    __nodoEliminar:Nodo = None

    def __init__(self, __frente:Nodo=None, __longitud:None=0):
        if __frente != None and __longitud != 0:
            self.__frente = __frente
            self.__longitud = __longitud
        else:
            self.__frente = None
            self.__longitud = 0

    def insertar(self, dato:int):
        nuevoNodo = Nodo(dato)
        if self.__frente == None:
            self.__frente = nuevoNodo
            self.__atras = nuevoNodo
            self.__atras.setSiguiente(self.__frente)
        else:
            self.__atras.setSiguiente(nuevoNodo)
            self.__atras = nuevoNodo
            self.__atras.setSiguiente
        self.__longitud += 1

    def obtener(self, indice:int):
        if (indice < 0 or indice >= self.__longitud):
            print("Indice fuera de rango")
            return
        elif (indice == 0):
            return self.__frente.getDato()
        else:
            nodoActual:Nodo = self.__frente
            for i in range(indice):
                nodoActual = nodoActual.getSiguiente()
            return nodoActual.getDato()

    def eliminar(self, indice:int):
        if (indice < 0 or indice >= self.__longitud):
            print("Indice fuera de rango")
            return
        if (indice == 0):
            self.__frente = self.__frente.getSiguiente()
        else:
            self.__nodoAnterior:Nodo = self.__frente
            for i in range(indice - 1):
               self.__nodoAnterior = self.__nodoAnterior.getSiguiente()
            self.__nodoEliminar:Nodo = self.__nodoAnterior.getSiguiente()
            self.__nodoAnterior.setSiguiente(self.__nodoEliminar.getSiguiente())
        self.__longitud -= 1

    def getLongitud(self):
        return self.__longitud