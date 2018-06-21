"""
Modulo para aquellos que estan motivados con programacion para darles una
pincelada de lo que realmente se puede hacer.

Se hace uso de herencia y dunder methods.

Para poder utilizar el modulo se debe tener el archivo listas ligadas en el
la misma carpeta que este archivo.
"""

from listas_ligadas import MiLista


class MiListaReal(MiLista):
    """
    Lista que utilizara los metodos magicos de Python para hacerla mas
    practica, que hereda de MiLista para simplificar las operaciones
    """

    def __init__(self):
        """
        Se inicializa como cualquier Objeto, pero se tiene que hacer
        el paso a continuacion porque hereda de otro objeto
        """

        # El metodo super().__init__() es utilizado para crear la instancia
        # del objeto del cual hereda
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
