class lista_arreglos:
    """
    Arreglo asociativo ordenado por llave
    """
    def __init__(self):
        # Init: lista vacia
        self.lista_llaves = []
        self.valores = []

    def clear(self):
        """
        Clear: vacia todo
        """
        self.lista_llaves = []
        self.valores = []

    def done(self):
        """
        Done: libera memoria
        """
        self.clear()

    def assign(self, llave, valor):
        """
        Assign: inserta o actualiza
        """
        pos = 0
        n = len(self.lista_llaves)

        # buscar donde va
        while pos < n:
            if self.lista_llaves[pos] >= llave:
                break
            pos += 1

        # si ya existe, actualizar
        if pos < n and self.lista_llaves[pos] == llave:
            self.valores[pos] = valor
            return

        # insertar
        self.lista_llaves.insert(pos, llave)
        self.valores.insert(pos, valor)

    def unassign(self, llave):
        """
        elimina por llave
        """
        pos = 0
        n = len(self.lista_llaves)

        # buscar
        while pos < n and self.lista_llaves[pos] < llave:
            pos += 1

        # eliminar si esta
        if pos < n and self.lista_llaves[pos] == llave:
            self.lista_llaves.pop(pos)
            self.valores.pop(pos)

    def lookup(self, llave):
        """
        retorna valor o None
        """
        pos = 0
        n = len(self.lista_llaves)

        while pos < n:
            if self.lista_llaves[pos] == llave:
                return self.valores[pos]

            # ya se paso, no esta
            if self.lista_llaves[pos] > llave:
                return None

            pos += 1

        return None

    def keys(self):
        """
        keys: retorna lista de llaves
        """
        return self.lista_llaves.copy()

    def print(self):
        """
        Print: muestra contenido
        """
        i = 0
        while i < len(self.lista_llaves):
            print("Llave:", self.lista_llaves[i], "| Valor:", self.valores[i])
            i += 1
