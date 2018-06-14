'''Programacion orientada a objetos

La programacion orientada a objetos, u OOP (por su sigla en ingles
Object Oriented Programing) es fundamental para poder modelar cosas como lo
son en la vida real.

Hay que pensar en la OOP como si se estuviese construyendo un "algo" desde
el punto de vista de programacion. En otras palabras, los objetos son una
abstraccion que permite construir un "algo" "tangible", el cual tendra
propiedades y posiblemente funciones.

'''


# Primero repasaremos como se define un objeto


# Para definir un objeto se debe poner "class NombreDelObjeto:"
class NombreDelObjeto:
    '''
    Nuestro objeto hipotetico va a tener el nombre que se le asigne
    despues del espacio de class
    '''

    # Ahora le asignamos un nombre, nuestro objeto tiene una identidad
    # con la cual podemos identificarlo

    # Cabe recordar que ademas es importante siempre recordar que se debe
    # definir la funcion "__init__" de la forma siguiente:
    # (vamos a abreviar "elemento_fundamental_de_nuestro_objeto" como "efo")
    # "def __init__(mi_mismo, efo_1, efo_2, efo_3, ...):"

    def __init__(mi_mismo, efo_1, efo_2):
        # Cabe notar que "mi_mismo" es lo mismo que decir el conocido "self".

        # Es importante destacar que "self", en realidad puede ser cualquier
        # nombre, siempre y cuando nos referenciemos a nosotros mismos
        # (mi_mismo) de la misma manera en el objeto:
        # La moraleja es, hay que ser consistente con los nombres

        # El metodo __init__ es para "inicializar" la clase, es decir,
        # cada vez que queramos crear un nuevo objeto de este tipo, se va a
        # llamar esta funcion, la cual va a definir los atriutos intrinsecos
        # de ese objeto nuevo en particular

        # Por el momento vamos definir nuestros elementos fundamentales
        mi_mismo.efo_1 = efo_1
        mi_mismo.efo_2 = efo_2

        # Lo anterior es lo mismo que decir
        # self.efo_1 = efo_1
        # y
        # self.efo_2 = efo_2

        # Lo que hemos hecho anteriormente es decirle a Python :snake:
        # que cada vez que creemos un nuevo objeto del tipo NombreDelObjeto
        # este tendra las caracteristicas efo_1 y efo_2 que le asignamos
