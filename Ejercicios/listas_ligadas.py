""" Modulo para definir nuestras propias listas """


class Nodo:
    """
    Lugar en que se almacena la informacion que queremos
    """

    def __init__(self, posicion, elemento):
        self.elemento = elemento
        self.posicion = posicion
        self.hijo = None

    def agregar(self, elemento):
        """
        Es el equivalente a hacer un append, pero si el nodo esta
        ocupado, entonces crea un hijo y almacena la informacion ahi

        param: elemento
        """

        if self.hijo is None:
            self.hijo = Nodo(self.posicion + 1, elemento)

        else:
            # aqui estamos haciendo un llamado recursivo
            self.hijo.agregar(elemento)

    def data_en_pos(self, posicion):
        """
        Funcion recursiva que sigue buscando hasta encontrar el numero
        del indice indicado

        param: posicion (int) -> numero de posicion
        """

        if self.posicion == posicion:
            # caso base de nuestra recursion
            return self.elemento

        # caso recursivo
        return self.hijo.data_en_pos(posicion)

    def reemplazar(self, posicion, nuevo_elemento):
        """
        Funcion que permite sobreescribir la informacion de un nodo dado

        param: posicion (int) -> posicion a reemplazar
        param: nuevo elemento -> cualquier cosa que se quiera
        """

        if self.posicion == posicion:
            # caso base
            self.elemento = nuevo_elemento

        else:
            # caso recursivo
            self.hijo.reemplazar(posicion, nuevo_elemento)

    def dame_todo(self, vuelta):
        """
        Es el equivalente a un print de una lista normal

        param: vuelta (string) -> va agregando recursivamete los elementos
                                  de cada nodo
        """

        # nuestro caso base en el que se inicia el llamado recursivo
        if vuelta == "":
            vuelta += "[" + str(self.elemento) + ", "
            return self.hijo.dame_todo(vuelta)

        # verifico si pued seguir haciendo la recursion
        elif self.hijo is None:
            vuelta += str(self.elemento) + "]"
            return vuelta

        # si estoy en un caso intermedio solo agrego el elemento que contengo
        vuelta += str(self.elemento) + ", "
        return self.hijo.dame_todo(vuelta)


class MiLista:
    """
    Una lista tal como las comunes y corrientes
    """

    def __init__(self):
        self.nodo = None
        self.cantidad = 0

    def agregar(self, elemento):
        """
        Es el equivalente a hacer un append de una lista normal

        param: cualquier tipo de cosa que se quiera agregar a la lista
        """

        if self.nodo is None:
            # caso base
            self.nodo = Nodo(self.cantidad, elemento=elemento)
            self.cantidad += 1

        else:
            # caso recursivo
            self.nodo.agregar(elemento=elemento)
            self.cantidad += 1

    def data_en_pos(self, posicion):
        """
        Es el equivalente a hacer un lista[pos]

        param: posicion (int) -> numero de posicion en la lista
        """

        return self.nodo.data_en_pos(posicion)

    def largo(self):
        """
        Funcion que retorna el largo actual de la lista
        """
        return self.cantidad

    def reemplazar(self, posicion, nuevo_elemento):
        """
        Funcion que permite sobreescribir la informacion de un nodo dado

        param: posicion (int) -> posicion a reemplazar
        param: nuevo elemento -> cualquier cosa que se quiera
        """

        self.nodo.reemplazar(posicion, nuevo_elemento)

    def dame_todo(self):
        """
        Es el equivalente a un print() de una lista normal
        """

        # se le tiene que dar un string vacio para comenzar
        return self.nodo.dame_todo("")


if __name__ == '__main__':
    # Ahora probemos nuestra lista
    # Instanciamos la lista que creamos
    MI_LISTA = MiLista()

    # Probameros agregando 10 elementos
    for num in range(10):
        MI_LISTA.agregar(num)
        print('En la posicion:', num, 'esta:', MI_LISTA.data_en_pos(num))

    print('-' * 25)
    print('El largo de la lista es:', MI_LISTA.largo())
    print('-' * 25)

    for num in range(0, 10, 2):
        # el tercer argumento de range nos permite ir de 2 en dos
        # esto es, 0, 2, 4, 6, 8
        MI_LISTA.reemplazar(num, num * 2)
        print('Ahora en la posicion:', num, 'esta:', MI_LISTA.data_en_pos(num))

    # probamos que se pueda imprimir bien
    print('-' * 25)
    print('Tambien se puede imprimir nuestra lista:', MI_LISTA.dame_todo())
