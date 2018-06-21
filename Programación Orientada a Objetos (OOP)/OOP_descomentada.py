class NombreDelObjeto:

    def __init__(self, efo_1, efo_2):

        self.efo_1 = efo_1
        self.efo_2 = efo_2

    def haz_algo(self, argumento_1):

        self.efo_1 = argumento_1

        print("No puedo hacerlo por tener el atributo " + str(self.efo_1))


class LenguajeDeProgramacion:

    def __init__(self, quien_soy):
        self.quien_soy = quien_soy

    def espejito_espejito_a_quien_imito(self):
        return 'Tu imitas a ' + self.quien_soy

    def cambia_mi_esencia_de_programacion(self, redefinicion):
        print('Voy a pasar de ser ' + self.quien_soy + ' a ' + redefinicion)

        self.quien_soy = redefinicion

        print('Ahora soy ' + self.quien_soy)


python = LenguajeDeProgramacion('Python')
wannabe_python = LenguajeDeProgramacion('Python')


print('python se ubica en: ' + python.__repr__())
print('wannabe_python se ubica en: ' + wannabe_python.__repr__())


print(python.__repr__() == wannabe_python.__repr__())
print(python.quien_soy == wannabe_python.quien_soy)


wannabe_python.cambia_mi_esencia_de_programacion('Cobra')


print(wannabe_python.quien_soy)
print(python.quien_soy)
