from ListaDoblementeEnlazada import ListaDoblementeEnlazada

def main():
    LDE = ListaDoblementeEnlazada()

    LDE.insertar(5)
    LDE.insertar(59)
    LDE.insertar(91)
    LDE.insertar(-17)
    LDE.insertar(73)
    LDE.insertar(34)
    LDE.insertar(40)
    LDE.eliminar(2)
    LDE.eliminar(3)
    print(LDE.obtener(3))

main()