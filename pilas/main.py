from pila import Pila

pila = Pila.create(Pila)

pila.insertar(14)
pila.insertar(27)
pila.insertar(1)
pila.insertar(15)
pila.insertar(10)
pila.insertar(90)
pila.insertar(71)
pila.insertar(37)
pila.insertar(2)
pila.insertar(48)

print(pila.getTamanio())

pila.quitar()
pila.quitar()
pila.quitar()
pila.quitar()

print(pila.getTamanio())

print(pila.obtenerCima())

pila.vaciar()

print(pila.estaVacia())