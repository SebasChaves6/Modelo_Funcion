from lista_arreglos import lista_arreglos
from lista_punteros import lista_punteros

if __name__ == "__main__":
    print("=== PRUEBA ARREGLOS ===")
    arr = lista_arreglos()

    arr.assign("c", "tres")
    arr.assign("a", "uno")
    arr.assign("b", "dos")
    arr.assign("b", "veinte")

    arr.print()

    print("lookup b:", arr.lookup("b"))
    print("lookup x:", arr.lookup("x"))

    arr.unassign("a")
    arr.print()

    print("keys:", arr.keys())

    arr.clear()
    arr.print()


    print("\n=== PRUEBA PUNTEROS ===")
    lista = lista_punteros()

    lista.assign("c", "tres")
    lista.assign("a", "uno")
    lista.assign("b", "dos")
    lista.assign("b", "veinte") 

    lista.print()

    print("lookup b:", lista.lookup("b"))
    print("lookup x:", lista.lookup("x"))

    lista.unassign("a")
    lista.print()

    print("keys:", lista.keys())

    lista.clear()
    lista.print()