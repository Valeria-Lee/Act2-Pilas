from nodo import Nodo

class ListaDoblementeEnlazada():
    __primerNodo:Nodo = None
    __ultimoNodo:Nodo = None
    __longitud:int = 0

    def __init__(self, __primerNodo:Nodo=None, __ultimoNodo:Nodo=None, __longitud:int=0):
        if __primerNodo != None or __ultimoNodo != None or __longitud != 0:
            self.__primerNodo = __primerNodo
            self.__ultimoNodo = __ultimoNodo
            self.__longitud = __longitud
        else:
            self.__primerNodo = None
            self.__ultimoNodo = None
            self.__longitud = 0

    def insertar(self, dato:int):
        nuevoNodo:Nodo = Nodo(dato)
        if self.__primerNodo == None:
            self.__primerNodo = nuevoNodo
            self.__ultimoNodo = nuevoNodo
        else:
            nuevoNodo.setAnterior(self.__ultimoNodo)
            self.__ultimoNodo.setSiguiente(nuevoNodo)
            self.__ultimoNodo = nuevoNodo
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
            raise Exception("Indice fuera de rango")
        
        nodoEliminar:Nodo

        if (indice == 0):
            nodoEliminar = self.__primerNodo
            self.__primerNodo = self.__primerNodo.getSiguiente()
        elif (indice == self.__longitud - 1):
            nodoEliminar = self.__ultimoNodo
            self.__ultimoNodo = self.__ultimoNodo.getAnterior()
            self.__ultimoNodo.setSiguiente(None)
        else:
            nodoActual:Nodo
            if (indice < self.__longitud // 2):
                nodoActual = self.__primerNodo
                for i in range(indice):
                    nodoActual = nodoActual.getSiguiente()
            else:
                nodoActual = self.__ultimoNodo
                for i in range(self.__longitud - 1, indice, -1):
                    nodoActual = nodoActual.getAnterior()
            nodoEliminar = nodoActual
            nodoActual.getAnterior().setSiguiente(nodoActual.getSiguiente())
            nodoActual.getSiguiente().setAnterior(nodoActual.getAnterior())
        nodoEliminar.setAnterior(None)
        nodoEliminar.setSiguiente(None)
        self.__longitud -= 1

    def getLongitud(self):
        return self.__longitud