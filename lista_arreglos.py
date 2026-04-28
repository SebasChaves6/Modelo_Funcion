class lista_arreglos:
    """
    Arreglo asociativo ordenado por llave
    """
    def __init__(self):
        # Init: lista vacia
        self.llaves = []
        self.valores = []

    def clear(self):
        """
        Clear: vacia todo
        """
        self.llaves = []
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
        n = len(self.llaves)

        # buscar donde va
        while pos < n:
            if self.llaves[pos] >= llave:
                break
            pos += 1

        # si ya existe, actualizar
        if pos < n and self.llaves[pos] == llave:
            self.valores[pos] = valor
            return

        # insertar
        self.llaves.insert(pos, llave)
        self.valores.insert(pos, valor)

    def eliminar(self, llave):
        """
        elimina por llave
        """
        pos = 0
        n = len(self.llaves)

        # buscar
        while pos < n and self.llaves[pos] < llave:
            pos += 1

        # eliminar si esta
        if pos < n and self.llaves[pos] == llave:
            self.llaves.pop(pos)
            self.valores.pop(pos)

    def obtener(self, llave):
        """
        retorna valor o None
        """
        pos = 0
        n = len(self.llaves)

        while pos < n:
            if self.llaves[pos] == llave:
                return self.valores[pos]

            # ya se paso, no esta
            if self.llaves[pos] > llave:
                return None

            pos += 1

        return None

    def llaves(self):
        """
        llaves: retorna lista de llaves
        """
        return self.llaves.copy()

    def print(self):
        """
        Print: muestra contenido
        """
        i = 0
        while i < len(self.llaves):
            print("Llave:", self.llaves[i], "| Valor:", self.valores[i])
            i += 1