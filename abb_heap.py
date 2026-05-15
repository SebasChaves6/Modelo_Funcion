class ModeloFuncionABBHeap:
    def __init__(self, capacidad_inicial=16):
        # init: arreglo vacio
        self.vec = [None] * capacidad_inicial
        self.tamanio = 0

    def done(self):
        # done: libera memoria
        self.vec = []
        self.tamanio = 0

    def clear(self):
        # clear: limpia todo
        self.vec = [None] * 16
        self.tamanio = 0

    def expandir(self, indice):
        # agranda el arreglo si hace falta
        while indice >= len(self.vec):
            self.vec.extend([None] * len(self.vec))

    def _hijo_izq(self, i):
        return 2 * i

    def _hijo_der(self, i):
        return 2 * i + 1

    def assign(self, llave, valor):
        # assign: inserta o actualiza
        self.expandir(1)

        i = 1

        while True:
            if self.vec[i] is None:
                self.vec[i] = (llave, valor)
                self.tamanio += 1
                return

            llave_actual, _ = self.vec[i]

            if llave == llave_actual:
                # actualizar
                self.vec[i] = (llave, valor)
                return

            elif llave < llave_actual:
                i = self._hijo_izq(i)

            else:
                i = self._hijo_der(i)

            self.expandir(i)

    def unassign(self, llave):
        # unassign: elimina por llave
        i = 1

        while i < len(self.vec) and self.vec[i] is not None:
            llave_actual, _ = self.vec[i]

            if llave == llave_actual:
                self._borrar_nodo(i)
                self.tamanio -= 1
                return

            elif llave < llave_actual:
                i = self._hijo_izq(i)

            else:
                i = self._hijo_der(i)

    def _borrar_nodo(self, i):
        iz = self._hijo_izq(i)
        dr = self._hijo_der(i)

        self.expandir(max(iz, dr))

        tiene_iz = self.vec[iz] is not None
        tiene_dr = self.vec[dr] is not None

        if not tiene_iz and not tiene_dr:
            self.vec[i] = None
        elif not tiene_iz:
            self._mover_subarbol(dr, i)
        elif not tiene_dr:
            self._mover_subarbol(iz, i)

        # dos hijos
        else:
            pos_sucesor = self._pos_minimo(dr)
            llave_suc, valor_suc = self.vec[pos_sucesor]
            self.vec[i] = (llave_suc, valor_suc)
            self._borrar_nodo(pos_sucesor)

    def _pos_minimo(self, i):
        self.expandir(i)

        while True:
            iz = self._hijo_izq(i)
            self.expandir(iz)

            if self.vec[iz] is None:
                return i
            i = iz

    def _mover_subarbol(self, origen, destino):
        # mover subarbol
        cola = [(origen, destino)]

        while len(cola) > 0:
            src, dst = cola.pop(0)

            self.expandir(max(src, dst))

            self.vec[dst] = self.vec[src]
            self.vec[src] = None

            if self.vec[dst] is not None:
                src_iz = self._hijo_izq(src)
                src_dr = self._hijo_der(src)

                dst_iz = self._hijo_izq(dst)
                dst_dr = self._hijo_der(dst)

                self.expandir(
                    max(src_iz, src_dr, dst_iz, dst_dr)
                )

                if self.vec[src_iz] is not None:
                    cola.append((src_iz, dst_iz))

                if self.vec[src_dr] is not None:
                    cola.append((src_dr, dst_dr))

    def lookup(self, llave):
        # lookup: retorna valor o none
        i = 1

        while i < len(self.vec):
            if self.vec[i] is None:
                return None

            llave_actual, valor_actual = self.vec[i]

            if llave == llave_actual:
                return valor_actual
            elif llave < llave_actual:
                i = self._hijo_izq(i)
            else:
                i = self._hijo_der(i)

        return None

    def keys(self):
        # keys: retorna llaves ordenadas
        res = []

        self._inorden_llaves(1, res)

        return res

    def _inorden_llaves(self, i, res):
        self.expandir(i)

        if self.vec[i] is None:
            return

        self._inorden_llaves(self._hijo_izq(i), res)

        res.append(self.vec[i][0])

        self._inorden_llaves(self._hijo_der(i), res)

    def print(self):
        # print: muestra contenido
        pares = []

        self._inorden_pares(1, pares)

        for llave, valor in pares:
            print("Llave:", llave, "| Valor:", valor)

        if not pares:
            print("Arreglo vacio")

    def _inorden_pares(self, i, res):
        self.expandir(i)

        if self.vec[i] is None:
            return

        self._inorden_pares(self._hijo_izq(i), res)

        res.append(self.vec[i])

        self._inorden_pares(self._hijo_der(i), res)