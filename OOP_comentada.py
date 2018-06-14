'''
Programacion orientada a objetos

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
    despues del espacio de "class"
    '''

    # Ahora le asignamos un nombre, nuestro objeto tiene una identidad
    # con la cual podemos identificarlo

    # Cabe recordar que ademas es importante siempre recordar que se debe
    # definir la funcion "__init__" de la forma siguiente:
    # (vamos a abreviar "elemento_fundamental_de_nuestro_objeto" como "efo")
    # "def __init__(self, efo_1, efo_2, efo_3, ...):"

    def __init__(self, efo_1, efo_2):
        # Cabe notar que "self" lo unico que hace es referenciarse a uno mismo,
        # en otras palabras, es como decir "yo voy a tener estas cosas".

        # Es importante destacar que "self", en realidad puede ser cualquier
        # nombre, siempre y cuando nos referenciemos a nosotros mismos
        # (mi_mismo) de la misma manera en el objeto:
        # La moraleja es, hay que ser consistente con los nombres

        # El metodo __init__ es para "inicializar" la clase, es decir,
        # cada vez que queramos crear un nuevo objeto de este tipo, se va a
        # llamar esta funcion, la cual va a definir los atriutos intrinsecos
        # de ese objeto nuevo en particular

        # Por el momento vamos definir nuestros elementos fundamentales
        self.efo_1 = efo_1
        self.efo_2 = efo_2

        # Lo anterior es lo mismo que decir
        # mi_mismo.efo_1 = efo_1
        # mi_mismo.efo_2 = efo_2

        # Lo que hemos hecho anteriormente es decirle a Python :snake:
        # que cada vez que creemos un nuevo objeto del tipo NombreDelObjeto
        # este tendra las caracteristicas efo_1 y efo_2 que le asignamos

    # Como ya sabemos que NombreDelObjeto tiene los atributos efo_1 y efo_2
    # podemos definir cosas caracteristicas que NombreDelObjeto puede hacer
    # digamos, por ejemplo, que al pedirle "haz_algo", se niegue a hacerlo
    # y nos lo diga diciendo que no puede por tener efo_1.

    # Esto podemos definirlo de la siguiente forma
    def haz_algo(self, argumento_1):
        '''
        Notar que cada funcion que sea parte de nuestro objeto NombreDelObjeto
        tendra que tener el argumento "self" para poder hacer referencia a
        a si mismo. Es decir, si no se incluye el "self", se estaria
        haciendo alusion a una variable que puede estar en cualquier parte,
        lo cual no es deseable en este tipo de modelacion.
        '''

        # Es importante notar que una funcion de un objeto tambien puede
        # recibir parametros externos al objeto mismo, lo cual permite
        # dar flexibilidad en lo que puede hacer.

        # Una particularidad especial de los objetos es que no necesariamente
        # deben retornar algo, ya que simplemente pueden hacer algo con
        # elementos de si mismos. Por ejemplo si una persona se rasca la
        # espalda no tiene porque notificar al resto que se rasco

        # En este caso vamos a sobreescribir "self.efo_1" con el argumento
        # que recibio nuestra funcion
        self.efo_1 = argumento_1
        # si ahora quisieramos usar "self.efo_1" en el resto de nuestro objeto,
        # ya no estariamos haciendo referencia al argumento efo_1 que recibimos
        # cuando declaramos nuestra funcion __init__, es decir, nuestra
        # variable de objeto fue sobreescrita en su totalidad

        # Asumamos que argumento_1 es un numero, entonces, recordando el
        # comienzo del curso, podemos concatenar un string (texto) con un
        # numero si hacemos este numero un string
        print("No puedo hacerlo por tener el atributo " + str(self.efo_1))

        # No retornaremos nada para demostrar que esto es perfectamente posible


# Ahora que hemos sentado las bases de la idea detras de un objeto, hagamos
# algo mas concreto, definamos nuestro "creativo" lenguaje de programacion
