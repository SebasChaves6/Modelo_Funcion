class Hijo:
    """
    Nodo para enlazar hijos del Trie (Lista simplemente enlazada).
    """
    def __init__(self, caracter, nodo):
        self.caracter = caracter
        self.nodo = nodo
        self.siguiente = None


class NodoTrie:
    """
    Nodo para el Trie por punteros.
    """
    def __init__(self):
        # Inicio de la lista enlazada de hijos
        self.hijos = None
        
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
        # Revisa que la llave sea válida (Alfanumérica, max 20 chars)
        return (
            isinstance(llave, str)
            and len(llave) <= 20
            and llave.isalnum()
        )

    def validar_valor(self, valor):
        # Revisa que el valor tenga exactamente 20 letras minúsculas (a-z)
        return (
            isinstance(valor, str)
            and len(valor) == 20
            and valor.isalpha()
            and valor.islower()
        )

    def clear(self):
        # Vacía el Trie
        self.raiz = NodoTrie()
        self.tamano = 0

    def done(self):
        # Libera memoria
        self.clear()

    def _buscar_hijo(self, nodo, caracter):
        actual = nodo.hijos

        while actual is not None:
            if actual.caracter == caracter:
                return actual
            actual = actual.siguiente

        return None

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
            hijo = self._buscar_hijo(actual, caracter)

            # Crear nodo si no existe
            if hijo is None:
                nuevo_nodo = NodoTrie()
                nuevo_hijo = Hijo(caracter, nuevo_nodo)

                # Insertar en la lista enlazada manteniendo orden alfabético
                if actual.hijos is None or caracter < actual.hijos.caracter:
                    # Va de primero
                    nuevo_hijo.siguiente = actual.hijos
                    actual.hijos = nuevo_hijo
                else:
                    # Buscar la posición correcta en el medio o al final
                    temp = actual.hijos
                    while temp.siguiente is not None and temp.siguiente.caracter < caracter:
                        temp = temp.siguiente
                    
                    nuevo_hijo.siguiente = temp.siguiente
                    temp.siguiente = nuevo_hijo

                actual = nuevo_nodo

            else:
                actual = hijo.nodo

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
        for caracter in llave:
            hijo = self._buscar_hijo(actual, caracter)

            # Si no existe el camino la llave no existe
            if hijo is None:
                return None

            actual = hijo.nodo

        # Retorna el valor si existe
        if actual.es_final:
            return actual.valor

        return None

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

                # Retorna True si no tiene hijos
                return nodo.hijos is None

            caracter = llave[posicion]

            actual = nodo.hijos
            anterior = None

            while actual is not None:
                if actual.caracter == caracter:
                    debe_borrar = borrar(
                        actual.nodo,
                        posicion + 1
                    )

                    # Borra el hijo si ya no se ocupa
                    if debe_borrar:
                        if anterior is None:
                            nodo.hijos = actual.siguiente
                        else:
                            anterior.siguiente = actual.siguiente

                    return (
                        not nodo.es_final
                        and nodo.hijos is None
                    )

                anterior = actual
                actual = actual.siguiente

            return False

        # Empezar borrado desde la raíz
        borrar(self.raiz, 0)

    def keys(self):
        # Lista para guardar llaves
        resultado = []

        def recorrer(nodo, prefijo):
            # Si es final guarda la llave
            if nodo.es_final:
                resultado.append(prefijo)

            actual = nodo.hijos

            while actual is not None:
                recorrer(
                    actual.nodo,
                    prefijo + actual.caracter
                )
                actual = actual.siguiente

        # Empezar recorrido desde la raíz
        recorrer(self.raiz, "")

        return resultado

    def print(self):
        # Imprime todas las relaciones
        for llave in self.keys():
            print(
                "Llave:",
                llave,
                "| Valor:",
                self.lookup(llave)
            )
