class Nodo:
    """
    Guarda llave, valor y referencia al siguiente
    """
    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor
        self.siguiente = None


class lista_punteros:
    """
    Lista enlazada ordenada por llave
    """
    def __init__(self):
        # Init: lista vacia
        self.cabeza = None

    def clear(self):
        """
        Clear: vacia la lista
        """
        self.cabeza = None

    def done(self):
        """
        Done: libera memoria
        """
        self.clear()

    def assign(self, llave, valor):
        """
        Assign: inserta o actualiza
        """
        nuevo = Nodo(llave, valor)

        # insertar al inicio
        if self.cabeza is None or self.cabeza.llave > llave:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        # actualizar cabeza
        if self.cabeza.llave == llave:
            self.cabeza.valor = valor
            return

        # buscar posicion
        aux = self.cabeza
        while aux.siguiente and aux.siguiente.llave < llave:
            aux = aux.siguiente

        # actualizar si existe
        if aux.siguiente and aux.siguiente.llave == llave:
            aux.siguiente.valor = valor
            return

        # insertar
        nuevo.siguiente = aux.siguiente
        aux.siguiente = nuevo

    def eliminar(self, llave):
        """
        elimina por llave
        """
        if self.cabeza is None:
            return

        # eliminar cabeza
        if self.cabeza.llave == llave:
            self.cabeza = self.cabeza.siguiente
            return

        # buscar anterior
        aux = self.cabeza
        while aux.siguiente and aux.siguiente.llave != llave:
            aux = aux.siguiente

        # eliminar si existe
        if aux.siguiente:
            aux.siguiente = aux.siguiente.siguiente

    def obtener(self, llave):
        """
        retorna valor o None
        """
        aux = self.cabeza

        while aux:
            if aux.llave == llave:
                return aux.valor

            # ya se paso
            if aux.llave > llave:
                return None

            aux = aux.siguiente

        return None

    def llaves(self):
        """
        retorna lista de llaves
        """
        res = []
        aux = self.cabeza

        while aux:
            res.append(aux.llave)
            aux = aux.siguiente

        return res

    def print(self):
        """
        Print: muestra contenido
        """
        aux = self.cabeza
        while aux:
            print("Llave:", aux.llave, "| Valor:", aux.valor)
            aux = aux.siguiente

    def limpiar(self):
        self.clear()

    def asigne(self, llave, valor):
        self.assign(llave, valor)

    def elimine(self, llave):
        self.eliminar(llave)

    def lookup(self, llave):
        return self.obtener(llave)

    def imprimir(self):
        self.print()