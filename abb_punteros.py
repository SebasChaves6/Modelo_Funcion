class Nodo:
    def __init__(self, llave, valor):
        # nodo del arbol
        self.llave = llave
        self.valor = valor
        self.izq = None
        self.der = None


class ModeloFuncionABBPunteros:
    def __init__(self):
        # init: arbol vacio
        self.raiz = None
        self.tamanio = 0

    def clear(self):
        # clear: vacia todo
        self.raiz = None
        self.tamanio = 0

    def done(self):
        # done: libera memoria
        self.clear()

    def assign(self, llave, valor):
        # assign: inserta o actualiza
        self.raiz = self._insertar(self.raiz, llave, valor)

    def _insertar(self, nodo, llave, valor):
        if nodo is None:
            self.tamanio += 1
            return Nodo(llave, valor)

        # bajar por el arbol
        if llave < nodo.llave:
            nodo.izq = self._insertar(nodo.izq, llave, valor)

        elif llave > nodo.llave:
            nodo.der = self._insertar(nodo.der, llave, valor)

        else:
            # actualizar si existe
            nodo.valor = valor

        return nodo

    def unassign(self, llave):
        # unassign: elimina por llave
        self.raiz, eliminado = self._eliminar(self.raiz, llave)

        if eliminado:
            self.tamanio -= 1

    def _eliminar(self, nodo, llave):
        if nodo is None:
            return None, False

        if llave < nodo.llave:
            nodo.izq, eliminado = self._eliminar(nodo.izq, llave)
            return nodo, eliminado

        elif llave > nodo.llave:
            nodo.der, eliminado = self._eliminar(nodo.der, llave)
            return nodo, eliminado

        else:
            # encontrado

            # sin hijo izquierdo
            if nodo.izq is None:
                return nodo.der, True

            # sin hijo derecho
            elif nodo.der is None:
                return nodo.izq, True

            # tiene dos hijos
            sucesor = self._minimo(nodo.der)

            nodo.llave = sucesor.llave
            nodo.valor = sucesor.valor

            nodo.der, _ = self._eliminar(nodo.der, sucesor.llave)

            return nodo, True

    def _minimo(self, nodo):
        # buscar menor
        aux = nodo

        while aux.izq is not None:
            aux = aux.izq

        return aux

    def lookup(self, llave):
        # lookup: retorna valor o none
        nodo = self._buscar(self.raiz, llave)

        if nodo is None:
            return None

        return nodo.valor

    def _buscar(self, nodo, llave):
        if nodo is None:
            return None

        if llave == nodo.llave:
            return nodo

        elif llave < nodo.llave:
            return self._buscar(nodo.izq, llave)

        else:
            return self._buscar(nodo.der, llave)

    def keys(self):
        # keys: retorna llaves ordenadas
        res = []
        self._inorden_llaves(self.raiz, res)
        return res

    def _inorden_llaves(self, nodo, res):
        if nodo is None:
            return

        self._inorden_llaves(nodo.izq, res)
        res.append(nodo.llave)
        self._inorden_llaves(nodo.der, res)

    def print(self):
        # print: muestra contenido
        res = []
        self._inorden_res(self.raiz, res)

        for llave, valor in res:
            print("Llave:", llave, "| Valor:", valor)

        if not res:
            print("Arreglo vacio")

    def _inorden_res(self, nodo, res):
        if nodo is None:
            return

        self._inorden_res(nodo.izq, res)
        res.append((nodo.llave, nodo.valor))
        self._inorden_res(nodo.der, res)