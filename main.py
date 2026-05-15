# Importar todas las estructuras de datos del proyecto
from lista_arreglos import lista_arreglos
from lista_punteros import lista_punteros
from tabla_hash import tabla_hash
from trie_punteros import trie_punteros
from trie_arreglos import trie_arreglos
from abb_punteros import ModeloFuncionABBPunteros
from abb_heap import ModeloFuncionABBHeap


def escoger_estructura():
    """
    Esta función le muestra al usuario las estructuras disponibles
    y devuelve la estructura escogida.
    """

    print("=== ESCOJA ESTRUCTURA ===")
    print("1. Lista ordenada por arreglos")
    print("2. Lista ordenada por punteros")
    print("3. Tabla hash abierta")
    print("4. Trie por punteros")
    print("5. Trie por arreglos")
    print("6. ABB por punteros")
    print("7. ABB por arreglos (Vector Heap)")

    # Leer la opción del usuario
    opcion = input("Opción: ")

    # Dependiendo de la opción se crea un objeto diferente
    if opcion == "1":
        return lista_arreglos()

    elif opcion == "2":
        return lista_punteros()

    elif opcion == "3":
        return tabla_hash()

    elif opcion == "4":
        return trie_punteros()

    elif opcion == "5":
        return trie_arreglos()
        
    elif opcion == "6":
        return ModeloFuncionABBPunteros()
        
    elif opcion == "7":
        return ModeloFuncionABBHeap()

    else:
        # Si el usuario escribe algo incorrecto
        print("Opción inválida. Se usará lista por arreglos.")
        return lista_arreglos()


def menu(funcion):
    """
    Menú principal del programa.
    Recibe la estructura seleccionada y permite realizar operaciones.
    """

    # Ciclo infinito hasta que el usuario escoja salir
    while True:

        print("\n=== MENÚ FUNCIÓN ===")
        print("1. Asignar relación (Assign)")
        print("2. Eliminar relación (Unassign)")
        print("3. Buscar llave (Lookup)")
        print("4. Imprimir (Print)")
        print("5. Mostrar llaves (Keys)")
        print("6. Limpiar (Clear)")
        print("7. Salir (Done)")

        # Leer opción del usuario
        opcion = input("Opción: ")

        #INSERTAR O ACTUALIZAR
        if opcion == "1":

            # Pedir llave y valor
            llave = input("Llave: ")
            valor = input("Valor: ")

            # Insertar o actualizar en la estructura
            funcion.assign(llave, valor)

        #ELIMINAR
        elif opcion == "2":

            # Pedir llave a eliminar
            llave = input("Llave a eliminar: ")

            # Eliminar la llave
            funcion.unassign(llave)

        #BUSCAR
        elif opcion == "3":

            # Pedir llave
            llave = input("Llave a buscar: ")

            # Buscar valor asociado
            valor = funcion.lookup(llave)

            # Verificar si existe
            if valor is None:
                print("La llave no existe.")
            else:
                print("Valor:", valor)

        #IMPRIMIR TODO
        elif opcion == "4":

            # Mostrar todas las relaciones
            funcion.print()

        #MOSTRAR LLAVES
        elif opcion == "5":

            # Imprimir lista de llaves
            print(funcion.keys())

        #LIMPIAR ESTRUCTURA
        elif opcion == "6":

            # Vaciar completamente la estructura
            funcion.clear()

            print("Estructura limpiada.")

        # SALIR
        elif opcion == "7":

            # Liberar memoria
            funcion.done()

            print("Saliendo...")

            # Salir del ciclo
            break

        #OPCIÓN INVÁLIDA
        else:
            print("Opción inválida.")


# Punto de inicio del programa
if __name__ == "__main__":
    
    # Escoger la estructura de datos
    funcion = escoger_estructura()

    # Ejecutar el menú principal
    menu(funcion)
