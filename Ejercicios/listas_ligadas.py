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


#######################################################################
# Lo que sigue no es parte de introduccion a la programacion, pero se #
# implementara para los curiosos                                      #
#######################################################################

print('\n' + '#' * 30 + '\n')


class MiListaReal(MiLista):
    """
    Lista que utilizara los metodos magicos de Python para hacerla mas
    practica, que hereda de MiLista para simplificar las operaciones

    """

    def __init__(self):
        """
        Se inicializa como cualquier Objeto, pero se tiene que hacer
        el paso a continuacion porque hereda

        """

        super(MiListaReal, self).__init__()

    def __getitem__(self, posicion):
        return self.data_en_pos(posicion)

    def __setitem__(self, posicion, nuevo_elemento):
        self.reemplazar(posicion, nuevo_elemento)

    def __len__(self):
        return self.cantidad

    def append(self, elemento):
        """
        Es el equivalente al append de una lista normal
        """
        self.agregar(elemento)


# Probemos nuestra nueva y mejorada lista
# Primero hay que instanciarla
LISTA_REAL = MiListaReal()

# Haremos la misma prueba que con MiLista
for num in range(10):
    LISTA_REAL.append(num)
    print('En la posicion:', num, 'esta:', LISTA_REAL[num])

print('-' * 25)
print('El largo de la lista es:', len(LISTA_REAL))
print('-' * 25)

for num in range(0, 10, 2):
    # el tercer argumento de range nos permite ir de 2 en dos
    # esto es, 0, 2, 4, 6, 8
    LISTA_REAL[num] = num * 2
    print('Ahora en la posicion:', num, 'esta:', LISTA_REAL[num])
