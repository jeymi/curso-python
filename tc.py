class Mascota(object):
    def __init__(self,gato,perro = 'inu'):
        self.gato= gato
        self.perro = perro
    def obtener_datos(self):
        print 'nombres'
        return '{gato} ,{perro}' .format(
            gato = self.gato,
            perro = self.perro
        )
class Argumentos(Mascota):

    def obtener_argum(self):
        def __init__(self, dato, nombre):
            super(Argumentos, self).__init__(nombre)
            self.dato = dato

        def obtener_info(self):
            return self.datos

if __name__ =='__main__':
    argu = Argumentos('parecido','nombres')
    print argu.obtener_datos()