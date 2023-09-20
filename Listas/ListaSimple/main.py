from ListaSimplementeEnlazada import ListaSimplementeEnlazada

'''
Inserta en la lista los valores 5, 59, 91, -17, 73, 34, 40
b. Elimina los índices 2 y 3
c. Imprime solamente el índice 3
'''

def main():
    LSE = ListaSimplementeEnlazada()
    LSE.insertar(5)
    LSE.insertar(59)
    LSE.insertar(91)
    LSE.insertar(-17)
    LSE.insertar(73)
    LSE.insertar(34)
    LSE.insertar(40)
    LSE.eliminar(2)
    LSE.eliminar(3)
    print(LSE.obtener(3))

main()