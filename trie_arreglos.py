class NodoTrieArreglo:
    """
    Nodo para el Trie por arreglos.
    Cada nodo guarda sus hijos en un arreglo fijo.
    """

    def __init__(self):

        # Arreglo para guardar los hijos
        self.hijos = [None] * 62

        # Valor asociado a una llave
        self.valor = None

        # Indica si el nodo es final de una llave
        self.es_final = False


class trie_arreglos:
    """
    Implementación del Modelo Función usando Trie por arreglos.
    """

    def __init__(self):

        # Raíz del Trie
        self.raiz = NodoTrieArreglo()

        # Cantidad de llaves guardadas
        self.tamano = 0

    def indice(self, caracter):

        # Convierte números en posiciones
        if '0' <= caracter <= '9':
            return ord(caracter) - ord('0')

        # Convierte mayúsculas en posiciones
        if 'A' <= caracter <= 'Z':
            return 10 + ord(caracter) - ord('A')

        # Convierte minúsculas en posiciones
        if 'a' <= caracter <= 'z':
            return 36 + ord(caracter) - ord('a')

        return -1

    def caracter(self, indice):

        # Convierte posición a número
        if 0 <= indice <= 9:
            return chr(ord('0') + indice)

        # Convierte posición a mayúscula
        if 10 <= indice <= 35:
            return chr(ord('A') + indice - 10)

        # Convierte posición a minúscula
        if 36 <= indice <= 61:
            return chr(ord('a') + indice - 36)

        return ""

    def validar_llave(self, llave):

        # Revisa que la llave sea válida
        return isinstance(llave, str) and len(llave) <= 20 and llave.isalnum()

    def validar_valor(self, valor):

        # Revisa que el valor tenga 20 letras minúsculas
        return isinstance(valor, str) and len(valor) == 20 and valor.isalpha() and valor.islower()

    def clear(self):

        # Vacía el Trie
        self.raiz = NodoTrieArreglo()
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
        for c in llave:

            pos = self.indice(c)

            # Crear nodo si no existe
            if actual.hijos[pos] is None:
                actual.hijos[pos] = NodoTrieArreglo()

            actual = actual.hijos[pos]

        # Si la llave es nueva aumenta el tamaño
        if not actual.es_final:
            self.tamano += 1

        # Guardar valor
        actual.es_final = True
        actual.valor = valor

    def lookup(self, llave):

        # Si la llave no es válida retorna None
        if not self.validar_llave(llave):
            return None

        actual = self.raiz

        # Recorrer la llave
        for c in llave:

            pos = self.indice(c)

            # Si no existe el camino la llave no existe
            if actual.hijos[pos] is None:
                return None

            actual = actual.hijos[pos]

        # Retorna el valor si existe
        if actual.es_final:
            return actual.valor

        return None

    def tiene_hijos(self, nodo):

        # Revisa si el nodo tiene hijos
        for hijo in nodo.hijos:
            if hijo is not None:
                return True

        return False

    def unassign(self, llave):

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
                return not self.tiene_hijos(nodo)

            pos = self.indice(llave[posicion])

            # Si no existe el camino
            if nodo.hijos[pos] is None:
                return False

            debe_borrar = borrar(nodo.hijos[pos], posicion + 1)

            # Borra el hijo si ya no se ocupa
            if debe_borrar:
                nodo.hijos[pos] = None

                return (not nodo.es_final) and (not self.tiene_hijos(nodo))

            return False

        # Inicia el borrado desde la raíz
        borrar(self.raiz, 0)

    def keys(self):

        # Lista donde se guardan las llaves
        resultado = []

        def recorrer(nodo, prefijo):

            # Si es final guarda la llave
            if nodo.es_final:
                resultado.append(prefijo)

            i = 0

            # Recorre todas las posiciones del arreglo
            while i < 62:

                # Si existe hijo sigue recorriendo
                if nodo.hijos[i] is not None:
                    recorrer(nodo.hijos[i], prefijo + self.caracter(i))

                i += 1

        # Empezar recorrido desde la raíz
        recorrer(self.raiz, "")

        return resultado

    def print(self):

        # Imprime todas las relaciones
        for llave in self.keys():
            print("Llave:", llave, "| Valor:", self.lookup(llave))
