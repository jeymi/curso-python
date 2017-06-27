import random
mensaje= "el estudiante {0} de {1} de edad, es de la ciudad de {2} y cursa {3} en la universidad \n"
NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]
import random

def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'ciudad': random.choice(CIUDADES)
        }
    return estudiantes
if __name__ == '__main__':
    diccio = generar_diccionario_estudiantes()

    for llave,valor in diccio.iteritems() :
        print llave,valor


    print 'estudiantes de managua'
    for llave,valor in diccio.iteritems():
        if valor['ciudad'] == 'Managua':
            print mensaje.format(llave,valor['edad'],valor['ciudad'],valor['anio'])
    print 'estudiantes de masaya que cursan 1er anio'
    for llave,valor in diccio.iteritems():
        if valor['ciudad'] == 'Masaya' and valor['anio'] == 1:
            print mensaje.format(llave, valor['edad'], valor['ciudad'], valor['anio'])
    print 'estudiantes menores de 21'
    for llave,valor in diccio.iteritems():
        if valor['edad']<21:
            print mensaje.format(llave,valor['edad'],valor['ciudad'],valor['anio'])
            f = open('ejercicio.txt', 'a')
            f.write(mensaje.format(llave, valor['edad'], valor['ciudad'], valor['anio']))
            f.close()