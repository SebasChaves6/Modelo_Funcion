class tabla_hash:
    """
    Implementación de una tabla hash abierta (con listas en cada posición).
    Cada posición de la tabla guarda una lista de pares [llave, valor].
    """

    def __init__(self, capacidad=10):
        # tamaño de la tabla
        self.capacidad = capacidad

        # la tabla es una lista de listas
        self.tabla = []
        self.tamano = 0

        # inicializar cada posición como lista vacía
        for i in range(capacidad):
            self.tabla.append([])

    def funcion_hash(self, llave):
        """
        Convierte la llave (string) en un índice de la tabla.
        Se usa una fórmula simple acumulando valores ASCII.
        """
        h = 0

        for c in llave:
            h = h * 31 + ord(c)

        return h % self.capacidad

    def clear(self):
        """
        Vacía completamente la tabla
        """
        self.tabla = []
        self.tamano = 0

        for i in range(self.capacidad):
            self.tabla.append([])

    def done(self):
        """
        Libera memoria (en Python es igual que limpiar)
        """
        self.clear()

    def assign(self, llave, valor):
        """
        Inserta o actualiza una relación llave-valor
        """
        indice = self.funcion_hash(llave)

        # obtener la lista donde va a caer (colisión)
        cubeta = self.tabla[indice]

        # revisar si ya existe la llave
        for par in cubeta:
            if par[0] == llave:
                par[1] = valor  # actualizar
                return

        # si no existe, se agrega
        cubeta.append([llave, valor])
        self.tamano += 1

    def eliminar(self, llave):
        """
        Elimina una llave si existe
        """
        indice = self.funcion_hash(llave)
        cubeta = self.tabla[indice]

        i = 0
        while i < len(cubeta):
            if cubeta[i][0] == llave:
                cubeta.pop(i)
                self.tamano -= 1
                return
            i += 1

    def obtener(self, llave):
        """
        Busca una llave y devuelve su valor
        """
        indice = self.funcion_hash(llave)
        cubeta = self.tabla[indice]

        for par in cubeta:
            if par[0] == llave:
                return par[1]

        return None

    def llaves(self):
        """
        Devuelve todas las llaves almacenadas
        """
        resultado = []

        for cubeta in self.tabla:
            for par in cubeta:
                resultado.append(par[0])

        return resultado

    def print(self):
        """
        Imprime todas las relaciones
        """
        for cubeta in self.tabla:
            for par in cubeta:
                print("Llave:", par[0], "| Valor:", par[1])

    # ===== Métodos puente (para el menú) =====

    def limpie(self):
        self.clear()

    def asigne(self, llave, valor):
        self.assign(llave, valor)

    def elimine(self, llave):
        self.eliminar(llave)

    def lookup(self, llave):
        return self.obtener(llave)

    def imprimir(self):
        self.print()