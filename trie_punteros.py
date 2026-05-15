class NodoTrie:
    """
    Nodo para el Trie por punteros.
    """

    def __init__(self):

        # Diccionario para guardar hijos
        self.hijos = {}

        # Valor asociado a la llave
        self.valor = None

        # Indica si aquí termina una llave
        self.es_final = False


class trie_punteros:
    """
    Implementación del Modelo Función usando Trie por punteros.
    """

    def __init__(self):

        # Raíz del Trie
        self.raiz = NodoTrie()

        # Cantidad de llaves almacenadas
        self.tamano = 0

    def validar_llave(self, llave):

        # Revisa que la llave sea válida
        return isinstance(llave, str) and len(llave) <= 20 and llave.isalnum()

    def validar_valor(self, valor):

        # Revisa que el valor tenga 20 letras minúsculas
        return isinstance(valor, str) and len(valor) == 20 and valor.isalpha() and valor.islower()

    def clear(self):

        # Vacía el Trie
        self.raiz = NodoTrie()
        self.tamano = 0

    def done(self):

        # Libera memoria
        self.clear()

    def assign(self, llave, valor):

        # Validar llave
        if not self.validar_llave(llave):
            print("Llave invalida.")
            return

        # Validar valor
        if not self.validar_valor(valor):
            print("Valor invalido.")
            return

        # Empezar desde la raíz
        actual = self.raiz

        # Recorrer la llave caracter por caracter
        for caracter in llave:

            # Crear nodo si no existe
            if caracter not in actual.hijos:
                actual.hijos[caracter] = NodoTrie()

            actual = actual.hijos[caracter]

        # Si la llave es nueva aumenta el tamaño
        if not actual.es_final:
            self.tamano += 1

        # Guardar valor
        actual.es_final = True
        actual.valor = valor

    def obtener(self, llave):

        # Si la llave no es válida retorna None
        if not self.validar_llave(llave):
            return None

        actual = self.raiz

        # Recorrer la llave
        for caracter in llave:

            # Si no existe el camino la llave no existe
            if caracter not in actual.hijos:
                return None

            actual = actual.hijos[caracter]

        # Retorna el valor si existe
        if actual.es_final:
            return actual.valor

        return None

    def eliminar(self, llave):

        # Si la llave no es válida no hace nada
        if not self.validar_llave(llave):
            return

        def borrar(nodo, posicion):

            # Llegó al final de la llave
            if posicion == len(llave):

                # La llave no existe
                if not nodo.es_final:
                    return False

                # Eliminar información
                nodo.es_final = False
                nodo.valor = None
                self.tamano -= 1

                # Retorna True si el nodo puede borrarse
                return len(nodo.hijos) == 0

            caracter = llave[posicion]

            # Si el camino no existe
            if caracter not in nodo.hijos:
                return False

            debe_borrar = borrar(nodo.hijos[caracter], posicion + 1)

            # Borra el nodo si ya no se ocupa
            if debe_borrar:
                del nodo.hijos[caracter]

                return (not nodo.es_final) and len(nodo.hijos) == 0

            return False

        # Empezar borrado desde la raíz
        borrar(self.raiz, 0)

    def llaves(self):

        # Lista para guardar llaves
        resultado = []

        def recorrer(nodo, prefijo):

            # Si es final guarda la llave
            if nodo.es_final:
                resultado.append(prefijo)

            # Recorre los hijos en orden
            for caracter in sorted(nodo.hijos.keys()):
                recorrer(nodo.hijos[caracter], prefijo + caracter)

        # Empezar recorrido desde la raíz
        recorrer(self.raiz, "")

        return resultado

    def print(self):

        # Imprime todas las relaciones
        for llave in self.llaves():
            print("Llave:", llave, "| Valor:", self.obtener(llave))

    # Métodos puente para mantener el mismo estilo

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
