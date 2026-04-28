from arreglos import lista_arreglos
from punteros import lista_punteros


def escoger_estructura():
    print("=== ESCOJA ESTRUCTURA ===")
    print("1. Lista ordenada por arreglos")
    print("2. Lista ordenada por punteros")

    opcion = input("Opción: ")

    if opcion == "1":
        return lista_arreglos()
    elif opcion == "2":
        return lista_punteros()
    else:
        print("Opción inválida. Se usará lista por arreglos.")
        return lista_arreglos()


def menu(funcion):
    while True:
        print("\n=== MENÚ FUNCIÓN ===")
        print("1. Asignar relación")
        print("2. Eliminar relación")
        print("3. Buscar llave")
        print("4. Imprimir")
        print("5. Mostrar llaves")
        print("6. Limpiar")
        print("7. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            llave = input("Llave: ")
            valor = input("Valor: ")
            funcion.asign(llave, valor)

        elif opcion == "2":
            llave = input("Llave a eliminar: ")
            funcion.eliminar(llave)

        elif opcion == "3":
            llave = input("Llave a buscar: ")
            valor = funcion.obtener(llave)
            if valor is None:
                print("La llave no existe.")
            else:
                print("Valor:", valor)

        elif opcion == "4":
            funcion.print()

        elif opcion == "5":
            print(funcion.llaves())

        elif opcion == "6":
            funcion.clear()
            print("Estructura limpiada.")

        elif opcion == "7":
            funcion.done()
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    funcion = escoger_estructura()
    menu(funcion)